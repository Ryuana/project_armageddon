from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute, MapAttribute, \
    ListAttribute


class FormAttribute(MapAttribute):
    FormName = UnicodeAttribute(null=False)
    Fee = NumberAttribute(null=False)
    IssuanceDays = NumberAttribute(null=False)
    QR = UnicodeAttribute(null=True)


class PayItemsAttribute(MapAttribute):
    PayItemNo = NumberAttribute(null=False)
    Form = FormAttribute(null=False)
    Quantity = NumberAttribute(null=False)


class BuyerAttribute(MapAttribute):
    BuyerNo = NumberAttribute(null=True)
    BuyerName = UnicodeAttribute(null=True)
    BirthDay = UTCDateTimeAttribute(null=True)
    SchoolId = NumberAttribute(null=True)
    SchoolName = UnicodeAttribute(null=True)
    CourseId = NumberAttribute(null=True)
    CourseName = UnicodeAttribute(null=True)


class PayOffLogAttribute(MapAttribute):
    Timestamp = UTCDateTimeAttribute(null=False)
    Total = NumberAttribute(null=False)
    Buyer = BuyerAttribute(null=False)
    PayItems = ListAttribute(of=PayItemsAttribute)
    Quantity = NumberAttribute(null=False)


class QuestionAndAnswerAttribute(MapAttribute):
    Questions = ListAttribute(null=True)
    Answer = UnicodeAttribute(null=False)


class MessageAttribute(MapAttribute):
    MessageContent = UnicodeAttribute(null=False)
    ImagePath = UnicodeAttribute(null=False)
    Timestamp = UTCDateTimeAttribute(null=True)


class CourseAttribute(MapAttribute):
    CourseId = NumberAttribute(null=False)
    CourseName = UnicodeAttribute(null=False)


class UserLogAttribute(MapAttribute):
    LoginTime = UTCDateTimeAttribute(null=False)
    LogoutTime = UTCDateTimeAttribute(null=True)
