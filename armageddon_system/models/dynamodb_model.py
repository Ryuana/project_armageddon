from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute,NumberAttribute,ListAttribute,MapAttribute
import armageddon_system.env as env

class dynamo(Model):
    class Meta:
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        table_name = env.AWS_TABLE_NAME
        region = env.AWS_REGION

    AppName = UnicodeAttribute(hash_key=True)
    AppNo = NumberAttribute(range_key=True)
    Forms = ListAttribute(null=True)
    Linebot = MapAttribute(null=True)
    PayOffLogs = ListAttribute(null=True)
    testStr = UnicodeAttribute(null=True)



