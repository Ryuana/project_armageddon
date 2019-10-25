from . import model as db
import datetime


class DynamoManager():
    def get_pay_log_all(self):
        """
        精算記録を全件取得します。
        :rtype: list of map
        """

        PayOffLog = db.PayOffLogsModel.scan()
        return PayOffLog

    def save_pay_log(self, pay_log):
        """
        精算記録を保存します。
        :param pay_log: map
        :rtype: void
        """
        pom = db.PayOffLogsModel
        pay_off_log = pom(pom.count() + 1)
        pay_off_log.IsPaid = False
        pay_off_log.PayOffLog = {
            'Timestamp': datetime.datetime.now(),
            'Total': 999999,
            'Buyer': {
                'BuyerNo': 999999,
                'BuyerName': 'test',
                'BirthDay': datetime.datetime.now(),
                'SchoolId': 999999,
                'SchoolName': 'test',
                'CourseId': 999999,
                'CourseName': 'test'
            },
            'PayItems': [{
                'PayItemNo': 99999,
                'Form': {
                    'FormName': 'test',
                    'Fee': 99999,
                    'IssuanceDays': 65535,
                    'QR': 'this is QR code.'
                },
                'Quantity': 999
            }],
        }
        pay_off_log.save()

    def del_pay_log(self, pay_log_id):
        """
        指定したIDの精算記録を削除します。
        :param pay_log_id: int
        :return: void
        """

    def get_pay_item_all(self, pay_items):
        """
        精算項目を全件取得します。
        :param pay_items: list of map
        :rtype: void
        """

    def save_pay_item(self, pay_item):
        """
        精算項目を保存します。
        :param pay_item: map
        :rtype: void
        """

    def del_pay_item(self, form_id):
        """
        指定したIDの精算項目を削除します。
        :param form_id:　int
        :rtype: void
        """

    def get_qa_all(self):
        """
        QAを全件取得します。
        :rtype: list of map
        """

    def save_qa(self, qa):
        """
        QAを保存します。
        :param qa:list of map
        :rtype: void
        """

    def del_qa(self, qa_id):
        """
        指定したIDのQAを削除します。
        :param qa_id: int
        :rtype: void
        """

    def get_message_list(self):
        """
        LINE Botのメッセージを全件取得します。
        :rtype: list of map
        """

    def save_message_list(self, bot_message):
        """
        LINE Botのメッセージを保存します。
        :param bot_message: map
        :rtype: void
        """

    def del_message_list(self, bot_message_id):
        """
        指定したIDのLINE Bot メッセージを削除します。
        :param bot_message_id: int
        :rtype: void
        """

    def save_session_log(self, user_id):
        """
        セッションログを保存します。
        :param user_id: int
        :rtype: void
        """

    def check_login_id(self, user_id, user_pass):
        """
        ユーザIDとパスワードからログイン可否します。
        :param user_id: str
        :param user_pass: str
        :rtype: bool
        """
