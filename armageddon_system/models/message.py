class Message:

    message_id = 0
    message = ""
    image: bytearray = ""
    create_date = ""

    def __init__(self, message_id, message, image, create_date):
        self.message_id = message_id
        self.message = message
        self.image = image
        self.create_date = create_date
