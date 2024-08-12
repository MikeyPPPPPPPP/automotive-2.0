def move_file(source_file: str, destination_file: str) -> None:
    try:
        from shutil import move
        move(source_file, destination_file)
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except PermissionError as e:
        print(f'Permission error: {e}')
    except Exception as e:
        print(f'Error: {e}')


def move_folder(source_folder: str, destination_folder: str) -> None:
    try:
        from shutil import move
        move(source_folder, destination_folder)
    except FileNotFoundError as e:
        print(f'Folder not found: {e}')
    except PermissionError as e:
        print(f'Permission error: {e}')
    except Exception as e:
        print(f'Error: {e}')


def remove_file(file: str) -> None:
    from os import remove
    try:
        remove(file)
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except PermissionError as e:
        print(f'Permission error: {e}')
    except Exception as e:
        print(f'Error: {e}')


def remove_folder(folder: str):
    try:
        from shutil import rmtree
        rmtree(folder)
    except FileNotFoundError as e:
        print(f'Folder not found: {e}')
    except PermissionError as e:
        print(f'Permission error: {e}')
    except Exception as e:
        print(f'Error: {e}')


def check_exits(fileorfolder: str) -> bool:
    from os.path import exists
    if exists(fileorfolder):
        return True
    else:
        return False
    

def make_directory(destination_folder: str) -> None:
    if not check_exits(destination_folder):
        from os import makedirs
        makedirs(destination_folder)


def make_backup_folder() -> str:
    movies_folder = "movies"
    if not check_exits(movies_folder):
        make_directory(movies_folder)
    return movies_folder


def validate_folder_path(path: str, must_exist: bool = True) -> bool:
    if not isinstance(path, str):
        return False

    # Check if the path is a valid path
    if not path:
        return False
    
    # Check if the path exists if required
    if must_exist:
        from os.path import isdir
        return isdir(path)
    
    return True


def make_config_folder() -> None:
    config_folder = "config"
    if not check_exits(config_folder):
        make_directory(config_folder)


def make_utils_folder() -> None:
    utils_folder = "utils"
    if not check_exits(utils_folder):
        make_directory(utils_folder)