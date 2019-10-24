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
