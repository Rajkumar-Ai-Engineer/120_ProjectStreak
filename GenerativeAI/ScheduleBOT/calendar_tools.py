import datetime
from typing import Dict, Any, List
from helper import GoogleAPIClient

class CalendarTools:
    def __init__(self):
        self.client = GoogleAPIClient()
    
    def create_calendar_service(self, summary: str, start_time: str, end_time: str, 
                              description: str = None, location: str = None) -> str:
      
        try:
            start_dt = datetime.datetime.fromisoformat(start_time)
            end_dt = datetime.datetime.fromisoformat(end_time)
            
            event = self.client.create_calendar_service(
                summary=summary,
                start_time=start_dt,
                end_time=end_dt,
                description=description,
                location=location
            )
            return f"Event created successfully: {event.get('summary')} - {event.get('htmlLink')}"
        except Exception as e:
            return f"Error creating event: {str(e)}"
    
    def list_upcoming_events(self, max_results: int = 10) -> str:
       
        try:
            events = self.client.list_upcoming_events(max_results=max_results)
            if not events:
                return "No upcoming events found."
            
            result = f"Found {len(events)} upcoming events:\n"
            for event in events:
                start = event.get("start", {}).get("dateTime", "No time")
                result += f"- {event.get('summary')}: {start}\n"
            return result
        except Exception as e:
            return f"Error listing events: {str(e)}"
    
    def delete_calendar_event(self, event_id: str) -> str:
        
        try:
            self.client.delete_calendar_event(event_id)
            return f"Event {event_id} deleted successfully"
        except Exception as e:
            return f"Error deleting event: {str(e)}"
