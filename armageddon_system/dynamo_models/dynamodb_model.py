from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class dynamo(Model):
    class Meta:
        aws_access_key_id = 'AKIA2SY5EY222UH55GWG'
        aws_secret_access_key = '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'
        table_name = "armageddon_db"
        region = 'ap-northeast-1' #東京リージョン

    AppName = UnicodeAttribute(hash_key=True)
    AppNo = UnicodeAttribute(range_key=True)
    Forms = UnicodeAttribute(null=True)
    Linebot = UnicodeAttribute(null=True)
    PayOffLogs = UnicodeAttribute(null=True)



