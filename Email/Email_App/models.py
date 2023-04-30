from django.db import models

class email_send(models.Model):
    email_to=models.EmailField(max_length=100)
    email_from=models.EmailField(max_length=100)
    email_sub=models.CharField(max_length=100)
    email_body=models.CharField(max_length=100)
    email_attachment=models.FileField()

    def __str__(self):
        return self.email_to