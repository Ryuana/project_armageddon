import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute,NumberAttribute,UTCDateTimeAttribute
import armageddon_system.env as env
from pynamodb.models import Model

#PynamoDBに変更する必要あり

class Transactions(Model):

    class Meta:
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        table_name = "linepay_test"
        region = env.AWS_REGION

    #PynamoDBに変更する必要あり
    transaction_id = UnicodeAttribute(hash_key=True)
    order_id = UnicodeAttribute(null=True)
    product_name = UnicodeAttribute(null=True)
    amount = NumberAttribute(null=True)
    currency = UnicodeAttribute(null=True)
    register_date = UTCDateTimeAttribute(null=True)
    user_id = UnicodeAttribute(null=True)

    #自身のオブジェクトから値を取得する専用のメソッド定義するときに使う
    @property
    def serialize(self):
        return {
            'transaction_id': self.transaction_id,
            'order_id': self.order_id,
            'product_name': self.product_name,
            'amount': self.amount,
            'currency': self.currency,
            'register_date': self.register_date.strftime('%Y-%m-%d %H:%M:%S'),
            'user_id':self.user_id
        }