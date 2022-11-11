from django import forms
from django.contrib.auth.forms import UserCreationForm

from onlineapp.models import log, teacherdata, studentdata, notification, courses, studentleave, teacherleave, \
    teachercomplaint, studentcomplaint, noteupload, Attendance, Assignment, uploadassign, Question, Mark


class loginform(UserCreationForm):

    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label='password')
    password2=forms.CharField(widget=forms.PasswordInput,label='confirmpassword')
    class Meta:
        model = log
        fields = ('username','password1','password2')

class teacherdataform(forms.ModelForm):
    class Meta:
        model = teacherdata
        fields = ('name','address','photo','subject','gender','DoB')


class studentdataform(forms.ModelForm):
    class Meta:
        model = studentdata
        fields = ('name','address','photo','semester','gender','DoB','guardian')


class courseform(forms.ModelForm):
    class Meta:
        model = courses
        fields = ('discription','course','teachername')


class notificationform(forms.ModelForm):
    class Meta:
        model = notification
        fields = ('alert','messages')


class studentleaveform(forms.ModelForm):
    class Meta:
        model = studentleave
        fields = ('title','messages')


class teacherleaveform(forms.ModelForm):
    class Meta:
        model = teacherleave
        fields = ('title','messages')

class teachercomplaintform(forms.ModelForm):
    class Meta:
        model = teachercomplaint
        fields = ('title','complaint')


class studentcomplaintform(forms.ModelForm):
    class Meta:
        model = studentcomplaint
        fields = ('title','complaint')




class noteform(forms.ModelForm):
    note=forms.FileField()
    class Meta:
        model = noteupload
        fields = ('subject','note')


att_choice=(
    ('present','present'),
    ('absent','absent')
)

class attendanceform(forms.ModelForm):
    student=forms.ModelChoiceField(queryset=studentdata.objects.all())
    attandance=forms.ChoiceField(choices=att_choice,widget=forms.RadioSelect)
    class Meta:
        model=Attendance
        fields=('student','attendance')


class uploadassignmentform(forms.ModelForm):
    class Meta:
        model=uploadassign
        fields=('student','studentname','assignment')


class topicassignmentform(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('t_name','subject','chap','topic')


ANSWER_CHOICES=(
    ('option1','option1'),
    ('option2','option2'),
    ('option3','option3'),
    ('option4','option4'),
)

class Questionform(forms.ModelForm):
    Ans = forms.ChoiceField(choices=ANSWER_CHOICES,widget=forms.RadioSelect)
    class Meta:
        model=Question
        fields=('question','Ans','option_1','option_2','option_3','option_4')


class Markform(forms.ModelForm):
    class Meta:
        model=Mark
        fields=('student','name','mark')