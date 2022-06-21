from configparser import ConfigParser


def config(fileName, section):
    # creation of a parser
    parser = ConfigParser()
    # read config parser
    parser.read(fileName)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        return db
    else:
        raise Exception("la section {} n'existe pas dans le fichier {}".format(section, fileName))

