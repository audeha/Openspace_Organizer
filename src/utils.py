"""get each participan's name"""
def hello(name_path):
    names = []
    with open(name_path, "r") as ifile:
        for line in ifile:
            #line.strip removes the extra blank lines
            space_name = line.strip().replace(',', ' ')
            names.append(space_name)
    return names

#print(hello())
