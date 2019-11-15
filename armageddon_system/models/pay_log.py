from armageddon_system.models.form import Form
from armageddon_system.models.dynamo_manager import DynamoManager as db

class PayLog:
    time_stamp = ""
    isStudent = True
    student_id = 0
    school_id = 0
    school_name = ""
    course_id = 0
    course_name = ""
    buyer_name = ""
    buyer_birth = ""
    form_list: list
    total = 0

    def __init__(self, time_stamp, student_id,
                 school_id, school_name, course_id,
                 course_name, form_list):
    def __init__(self,
                 time_stamp,
                 form_list,
                 isStudent=True,
                 student_id=None,
                 school_id=None,
                 school_name=None,
                 course_id=None,
                 course_name=None,
                 buyer_name=None,
                 buyer_birth=None
                 ):
        self.time_stamp = time_stamp
        if isStudent:
            self.student_id = student_id
            self.school_id = school_id
            self.school_name = school_name
            self.course_id = course_id
            self.course_name = course_name
        else:
            self.buyer_name = buyer_name
            self.buyer_birth = buyer_birth

        self.form_list = []
        dbm = db()
        all_form = dbm.get_form_all()
        for l in form_list:
            f = l['form']
            form = Form(
                form_id=f.form_id,
                form_name=f.form_name,
                fee=f.fee,
                issuance_days=None,
                qr=None
            )
            self.form_list.append(
                {'form': all_form[l['form_id']], 'quantity': l['quantity']}
            )

            self.total += form.fee * l['quantity']
