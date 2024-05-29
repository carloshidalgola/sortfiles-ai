# File Organizer

## Overview

The File Organizer is a Python script designed to help you organize files within a specified directory. It uses the OpenAI API to determine the optimal folder structure for your files and can optionally back up your files before organizing them.

## Features

- Organizes files into folders based on a structure determined by the OpenAI API.
- Optionally backs up files before organizing.
- Provides detailed logs to inform the user of the operations being performed.

## Requirements

- Python 3.x
- `openai` Python package
- `python-dotenv` Python package

## Setup

1. Clone the repository:
sh git clone https://github.com/yourusername/file-organizer.git cd file-organizer

2. Install the required packages:
sh pip install openai python-dotenv

3. Create a `.env` file in the root directory and add your OpenAI API key:
env OPENAI_API_KEY=your_openai_api_key

4. Create a `config.py` file in the `configs` directory and add the following content:
python # configs/config.py
```

PROMPT_SYSTEM = """You are an agent that organizes files. You will be sent a set of file names and you must organize them into folders and files up to 3 levels. I need you to structure the response like this example: [ {"Folder": "agile", "Content": ["agile-conversation.png", "agile-lcm-training.jpg", "agile-lcm.jpg", "agile-planning.jpg", "agile-training-lcm.jpg", "agile-training-m3.jpg"]}, {"Folder": "team", "Content": ["team-conversation.jpg"]}, {"Folder": "others", "Content": ["72129910_2713404035408494_1922342458776092672_n.jpg", "adkar-assessment.jpg", "CM_Icon_black.png"]} ] IMPORTANT: The response should only return an array in JSON format. Do not add any other response."""
```

## Usage

1. Run the script:
```
sh python main.py
```

2. Follow the prompts:
    - Enter the path of the folder you want to organize.
    - Choose whether to back up your files before organizing.

## Example
```
Please enter the path of the folder you want to organize: /path/to/your/folder
Would you like to back up your files? (Y/N): Y
```

## Logs

The script provides detailed logs to inform you of the operations being performed, including:

- Setting the directory path.
- Validating the backup option.
- Getting file names from the directory.
- Creating directories and copying files.
- Backing up files.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note:** Replace `yourusername` in the clone URL with your actual GitHub username and ensure the `LICENSE` file is included in your repository if you choose to use the MIT License.
