from datetime import datetime
from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute, MapAttribute, \
    ListAttribute
from pynamodb.models import Model
import armageddon_system.env as env

from armageddon_system.models import attributes


class FormsModel(Model):
    class Meta:
        table_name = "Forms"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    FormId = NumberAttribute(hash_key=True)
    Form = attributes.FormAttribute(null=True)

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))


class PayOffLogsModel(Model):
    class Meta:
        table_name = "PayOffLogs"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    LogId = NumberAttribute(hash_key=True)
    PayOffLog = attributes.PayOffLogAttribute(null=False)

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))


class LineBotModel(Model):
    class Meta:
        table_name = "LineBot"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    QuestionAndAnswers = ListAttribute(of=attributes.QuestionAndAnswerAttribute)
    Messages = ListAttribute(of=attributes.MessageAttribute)
    Alerms = ListAttribute(of=attributes.AlermAttribute)

class SchoolsModel(Model):
    class Meta:
        table_name = "Schools"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    # Schools =

if not FormsModel.exists():
    FormsModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
if not PayOffLogsModel.exists():
    PayOffLogsModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
