import re

def read_template(path):

    """
    Reads a file from the specified path and returns its contents as a string.

    Parameters:
    - path (str): The path to the file to be read.

    Raises:
    - FileNotFoundError: If the specified path does not exist or is not a valid file.

    Returns:
    - str: The contents of the file as a string.
    """

    if path != "assets/text_befor.txt" :
        if path != "assets/dark_and_stormy_night_template.txt" :
            raise FileNotFoundError ("path does not exsist")
    with open(path) as file:
        return file.read()

def parse_template(str):

    """
    Parses a template string and returns a tuple containing the stripped template and its variable parts.

    Parameters:
    - string (str): The template string to be parsed.

    Returns:
    - tuple (str, tuple): A tuple containing the stripped template and its variable parts.
        - The stripped template (str) is the original template string with its variable parts replaced by '{}' placeholders.
        - The variable parts (tuple) is a tuple of strings representing the variable parts of the original template string, in the order they appear.
    """
        
    parts = re.findall(r'\{([^{}]+)\}', str)
    stripped_template = re.sub(r'\{([^{}]+)\}', '{}', str)
    stripped_parts = [part.strip() for part in parts]
    return stripped_template, tuple(stripped_parts)

def merge(stripped_template, user_inputs):

    """
    Merges user inputs with a stripped template string and returns the merged string.

    Parameters:
    - stripped_template (str): The stripped template string to merge user inputs with.
    - user_inputs (tuple): A tuple of strings representing the user inputs to be merged with the stripped template string.

    Returns:
    - str: The merged string, with the user inputs inserted into the stripped template string using the '{}' placeholders.
    """

    return stripped_template.format(*user_inputs)

def play_game(template_path):

    """
    Plays a madlibs game using the specified template file.

    Parameters:
    - template_path (str): The path to the template file to use for the madlibs game.

    Returns:
    - None

    Side Effects:
    - Prompts the user to enter values for the variable parts in the template.
    - Prints the resulting madlibs story to the console.
    - Writes the resulting madlibs story to a file named "assets/text_after.txt".
    """

    template = read_template(template_path)
    stripped_template, parts = parse_template(template)

    user_inputs = []
    for part in parts:
        user_input = input(f"Enter a {part}: ")
        user_inputs.append(user_input)

    madlib = merge(stripped_template, user_inputs)
    print(madlib)

    with open("assets/text_after.txt", "w") as file:
        file.write(madlib)

if __name__ == "__main__":
    # This block of code is executed when the Python script is run as the main program.
    # It welcomes the user to the madlib game and calls the play_game function with the template path set to "assets/text_befor.txt".
    print('''
******** Welcome to the madlib game ********
***** in this game you can play by entering what you are asked ;) *****
''')

    template_path = "assets/text_befor.txt"
    play_game(template_path)
