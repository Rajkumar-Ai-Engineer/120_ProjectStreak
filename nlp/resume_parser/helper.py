from google import genai
from dotenv import load_dotenv
load_dotenv()
import os 
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class resume_parser:
    
    def __init__(self):
        self.llm_key = os.getenv("GEMINI_API_KEY"),
        self.model_id = "gemini-2.0-flash",
        self.prompt =  """
                                You are an intelligent HR assistant. Analyze this resume and extract:

                                - Full Name
                                - Email
                                - Phone
                                - Skills
                                - Education
                                - Experience
                                - Is the candidate suitable for a AI Engineer  job? (Yes/No)
                                - Justify your decision.

                                Resume Text:
                                {ocr_output}
                            
                        Note: Reduce the output as much as possible,avoid unnecessary details, and focus on the key information.
            
                        """
    
    def img_text(self,image):
        
        try:
            ocr_output = pytesseract.image_to_string(image)
            if not ocr_output.strip():
                return "No text found in the image."
            return ocr_output
        except Exception as e:
            return f"Error processing image: {str(e)}"
    
    def parse_resume(self, image):
        ocr_output = self.img_text(image)
        if "Error" in ocr_output:
            return ocr_output
        
        prompt = self.prompt.format(ocr_output=ocr_output)
        
        client = genai.Client(api_key=self.llm_key[0])
        response = client.models.generate_content(model=self.model_id[0], contents=prompt)
        
        return response.text
