from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.

class log(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

GENDER_CHOICES={
    ('F','FEMALE'),
    ('M','MALE'),
    ('O','OTHERS')
}

SUBJECT_CHOICES={
    ('MATHS','MATHS'),
    ('PHYSICS','PHISICS'),
    ('CHEMISTRY','CHEMISTRY')

}

class teacherdata(models.Model):
    user=models.OneToOneField(log,on_delete=models.CASCADE,related_name='teacher')
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    photo = models.ImageField(null=True,blank=True)
    subject= models.CharField(max_length=20,choices=SUBJECT_CHOICES)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    DoB=models.DateField()
    tid=models.CharField(max_length=5)
    status = models.IntegerField(default=False)


    def __str__(self):
        return self.name

class studentdata(models.Model):
    user=models.ForeignKey(log,on_delete=models.CASCADE,related_name='suser')
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    photo = models.ImageField(null=True,blank=True)
    DoB = models.DateField()
    semester = models.CharField(max_length=200)
    guardian = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    sid=models.CharField(max_length=5)


    def __str__(self):
        return self.name


class courses(models.Model):
    course=models.CharField(max_length=200)
    discription=models.CharField(max_length=200)
    teachername=models.CharField(max_length=200)


    def __str__(self):
        return self.course


class notification(models.Model):
    messages=models.TextField(max_length=200)
    alert=models.CharField(max_length=2000)



    def __str__(self):
        return self.messages


class studentleave(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=100)
    messages=models.TextField()
    status=models.IntegerField(default=False)



    def __str__(self):
        return self.name


class teacherleave(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=100)
    messages=models.TextField()
    status=models.IntegerField(default=False)



    def __str__(self):
        return self.name


class teachercomplaint(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=100)
    complaint=models.TextField()
    replay=models.TextField()



    def __str__(self):
        return self.name

class studentcomplaint(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=100)
    complaint=models.TextField()
    replay=models.TextField()


    def __str__(self):
        return self.name


class noteupload(models.Model):
    subject=models.CharField(max_length=200)
    note=models.FileField(upload_to='notes',null=True)


    def __str__(self):
        return self.subject

class Attendance(models.Model):
    student=models.ForeignKey(studentdata,on_delete=models.CASCADE,related_name='attendance')
    attendance=models.CharField(max_length=10)
    date=models.DateField()
    time=models.TimeField()

class Assignment(models.Model):
    user=models.ForeignKey(log,on_delete=models.CASCADE)
    t_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=50,choices=SUBJECT_CHOICES)
    chap=models.IntegerField(null=True,blank=True)
    topic=models.CharField(max_length=100)

class uploadassign(models.Model):
    student=models.ForeignKey(log,on_delete=models.CASCADE)
    studentname=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    assignment=models.FileField()


class Question(models.Model):
    question=models.TextField(max_length=100,null=True)
    Ans=models.CharField(max_length=100)
    option_1=models.CharField(max_length=100)
    option_2=models.CharField(max_length=100)
    option_3=models.CharField(max_length=100)
    option_4=models.CharField(max_length=100)
    checkans=models.BooleanField(default=False)

    def __str__(self):
        return self.question


class Mark(models.Model):
    mark=models.IntegerField(null=True,blank=True)
    student=models.ForeignKey(log,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.mark