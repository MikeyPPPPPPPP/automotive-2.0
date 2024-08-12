def argsparser():
    import argparse

    parser = argparse.ArgumentParser(description='Manage movie folder location.')
    
    # Define command-line arguments
    parser.add_argument('-r', '--reset', action='store_true', 
                        help='Reset movie\'s folder location')
    parser.add_argument('-d', '--destination', type=str,
                        help='Specify the movie\'s folder location')
    
    args = parser.parse_args()
    
    if args.reset:
        from utils.configuring import reset_destination, load_destination
        dest = load_destination()
        reset_destination()
        if dest == None or dest == '':
            print(f"Destination was not set. ", end="", flush=True)
            from utils.timings import take_rest
            take_rest()
            print(f"(if you where wondering)")
        else:
            print(f"The destination of \"{dest}\" will no longer be used.")
        exit()
    elif args.destination:
        from utils.configuring import save_destination
        save_destination(args.destination)