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
    IsPaid = BooleanAttribute(null=False)

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))


class QuestionAndAnswersModel(Model):
    class Meta:
        table_name = "QuestionAndAnswers"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    QuestionAndAnswerId = NumberAttribute(hash_key=True)
    QuestionAndAnswer = attributes.QuestionAndAnswerAttribute(null=False)

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))


class MessagesModel(Model):
    class Meta:
        table_name = "Messages"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    MessageId = NumberAttribute(hash_key=True)
    attributes.MessageAttribute(null=False)

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))


class AlermsModel(Model):
    class Meta:
        table_name = "Alerms"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    AlarmId = NumberAttribute(hash_key=True)
    LineUserId = NumberAttribute(null=False)
    AlermDateTime = UTCDateTimeAttribute(null=False)

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))


class SchoolsModel(Model):
    class Meta:
        table_name = "Schools"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    SchoolId = NumberAttribute(hash_key=True)
    SchoolName = UnicodeAttribute(null=False)
    Courses = ListAttribute(of=attributes.CourseAttribute)


class UsersModel(Model):
    class Meta:
        table_name = "Schools"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    UserId = NumberAttribute(hash_key=True)
    Password = UnicodeAttribute(null=False)
    UserLogs = attributes.UserLogAttribute(null=True)

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))

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

if not FormsModel.exists():
    FormsModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
if not PayOffLogsModel.exists():
    PayOffLogsModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
if not QuestionAndAnswersModel.exists():
    QuestionAndAnswersModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
if not MessagesModel.exists():
    MessagesModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
if not AlermsModel.exists():
    AlermsModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
if not SchoolsModel.exists():
    SchoolsModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
if not UsersModel.exists():
    UsersModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
if not Transactions.exists():
    Transactions.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
