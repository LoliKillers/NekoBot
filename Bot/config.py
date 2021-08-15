class Config(object):
    LOGGER = True
    TOKEN = "1870815445:AAEODGdC2uvoxw0vue4sKBeVxH6ZTmACnDw"
    MONGO_URI = "mongodb+srv://username:<password>@cluster0.c11xf.mongodb.net/<dbname>?retryWrites=true&w=majority"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
