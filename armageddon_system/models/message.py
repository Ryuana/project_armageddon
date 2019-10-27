import datetime

class Message:

    message_id = 0
    message = ""
    image: bytearray = ""
    create_date = ""

    def __init__(self, message_id, message, image):
        self.message_id = message_id
        self.message = message
        self.image = image
        self.create_date = str(datetime.date.today()).replace("-", "")