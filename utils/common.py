# common python utilities

def said_yes( question: str ) -> bool:
    
    while True:
        response = input(f"> {question}? (yes/no): ")
        if response == "y" or response == "yes":
            return True
        elif response == "n" or response == "no":
            return False
        else:
            print("Incorrect response, please enter 'yes/y' or 'no/n'")

def menu_maker(menu_title: str, menu_desc: str):
    max_menu_len = 50
    menu_title_len = len(menu_title)
    menu_desc_len = len(menu_desc)
    menu_desc_rows = []
    menu_desc_list = menu_desc.split()
    buffer_char = "="

    # If the length of the provided title is < the default max, 
    # but is odd will append a space to make the buffers even on either side
    # If the provided title is greater than default max will set the default max to that length
    if menu_title_len < max_menu_len and menu_title_len % 2 != 0:
        menu_title = menu_title + " "
        menu_title_len = len(menu_title)
    elif menu_title_len > max_menu_len:
        max_menu_len = menu_title_len

    title_buffer_len =  (max_menu_len - menu_title_len) / 2
    title_buffer = buffer_char * int(title_buffer_len)
    menu_title = title_buffer + menu_title + title_buffer

    # Will parse each word in the provided desc, and split it into a row thats < the current max length
    index = 0
    for word in menu_desc_list:
        if 0 <= index < len(menu_desc_rows):
            if len(menu_desc_rows[index]) < max_menu_len:
                if len(menu_desc_rows[index] + " " + word) <= max_menu_len:
                    menu_desc_rows[index] = menu_desc_rows[index] + " " + word
                else:
                    index += 1
                    menu_desc_rows.append(word)
            elif len(menu_desc_rows[index]) >= max_menu_len:
                index += 1
                menu_desc_rows.append(word)
        else:
            menu_desc_rows.append(word)

    # Will generate the bottom line of the title 
    menu_bottom_line = buffer_char * max_menu_len
    print (menu_title)
    for menu_desc_line in menu_desc_rows:
        print (menu_desc_line)
    print (menu_bottom_line)
            




