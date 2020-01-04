from django.db import models

class student(models.Model):
    full_name = models.CharField(max_length=100)

    email = models.EmailField()
    
    mac_address = models.CharField(max_length=200)

    attendence_stat = models.BooleanField(default= False)
    

    def __str__(self):
        return self.full_name

    def __iter__(self):
        return [
            self.full_name,
            self.email,
            self.mac_address,
            self.attendence_stat
        ]

class attendance_history(models.Model):
    student = models.CharField(max_length=100)
    date = models.DateField()
    attendance = models.BooleanField(default= True)

    def __str__(self):
        return self.student
