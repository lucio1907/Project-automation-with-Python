import os
from colorama import Fore
from time import sleep
# from serverNodeTS import get_server_file_structure
from helpers import folder_name_input, create_folder_and_files

TEXT = f"""
Create a new project instantly! 
I am a system that can create project structures for you in seconds.
For the moment I've knowledges in Node with Typescript, Python and React!

- Write {Fore.BLUE}"node ts"{Fore.RESET} or {Fore.BLUE}"nts"{Fore.RESET} to create node and typescript project structure
- Write {Fore.YELLOW}"node js"{Fore.RESET} or {Fore.YELLOW}"njs"{Fore.RESET} to create node project structure
"""

def createNodeStructureTS(folder):
    contents = ['controllers', 'models', 'middlewares', 'routes', 'interfaces', 'db']
    src_folder = f'{folder}\src'
    files_paths = [f'{folder}\.gitignore', f'{folder}\.env']

    os.mkdir(src_folder)
    
    for content in contents:
        os.mkdir(f'{src_folder}\{content}')
    
    #* Cambia de directorio para escribir el archivo app.ts
    os.chdir(src_folder)
    app_file = f'{src_folder}/app.ts'

    #* Crear carpetas y archivos
    create_folder_and_files(folder, app_file, files_paths)

    #* Cambia de directorio para correr comandos en la carpeta seleccionada
    os.chdir(folder)
    
    init_node_package_json = 'npm init -y'
    init_typescript = 'tsc --init'
    install_essential_dependencies = 'npm i express dotenv cors'
    install_dependencies_types = 'npm i @types/express @types/dotenv @types/cors -D'
    commands = [init_node_package_json, init_typescript, install_essential_dependencies, install_dependencies_types]
    
    for command in commands:
        os.system(command)
    
    #* Finaliza abriendo el vsc
    os.system('cls')
    print('Opening project in VSC...')
    sleep(2)
    os.system('code .')
    return

def createNodeStructureJS(folder):
    contents = ['controllers', 'models', 'middlewares', 'routes', 'db']
    src_folder = f'{folder}\src'
    files_paths = [f'{folder}\.gitignore', f'{folder}\.env']

    os.mkdir(src_folder)

    for content in contents:
        os.mkdir(f'{src_folder}\{content}')

    os.chdir(src_folder)
    app_file = f'{src_folder}/app.js'

    #* Crear carpetas y archivos
    create_folder_and_files(folder, app_file, files_paths)

    #* Cambia de directorio para correr comandos en la carpeta seleccionada
    os.chdir(folder)

    init_package_json = 'npm init -y'
    install_essential_dependencies = 'npm i express cors dotenv'
    commands = [init_package_json, install_essential_dependencies]

    for command in commands:
        os.system(command)

    #* Finaliza abriendo el vsc
    os.system('cls')
    print('Opening project in VSC...')
    sleep(2)
    os.system('code .')
    return
    

def createNewProject(folder_name: str, is_typescript: bool):
    desktop = os.path.abspath('E:\Projects')

    try:
        folder = f'{desktop}\{folder_name}'
        os.mkdir(folder)
        print('Creating the whole structure...')
        sleep(2)
        if is_typescript:
            createNodeStructureTS(folder)
        else:
            createNodeStructureJS(folder)
        os.system('cls')
        print(f'Project: {folder_name} \nStatus: {Fore.GREEN}Created successfully in path "{folder}".{Fore.RESET}')    
    except FileExistsError:
        print(f'Project: {folder_name} \nStatus: {Fore.RED}"{desktop}\{folder_name}" already exists in path "{desktop}".{Fore.RESET}')
        print('\nReloading program...')
        sleep(3)
        os.system('cls')
        print(TEXT)
        configure_project()
        return

def configure_project():
    while True:
        user_selection = str(input('What kind of project would you like to do?: ')).lower()

        if 'node ts' in user_selection or 'nts' in user_selection: 
            os.system('cls')
            user_folder = folder_name_input('Node TS')
            createNewProject(user_folder, True)
            break
        else:
            os.system('cls')
            print("Sorry, I don't have the knowledge to create that.")

        if 'node js' in user_selection or 'njs' in user_selection:
            os.system('cls')
            user_folder = folder_name_input('Node JS')
            createNewProject(user_folder, False)
            break

def main():
    os.system('cls')
    print(TEXT)
    configure_project()


if __name__ == '__main__':
    main()