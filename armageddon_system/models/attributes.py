from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute, MapAttribute, \
    ListAttribute


class FormAttribute(MapAttribute):
    FormName = UnicodeAttribute(null=False)
    Fee = NumberAttribute(null=False)
    IssuanceDays = NumberAttribute(null=False)
    QR = UnicodeAttribute(null=True)


class BuyerAttribute(MapAttribute):
    BuyerNo = NumberAttribute(null=True)
    BuyerName = UnicodeAttribute(null=True)
    BirthDay = UTCDateTimeAttribute(null=True)
    SchoolId = NumberAttribute(null=True)
    SchoolName = UnicodeAttribute(null=True)
    CourseId = NumberAttribute(null=True)
    CourseName = UnicodeAttribute(null=True)


class PayItemsAttribute(MapAttribute):
    PayItemNo = NumberAttribute(null=False)
    Form = FormAttribute(null=False)
    Quantity = NumberAttribute(null=False)


class PayOffLogAttribute(MapAttribute):
    Timestamp = UTCDateTimeAttribute(null=False)
    Total = NumberAttribute(null=False)
    Buyer = BuyerAttribute(null=False)
    PayItems = ListAttribute(of=PayItemsAttribute)
    Quantity = NumberAttribute(null=False)


class QuestionAndAnswerAttribute(MapAttribute):
    QuestionId = NumberAttribute(null=False)
    Questions = ListAttribute(null=True)
    Answer = UnicodeAttribute


class MessageAttribute(MapAttribute):
    MessageId = NumberAttribute(null=False)
    Message = UnicodeAttribute(null=False)
    Image = UnicodeAttribute(null=False)
    Timestamp = UTCDateTimeAttribute(null=True)


class AlermAttribute(MapAttribute):
    AlermId = NumberAttribute(null=False)
    UserId = UnicodeAttribute(null=False)
    AlermDatetime = UTCDateTimeAttribute(null=False)

class SchoolAttribute(MapAttribute):
    SchoolId = NumberAttribute(null=False)
    SchoolName = UnicodeAttribute(null=False)
    Courses = ListAttribute()
    #TODO:ここから