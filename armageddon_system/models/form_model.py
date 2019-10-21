from datetime import datetime
from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute, MapAttribute, \
    ListAttribute
from pynamodb.models import Model
import armageddon_system.env as env


class FormAttribute(MapAttribute):
    FormName = UnicodeAttribute(null=True)
    Fee = NumberAttribute(null=True)
    IssuanceDays = NumberAttribute(null=True)
    QR = UnicodeAttribute(null=True)


class FormsModel(Model):
    class Meta:
        table_name = "Forms"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION
        write_capacity_units = 1
        read_capacity_units = 1

    FormId = UnicodeAttribute(hash_key=True)
    testClumn = UnicodeAttribute(null=True)
    Form = FormAttribute(null=True)
    listAttribute = ListAttribute(null=True)
    mapAttribute = MapAttribute(null=True)

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))



if not FormsModel.exists():
    FormsModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
