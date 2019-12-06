import datetime


class Message:
    message_id = 0
    message = ""
    image: bytearray = ""
    time_stamp = ""

    def __init__(self, message_id, message, image):
        self.message_id = message_id
        self.message = message
        self.image = image
        self.time_stamp = datetime.date.today()
