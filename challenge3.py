def assemble_guest_list():
    """This function repeatedly prompts the user for the name of a dinner guest.
    Each string the user supplies is added to a list. If/when the user hits 
    "Enter" without typing anything, the function stops asking and 
    returns the list.
    
    Arguments: None!
    
    Returns:
        - a list of strings supplied by the user
    """
    guest_list = []
    guest_name = input("Please enter guest name: ")

    while guest_name != "":
        guest_list.append(guest_name)
        guest_name = input("Please enter a guest name: ")

    return guest_list
assemble_guest_list()
    