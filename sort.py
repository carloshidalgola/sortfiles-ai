import os
import json
import shutil
import dotenv
import configs
from openai import OpenAI
import configs.config

dotenv.load_dotenv()

# Variables globales
directory_path = None
backup = False
summary = None
prompt_system = configs.config.PROMPT_SYSTEM

def set_directory_path():
    global directory_path
    directory_path = input("Please enter the path of the folder you want to organize: ")
    if not os.path.exists(directory_path):
        print("The path does not exist.")
        directory_path = None
    else:
        print(f"Path set to: {directory_path}")

def validate_backup():
    global backup
    respuesta = input("Would you like to back up your files? (Y/N): ").strip().upper()
    if respuesta == "Y":
        backup = True
        print("Backup option selected: Yes")
    elif respuesta == "N" or respuesta == "":
        backup = False
        print("Backup option selected: No")
    else:
        print("Invalid input. Backup will not be performed.")
        backup = False

def get_all_file_names_in_directory():
    print("Getting all file names in the directory...")
    try:
        file_names = [file for root, _, files in os.walk(directory_path) if "__backup" not in root for file in files]
        print(f"Found {len(file_names)} files.")
        return file_names
    except Exception as e:
        print(f"Error getting file names: {e}")
        return []

def create_directories_and_copy_files(structure):
    print("Creating directories and copying files...")
    try:
        for item in structure:
            folder_path = os.path.join(directory_path, item['Folder'])
            os.makedirs(folder_path, exist_ok=True)
            for file_name in item['Content']:
                src_file_path = os.path.join(directory_path, file_name)
                if os.path.exists(src_file_path):
                    shutil.move(src_file_path, folder_path)
                    print(f"Moved file {file_name} to {folder_path}")
                else:
                    print(f"File not found: {src_file_path}")
    except Exception as e:
        print(f"Error creating directories or copying files: {e}")

def backup_files():
    print("Backing up files...")
    backup_path = os.path.join(directory_path, "_backup")
    os.makedirs(backup_path, exist_ok=True)
    try:
        for root, _, files in os.walk(directory_path):
            if "_backup" in root:
                continue
            for file in files:
                src_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(src_file_path, directory_path)
                backup_file_path = os.path.join(backup_path, relative_path)
                backup_dir = os.path.dirname(backup_file_path)
                os.makedirs(backup_dir, exist_ok=True)
                shutil.copy(src_file_path, backup_file_path)
                print(f"Backed up file {file} to {backup_file_path}")
    except Exception as e:
        print(f"Error creating file backup: {e}")

def main():
    set_directory_path()
    if not directory_path:
        return
    
    all_file_names = get_all_file_names_in_directory()
    
    if not all_file_names:
        print("No files found in the specified directory.")
        return

    validate_backup()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
   
    print("Communicating with OpenAI API...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt_system},
                {"role": "user", "content": str(all_file_names)}
            ],
            temperature=0.3,
            top_p=1,
            frequency_penalty=0.1,
            presence_penalty=0.1
        )
    except Exception as e:
        print(f"Error communicating with the OpenAI API: {e}")
        return

    try:
        result = response.choices[0].message.content
        print("Received response from OpenAI API.")
        folder_structure = json.loads(result)
    except Exception as e:
        print(f"Error processing the API response: {e}")
        return

    create_directories_and_copy_files(folder_structure)
    if backup:
        backup_files()

    print("Files sorted correctly!!!")

if __name__ == "__main__":
    main()