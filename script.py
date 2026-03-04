import os
import requests
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

BASE_URL = "https://boisestatecanvas.instructure.com/api/v1"
TOKEN = os.getenv("CANVAS_API_TOKEN")

# Handle .env file using python library dotenv

if not TOKEN:
    raise ValueError("Missing CANVAS_API_TOKEN: Check/create your .env file")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

def get_canvas_courses():
    print("-" * 100)
    print("BSU CANVAS GRADE TRACKER")
    print("-" * 100)

    # Parse and handle user input, no input means show all grades
    specific_id_input = input("\nEnter class ID for specific class (leave blank to view all class grades):\n")
    specific_id = -1
    found_specific_grade_switch = False
    if specific_id_input.isdigit():
        specific_id = int(specific_id_input)
        if specific_id < 0:
            print("Invalid input: class ID should be a number >= 0! Continuing to show all class grades.\n")
            specific_id = -1
        else:
            found_specific_grade_switch = True
    else:
        if specific_id_input != "":
            print("Invalid input: class ID should be a number >= 0! Continuing to show all class grades.\n")
        print("Displaying all grades, please wait while data is retrieved...")

    print("")

    # Adding per_page=100 to handle more results in one go
    url = f"{BASE_URL}/courses?per_page=100&include[]=total_scores"
    courses = []
    
    # Get Courses, 1st api call
    try:
        while url: # Handles pagination
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            courses.extend(response.json())
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                url = None
        
        print(f"{'ID':<10} | {'Course Name':<60} | {'Grade':<8} | {'Score'}")
        print("-" * 100)
        
        for course in courses:
            # Note: Canvas sometimes returns 'None' for names if you 
            # aren't technically 'enrolled' in a deleted/old shell.
            name = course.get('name') or course.get('course_code', 'Unknown')
            if name == 'Unknown':
                continue

            id = course.get('id')
            if specific_id != -1 and id != specific_id:
                continue
            elif not found_specific_grade_switch:
                found_specific_grade_switch = False
            
            # Now get enrollment information given course id from courses retrieval, 2nd api call
            try:
                # Now get enrollment information given course id from courses retrieval, 2nd api call
                response2 = requests.get(f"{BASE_URL}/courses/{id}/enrollments?per_page=200", headers=headers)
                response2.raise_for_status()
                enrollments = response2.json()

                if enrollments:
                    for enrollment in enrollments:
                        grades = enrollment.get('grades', {})
                        current_grade = grades.get('current_grade', 'N/A')
                        current_score = grades.get('current_score', 'N/A')
                        if current_grade is None or current_score is None:
                            continue
                        if current_grade != 'N/A' and current_score != 'N/A': # only user (since they have token) can have the current_grade object
                            print(f"{id:<10} | {name[:50]:<60} | {current_grade:<8} | {current_score}%")
                            break
            except requests.exceptions.RequestException as e:
                # Catches potential error trying to retrieve enrollment grade.
                continue
        if found_specific_grade_switch:
            print("\nCouldn't find specific class!\n")
        else:
            print("\nComplete!\n")
            
    except requests.exceptions.RequestException as e: # Let user know if there is an api error, such as invalid user token.
        print(f"API Error: {e}")
        print("Hint: Token probably not recognized, check .env")

if __name__ == "__main__":
    get_canvas_courses()