from . import model as db
import datetime
import json
from armageddon_system.models.form import Form
from armageddon_system.models.pay_log import PayLog


class DynamoManager():
    def get_pay_log_count(self):
        count = 0
        PayOffLog = db.PayOffLogsModel().scan()

        for item in PayOffLog:
            count += 1
        return count

    def get_pay_log_all(self):
        """
        精算記録を全件取得します。
        :rtype: list of map
        """
        form_list = [
            {
                'form':
                {
                    'form_id': '1',
                    'form_name': "AA",
                    'fee': 100,
                    'issuance_days': 3,
                    'qr': 'dog'
                },
                'quantity': 3
            },
            {
                'form':
                    {
                        'form_id': '2',
                        'form_name': "BB",
                        'fee': 200,
                        'issuance_days': 2,
                        'qr': 'cat'
                    },
                'quantity': 2
            }
        ]

        pay_logs = PayLog("20191029", 1801179, 1233, "AB", 2, "Jo", form_list)
        #all_pay_off_log = db.PayOffLogsModel.scan()
        return pay_logs

    def save_pay_log(self, id, pay_log):
        """
        精算記録を保存します。
        :param pay_log: map
        :rtype: void
        """
        log = db.PayOffLogsModel(id)
        log.IsPaid = False
        log.PayOffLog = {
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
        log.save()

    def del_pay_log(self, pay_log_id):
        """
        指定したIDの精算記録を削除します。
        :param pay_log_id: int
        :return: void
        """
        pay_log = db.PayOffLogsModel.get(hash_key=pay_log_id)
        pay_log.delete()

    def get_form_all(is_ascending=False):
        """
        精算項目を全件取得します。(通常はidで降順)
        is_ascending=Trueの場合昇順
        :rtype: all_form: list of map
        """
        all_form = db.FormsModel.scan()
        # pay_itemsの
        return_items = []
        for item in all_form:
            form = Form(
                form_id=item.FormId,
                form_name=item.FormName,
                fee=item.Fee,
                issuance_days=item.IssuanceDays,
                qr=item.QR
            )
            return_items.append(form)
        if is_ascending:
            return_items = reversed(return_items)
        return return_items

    def save_form(self, form: Form):
        """
        精算項目を保存します。
        :param pay_item: map
        :rtype: void
        """
        new_form = db.FormsModel(int(form.form_id))
        # Formsの項目に埋め込む処理
        new_form.FormName = form.form_name
        new_form.Fee = int(form.fee)
        new_form.IssuanceDays = int(form.issuance_days)
        new_form.QR = form.qr

        new_form.save()

    def del_form(self, form_id):
        """
        指定したIDの精算項目を削除します。
        :param form_id:　int
        :rtype: void
        """
        fm = db.FormsModel
        form_item = fm.get(hash_key=form_id)
        form_item.delete()

    def get_qa_all(self):
        """
        QAを全件取得します。
        :rtype: list of map
        """
        all_qa = db.QuestionAndAnswersModel.scan()
        # QAに埋め込む処理
        return all_qa

    def save_qa(self, qa):
        """
        QAを保存します。
        :param qa:list of map
        :rtype: void
        """
        qa = db.QuestionAndAnswersModel()
        # QAに情報を埋め込む
        qa.save()

    def del_qa(self, qa_id):
        """
        指定したIDのQAを削除します。
        :param qa_id: int
        :rtype: void
        """
        qa = db.QuestionAndAnswersModel.get(qa_id)
        qa.delete()

    def get_message_list(self):
        """
        LINE Botのメッセージを全件取得します。
        :rtype: list of map
        """
        message_list = db.MessagesModel.scan()
        # messageを埋め込む処理
        return message_list

    def save_message_list(self, bot_message):
        """
        LINE Botのメッセージを保存します。
        :param bot_message: map
        :rtype: void
        """
        message = db.MessagesModel()
        #     埋め込む処理
        message.save()

    def del_message_list(self, bot_message_id):
        """
        指定したIDのLINE Bot メッセージを削除します。
        :param bot_message_id: int
        :rtype: void
        """
        message = db.MessagesModel(bot_message_id)
        message.delete()

    def save_session_log(self, user_id):
        """
        セッションログを保存します。
        :param user_id: int
        :rtype: void
        """
        session_log = db.MessagesModel()
        # 情報を埋め込む
        session_log.save()

    def check_login_id(self, user_id, user_pass):
        """
        ユーザIDとパスワードからログイン可否します。
        :param user_id: str
        :param user_pass: str
        :rtype: bool
        """
        session_log = db.MessagesModel()
        # 情報を埋め込む
        session_log.save()
