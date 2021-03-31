class Config(object):
    LOGGER = True
    TOKEN = "1457068950:AAFunUFSFW2IBT9rgjbvqyL3lvB1cbnzSis"
    MONGO_URI = "mongodb+srv://username:<password>@cluster0.c11xf.mongodb.net/<dbname>?retryWrites=true&w=majority"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
