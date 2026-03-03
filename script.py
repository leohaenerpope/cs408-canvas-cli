import os
import requests
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

BASE_URL = "https://boisestatecanvas.instructure.com/api/v1"
TOKEN = os.getenv("CANVAS_API_TOKEN")

if not TOKEN:
    raise ValueError("Missing CANVAS_API_TOKEN: Check/create your .env file")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

def get_canvas_courses():
    # Adding per_page=100 to handle more results in one go
    endpoint = f"{BASE_URL}/courses?per_page=100"
    
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        courses = response.json()
        
        print(f"{'ID':<10} | {'Course Name'}")
        print("-" * 50)
        
        for course in courses:
            # Note: Canvas sometimes returns 'None' for names if you 
            # aren't technically 'enrolled' in a deleted/old shell.
            name = course.get('name') or course.get('course_code', 'Unknown')
            print(f"{course.get('id'):<10} | {name}")
            
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    get_canvas_courses()