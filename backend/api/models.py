from django.db import models

class Item(models.Model):
    first_name = models.CharField(max_length=100, default='Leonard')
    middle_name = models.CharField(max_length=100, default='Delante')
    last_name = models.CharField(max_length=100, default='Ducusin')
    date_of_birth = models.DateField(default='2002-04-11')
    place_of_birth = models.CharField(max_length=100, default='Quezon City')
    sex = models.CharField(max_length=10, default='Male')
    civil_status = models.CharField(max_length=20, default='Single')
    height = models.FloatField(default=1.70)
    weight = models.FloatField(default=70.0)
    blood_type = models.CharField(max_length=3, default='O')
    gsis_id_no = models.CharField(max_length=20, default='0000000000')
    pagibig_id_no = models.CharField(max_length=20, default='0000000000')
    philhealth_no = models.CharField(max_length=20, default='0000000000')
    sss_no = models.CharField(max_length=20, default='0000000000')
    tin_no = models.CharField(max_length=20, default='0000000000')
    agency_employee_no = models.CharField(max_length=20, default='0000000000')
    citizenship = models.CharField(max_length=50, default='Filipino')
    residential_address = models.CharField(max_length=255, default='40 Corumi St, QC')
    zip_code = models.CharField(max_length=10, default='1115')
    permanent_address = models.CharField(max_length=255, default='40 Corumi St')
    telephone_no = models.CharField(max_length=20, default='0000000')
    mobile_no = models.CharField(max_length=20, default='09000000000')
    email_address = models.EmailField(default='example@example.com')
    fathers_name = models.CharField(max_length=100, default='Unknown Father')
    mothers_name = models.CharField(max_length=100, default='Unknown Mother')

    def str(self) -> str:
        return f"{self.first_name} {self.middle_name} {self.last_name}"