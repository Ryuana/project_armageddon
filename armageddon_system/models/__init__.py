class DynamoClass:
    from .model import FormsModel, PayOffLogsModel, UsersModel, SchoolsModel, \
        MessagesModel, AlermsModel, QuestionAndAnswersModel, Transactions


class arrmagedon_models:
    from .pay_log import PayLog
    from .form import Form
    from .qa import QA
    from .message import Message


class DynamoManager:
    from .dynamo_manager import DynamoManager
