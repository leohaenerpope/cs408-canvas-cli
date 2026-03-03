
In project directory, create a .env file that contains a specification for your
CANVAS_API_TOKEN, see .env.example for formatting.

In bash terminal, navigate to inside of folder cs408-canvas-cli that was imported from github
Set up the python environment

`python -m venv venv`

Then either
`.\venv\Scripts\activate` (windows) or
`source venv/bin/activate` (linux/mac)

Make sure that your venv is activated, (venv) should appear in terminal prompt.
If you are using vscode and (venv) doesn't appear, kill and restart the terminal.

install necessary python libraries
`pip install requests python-dotenv`

then, to run program, use
`python script.py`

turn this into a thing where user shows assignments from certain/all courses