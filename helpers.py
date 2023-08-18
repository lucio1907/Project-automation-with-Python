from colorama import Fore
from serverNodeTS import get_server_file_structure

def folder_name_input(project: str):
    folder_name = str(input(f'{Fore.GREEN}({project}){Fore.RESET} Please, give me the folder name: ')).capitalize()
    return folder_name

def create_folder_and_files(folder: str, app_file: str, files_paths: list):
    with open(app_file, 'w') as file:
        content_file = get_server_file_structure()
        file.write(content_file)

    #* Escribir archivos de .gitignore y .env
    gitignore = f'{folder}\.gitignore'
    for file_path in files_paths:
        with open(file_path, 'w') as file:
            if file_path == gitignore:
                file.write('/node_modules \n.env')
            else:
                file.write('PORT=8080')