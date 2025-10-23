import os 
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import datetime 
from zoneinfo import ZoneInfo

SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/spreadsheets'
]

class GoogleAPIClient:
    def __init__(self,credentials="credentials.json"):
        self.credentials = credentials
        self.creds = None
        self.authenticate()
        
        self.calendar_service = build(serviceName="calendar",version="v3",credentials=self.creds)
        self.sheets_service = build('sheets', 'v4', credentials=self.creds)
         
    def authenticate(self):
        if os.path.exists("token.pickle"):
            with open("token.pickle",'rb') as token:
                self.creds = pickle.load(token)
        
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    client_secrets_file=self.credentials,
                    scopes=SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            with open("token.pickle",'wb') as token:
                pickle.dump(self.creds,token)
                
    def create_calendar_service(self,summary,location,description,start_time,end_time):
        
        
        if isinstance(start_time, str):
            start_time = start_time.replace('Z', '+00:00') if 'Z' in start_time else start_time
            start_time = datetime.datetime.fromisoformat(start_time)
        if isinstance(end_time, str):
            end_time = end_time.replace('Z', '+00:00') if 'Z' in end_time else end_time
            end_time = datetime.datetime.fromisoformat(end_time)
            
        # Ensure timezone is set to IST
        if start_time.tzinfo is None:
            start_time = start_time.replace(tzinfo=ZoneInfo('Asia/Kolkata'))
        if end_time.tzinfo is None:
            end_time = end_time.replace(tzinfo=ZoneInfo('Asia/Kolkata'))
        
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': 'Asia/Kolkata',
            },
        }
        
        if description is not None:
            event["description"] = str(description)
        if location is not None:
            event["location"] = str(location)
        
        event = self.calendar_service.events().insert(
            calendarId="primary",
            body=event
        ).execute()
        print(f"Event created: {event.get('htmlLink')}")
        return event
    
    def list_upcoming_events(self,max_results=10):
        now = datetime.datetime.now(ZoneInfo("Asia/Kolkata")).isoformat()
        
        events_result = self.calendar_service.events().list(
            calendarId="primary",
            timeMin=now,
            maxResults = max_results,
            singleEvents=True,
            orderBy="startTime"
        ).execute()
        events = events_result.get("items",[])
        
        if not events:
            print("No upcoming events found.")
            return []
        
        print(f"Upcoming {len(events)} events:")
        for event in events:
            start = event['start'].get('dateTime',event['start'].get('date'))
            print(f"{start}: {event['summary']}")
        return events
    
    def delete_calendar_event(self,event_id):
        self.calendar_service.events().delete(
            calendarId="primary",
            eventId=event_id
        ).execute()
        print(f"Event with ID {event_id} deleted successfully.")
        
    def create_spreadsheet(self,title):
        spreadsheet = {
            "properties":{
                "title":title
            }
        }
        spreadsheet = self.sheets_service.spreadsheets().create(body=spreadsheet,fields="spreadsheetId").execute()
        spreadsheet_id = spreadsheet.get("spreadsheetId")
        print(f"Spreadsheet ID: {spreadsheet_id}")
        return spreadsheet_id
    
    def write_to_spreadsheet(self,spreadsheet_id,range_name,values):
        body = {
            'values':values
        }
        result = self.sheets_service.spreadsheets().values().update(
           spreadsheetId = spreadsheet_id,range=range_name,valueInputOption="RAW",body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    
    def read_from_spreadsheet(self,spreadsheet_id,range_name):
        result = self.sheets_service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,range=range_name).execute()
        values = result.get('values',[])
        
        if not values:
            print("No data found.")
            return []
        
        print(f"Data from {range_name}:")
        for row in values:
            print(row)
        return values
    
    def append_to_spreadsheet(self, spreadsheet_id, range_name, values):
        body = {
            'values': values
        }
        result = self.sheets_service.spreadsheets().values.append(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption='RAW', body=body).execute()
        print(f"{result.get('updates').get('updatedCells')} cells appended.")
        return result

        
        