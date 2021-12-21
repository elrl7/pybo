from django.db import models

# Create your models here.
class company(models.Model):
    cno = models.IntegerField(
        primary_key=True, auto_created=True)         # 회사번호
    company_name = models.CharField(
        max_length=100)                              # 회사명
    company_bisnum = models.IntegerField(
        null=True)                                   # 사업자번호
    expiration_date = models.DateTimeField()         # 만료일
    company_status = models.CharField(max_length=1)
    company_address = models.CharField(
        max_length=255)                              # 사업장주소
    company_telno = models.CharField(
        max_length=50)                               # 전화번호
    company_email = models.EmailField()              # 이메일
    company_note = models.TextField(max_length=255, null=True)     # 비고
    create_date = models.DateTimeField()                           # 등록일
    update_date = models.DateTimeField(
        null=True)                           # 수정일

    def __str__(self):
        return self.company_name