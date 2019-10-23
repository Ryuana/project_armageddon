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



class PayOffLogAttribute(MapAttribute):
    TimeStamp = UTCDateTimeAttribute(null=False)
    Total = NumberAttribute(null=False)
    Buyer = BuyerAttribute(null=False)
    # TODO:ここから
    # Form = FormAttribute(null=False)



