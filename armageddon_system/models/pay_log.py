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
            if 'form' in l:
                f = l['form']
                form = Form(
                    form_id=int(f.form_id),
                    form_name=f.form_name,
                    fee=f.fee,
                    issuance_days=None,
                    qr=None
                )
                self.form_list.append(
                    {'form': all_form[int(f.form_id)-1],
                     'quantity': l['quantity'],
                     'subtotal': l['subtotal']
                     }
                )

            else:
                form = Form(
                    form_id=int(l['form_id']),
                    form_name=l['form_name'],
                    fee=l['fee'],
                    issuance_days=None,
                    qr=None
                )
                self.form_list.append(
                    {'form': all_form[int(l['form_id'])-1], 'quantity': int(l['quantity']),
                     'subtotal': (int(l['fee']) * int(l['quantity']))}
                )

    def __iter__(self):
        yield 'time_stamp', self.time_stamp,
        yield 'form_list', self.form_list,
        yield 'isStudent', self.isStudent,
        yield 'student_id', self.student_id,
        yield 'school_id', self.school_id,
        yield 'school_name', self.school_name,
        yield 'course_id', self.course_id,
        yield 'course_name', self.course_name,
        yield 'buyer_name', self.buyer_name,
        yield 'buyer_birth', self.buyer_birth,
