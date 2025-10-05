# file-organizer
A simple Python tool for automatically organizing your files into folders based on their file types. Helps in 
keeping your downloads, documents, and media files neatly arranged with minimal effort.

## Features
- Automatically categorizes files into folders like, Images, Videos, Documents, Audio, and more.
- Custom categories; you can add your own file extentions.
- Logs all actions to *organizer_log.txt*.
- Keeps your directories clean.

## Setup and Usage
1. Make sure you have **Python 3+** installed.
2. Clone or download this repository.
3. Run the application: **file_organizer.py**.
4. When prompted, paste the directory path of the folder you want to organize.
5. Files will automatically move into their respective folders.

## Customization
- You can add your own categories or file extensions by editing the _file_types_ dictionary.
- [Where to add your custom categories and extension](https://github.com/Reinald-Claudio/file-organizer/blob/main/Screenshot%202025-09-10%20072323.png?raw=true)

## How It Works
- The program reads all files in the specified folder.
- Matches each file to a folder category based on its extension.
- Moves the file into the corresponding folder.
- Logs all changes in *organizer_log.txt*.



