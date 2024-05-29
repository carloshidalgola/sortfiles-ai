File Organizer
Overview
The File Organizer is a Python script designed to help you organize files in a specified directory. It uses the OpenAI API to intelligently categorize and move files into appropriate folders. Additionally, it offers an option to back up your files before organizing them.

Features
Organizes files into folders based on their names and content.
Option to back up files before organizing.
Logs progress and actions to keep the user informed.
Configurable via a separate configuration file.
Requirements
Python 3.6+
OpenAI API Key
dotenv library
openai library
Installation
Clone the repository:
Sh

Insert code
git clone https://github.com/yourusername/file-organizer.git
    cd file-organizer
Create and activate a virtual environment (optional but recommended):
Sh

Insert code
python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:
Sh

Insert code
pip install -r requirements.txt
Create a .env file in the root directory and add your OpenAI API key:
Env

Insert code
OPENAI_API_KEY=your_openai_api_key
Configuration
The script uses a configuration file (config.py) to store constants. The default configuration file looks like this:

Python

Insert code
# config.py
PROMPT_SYSTEM = """You are an agent that organizes files. You will be sent a set of file names and you must organize them into folders and files up to 3 levels. I need you to structure the response like this example:
[
    {"Folder": "agile", "Content": ["agile-conversation.png", "agile-lcm-training.jpg", "agile-lcm.jpg", "agile-planning.jpg", "agile-training-lcm.jpg", "agile-training-m3.jpg"]},
    {"Folder": "team", "Content": ["team-conversation.jpg"]},
    {"Folder": "others", "Content": ["72129910_2713404035408494_1922342458776092672_n.jpg", "adkar-assessment.jpg", "CM_Icon_black.png"]}
]

IMPORTANT: The response should only return an array in JSON format. Do not add any other response."""
Usage
Run the script:
Sh

Insert code
python main.py
Follow the prompts:

Enter the path of the folder you want to organize.
Choose whether to back up your files before organizing.
The script will communicate with the OpenAI API to get the folder structure and organize your files accordingly.

Example
Sh

Insert code
Please enter the path of the folder you want to organize: /path/to/your/folder
Would you like to back up your files? (Y/N): Y
Getting all file names in the directory...
Found 10 files.
Communicating with OpenAI API...
Received response from OpenAI API.
Creating directories and copying files...
Moved file example1.txt to /path/to/your/folder/agile
Moved file example2.jpg to /path/to/your/folder/team
Backing up files...
Backed up file example1.txt to /path/to/your/folder/_backup/example1.txt
Backed up file example2.jpg to /path/to/your/folder/_backup/example2.jpg
Files sorted correctly!!!
