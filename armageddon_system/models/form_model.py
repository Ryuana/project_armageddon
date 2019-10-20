from datetime import datetime
from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute, MapAttribute
from pynamodb.models import Model
import armageddon_system.env as env


class Form(MapAttribute):
    FormName = UnicodeAttribute(null=False)
    Fee = NumberAttribute(null=False)
    IssuanceDays = NumberAttribute(null=False)
    QR = UnicodeAttribute(null=False)


class FormsModel(Model):
    class Meta:
        table_name = "Forms"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION
        write_capacity_units = 1
        read_capacity_units = 1

    FormId = NumberAttribute(hash_key=True)
    Form = Form(null=False)


if not FormsModel.exists():
    FormsModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
