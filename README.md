# CS408 Canvas CLI Project

This is a lab for my BSU CS408 class that utilizes Instructure Canvas's api tokens to access user grades. Users have the option to choose a specific class (with a class id) to view, or just view all class grades.

![Demo](assets/demo.gif)

## Setup Instructions


In the project directory, create a '.env' file that contains a specification for your
CANVAS_API_TOKEN, see '.env.example' for formatting.

In a bash terminal, navigate to directory.


Set up the python environment:

`python -m venv venv`

Then either
`.\venv\Scripts\activate` (windows) or
`source venv/bin/activate` (linux/mac)

Make sure that your venv is activated, (venv) should appear in terminal prompt.
If you are using vscode and (venv) doesn't appear, kill and restart the terminal. (I had issues with VSCode needing to change the Python Interpreter in the IDE itself.)

Install necessary python libraries:

`pip install requests python-dotenv`

Then, to run program, use:

`python script.py`

## Example Uses

Using `python script.py` to run the program, when prompted to enter a class id, simply press enter to continue without entering a specific class, the program will then display all classes that the program is able to pull using API calls that have current grades that can be displayed, along with score percentage and class id. If bad input is provided for class id, program will automatically assume user is trying to display all classes.

Using `python script.py` to run the program, enter in a specific class id number and the program will show you the specific class with grade information if the class/info is able to be found.

## API Endpoints Used

This program uses two different Canvas api endpoints.

`/api/v1/courses`- Gets all courses from the user token, gets the id and name of each course.

`/api/v1/courses/:id/enrollments` - Gets the enrollments in a specific course, specified by an id that the first api endpoint got. Goes through the enrollments until it finds an object that contains a valid current_grade and current_score in the grade object gotten from each enrollment.

## Reflection



