import json
def json2ini():
    data = json.load(open("config.json"))

    data.keys()
    data.items()
    ouput = ""

    for clé in data.keys():
        ouput += "[" + clé + "]\n"
        for item in data[clé].keys():
            ouput += item + " = " + data[clé][item] + "\n"
        ouput += "\n"
    with open('output.ini', 'w') as file:
        file.write(ouput)

if __name__ == '__main__':
    json2ini()