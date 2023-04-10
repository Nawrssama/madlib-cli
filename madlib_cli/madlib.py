import re


def read_template(path):
    if path != "/home/nawrs/python-labs/madlib-cli/assets/great_copy.txt" :
        if path != "/home/nawrs/python-labs/madlib-cli/assets/great_and_amazing_game.txt" :
            raise FileNotFoundError ("path does not exsist")
    
    with open(path) as sekiro:
        open_sekiro = sekiro.read()
        return (open_sekiro.strip())
    


def parse_template(str):
    result = re.findall(r'\{([^{}]+)\}',str)
    print(result)
    x = ()
    for item in result:
        y = list(x)
        y.append(item)
        x = tuple(y)
        str = re.sub(r'\{([^{}]+)\}', '{}' ,str)
    print(str,x)
    return str,x


def merge(str, tuple):
    y = list(tuple)
    txt = str.format(*y)
    return txt



if __name__ == "__main__":
    print('''
******** Welcome to the madlib game ********
***** in this game you can play by entering what you are asked ;) *****
''')
    
    template = read_template("/home/nawrs/python-labs/madlib-cli/assets/great_copy.txt")
    stripped_template, parts = parse_template(template)

    what_user_input = []
    for part in parts:
        what_user_input.append(input(f"Enter a {part}: "))
    x = ()
    for item in what_user_input:    
        y = list(x)
        y.append( item)
        x = tuple(y)
    text = merge(stripped_template, x)
    print(text)
    with open("/home/nawrs/python-labs/madlib-cli/assets/file_to_write_on_it.txt", "w") as new:
        opened_new =new.write(text)



