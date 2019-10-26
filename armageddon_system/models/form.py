class Form:

    form_id = 0
    form_name = ""
    fee = 0
    issuance_days = ""
    qr = ""

    def __init__(self, form_id, form_name, fee, issuance_days, qr):
        self.form_id = form_id
        self.form_name = form_name
        self.fee = fee
        self.issuance_days = issuance_days
        self.qr = qr
