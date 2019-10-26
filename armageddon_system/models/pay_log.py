from  armageddon_system.models.form import Form

class PayLog:

    time_stamp = ""
    student_id = 0
    school_id = 0
    school_name = ""
    course_id = 0
    course_name = ""
    form_list: list[dict]
    total = 0

    def __init(self, time_stamp, student_id, school_id, school_name, course_id, course_name, form_list):
        self.time_stamp = time_stamp
        self.student_id = student_id
        self.school_id = school_id
        self.school_name = school_name
        self.course_id = course_id
        self.course_name = course_name
        for l in form_list:
            self.form_list.append(
                dict({'form': Form(l.form_id, l.form_name, l.fee, l.issuance_days, l.qr), 'quantity': l.quantity})
            )
            self.total += l.fee * l.quantity


