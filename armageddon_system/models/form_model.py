from datetime import datetime
from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute, MapAttribute
from pynamodb.models import Model
import armageddon_system.env as env


class Form(MapAttribute):
    FormName = UnicodeAttribute(null=False)
    Fee = UnicodeAttribute(null=False)
    IssuanceDays = NumberAttribute(null=False)
    QR = UnicodeAttribute(null=True)


class Forms(Model):
    class Meta:
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        table_name = env.AWS_TABLE_NAME
        region = env.AWS_REGION
        write_capacity_units = 1
        read_capacity_units = 1

    FormId = UnicodeAttribute(hash_key=True, null=False),
    Form = Form()