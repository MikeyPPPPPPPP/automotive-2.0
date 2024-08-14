config_file =   "config\\settings.conf"


def save_destination(destination) -> None:
    import configparser
    from utils.fileandfolder import make_config_folder
    make_config_folder()
    config = configparser.ConfigParser()
    config['Settings'] = {'Destination': destination}
    
    with open(config_file, 'w') as configfile:
        config.write(configfile)


def load_destination() -> str | None:
    import configparser
    from utils.fileandfolder import check_exits
    from utils.fileandfolder import make_config_folder
    make_config_folder()
    config = configparser.ConfigParser()
    if check_exits(config_file):
        config.read(config_file)
        return config.get('Settings', 'Destination', fallback=None)
    else:
        with open(config_file, 'w') as configfile:
            config['Settings'] = {'Destination': ''}
            config.write(configfile)
        return None
    

def reset_destination() -> None:
    import configparser
    from utils.fileandfolder import check_exits
    from utils.fileandfolder import make_config_folder
    make_config_folder()
    config = configparser.ConfigParser()
    if check_exits(config_file):
        with open(config_file, 'w') as configfile:
            config['Settings'] = {'Destination': ''}
            config.write(configfile)