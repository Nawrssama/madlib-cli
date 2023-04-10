import re

def read_template(path):
    if path != "assets/sekiro_game.txt" :
        if path != "assets/great_and_amazing_game.txt" :
            raise FileNotFoundError ("path does not exsist")
    with open(path) as file:
        return file.read()

def parse_template(str):
    parts = re.findall(r'\{([^{}]+)\}', str)
    stripped_template = re.sub(r'\{([^{}]+)\}', '{}', str)
    stripped_parts = [part.strip() for part in parts]
    return stripped_template, tuple(stripped_parts)

def merge(stripped_template, user_inputs):
    return stripped_template.format(*user_inputs)

def play_game(template_path):
    template = read_template(template_path)
    stripped_template, parts = parse_template(template)

    user_inputs = []
    for part in parts:
        user_input = input(f"Enter a {part}: ")
        user_inputs.append(user_input)

    madlib = merge(stripped_template, user_inputs)
    print(madlib)

    with open("assets/complete_sekiro_game.txt", "w") as file:
        file.write(madlib)

if __name__ == "__main__":
    print('''
******** Welcome to the madlib game ********
***** in this game you can play by entering what you are asked ;) *****
''')

    template_path = "assets/sekiro_game.txt"
    play_game(template_path)
