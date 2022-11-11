from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import datetime


# Create your views here.
from onlineapp.forms import loginform, teacherdataform, studentdataform, courseform, notificationform, studentleaveform, \
    teacherleaveform, studentcomplaintform, teachercomplaintform, noteform, uploadassignmentform, topicassignmentform, \
    Questionform
from onlineapp.models import teacherdata, studentdata, courses, notification, studentleave, teacherleave, \
    studentcomplaint, teachercomplaint, noteupload, Attendance, Assignment, uploadassign, Question


def home(request):
    return render(request, 'home.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('adminpage')

        if user is not None and user.is_user:
            if user.teacher.status==True:
                login(request,user)
                return redirect('dash')

        if user is not None and user.is_student:
            login(request,user)
            return redirect('s_dash')

        else:
            messages.info(request, ' Invalid Credentials ')

    return render(request, 'loginpage.html')











# Admin

def adminpage(request):
    return render(request, 'admin/admin.html')


def tuserview(request):
    u=request.user
    teacherdata_form= teacherdata.objects.all()
    print(teacherdata_form)
    return render(request, 'admin/tuserview.html',{'teacherdata_form':teacherdata_form})


def tdelete(request,id):
    if request.method == 'POST':
        teacherdata.objects.get(id=id).delete()
        return redirect('tuserview')


def register(request):
    login_form = loginform()
    teacherdata_form = teacherdataform()
    if request.method == "POST":
        login_form = loginform(request.POST)
        teacherdata_form = teacherdataform(request.POST, request.FILES)
        if login_form.is_valid() and teacherdata_form.is_valid():
            user = login_form.save(commit=False)
            print(user)
            user.is_user = True
            user.save()
            teacher= teacherdata_form.save(commit=False)
            teacher.user = user
            teacher.save()
            print(teacher)
            messages.info(request,'registration successfully')
        return redirect('loginpage')
    return render(request, 'register.html', {'login_form': login_form ,'teacherdata_form':teacherdata_form})


def suserview(request):
    u=request.user
    studentdata_form= studentdata.objects.all()
    print(studentdata_form)
    return render(request, 'admin/suserview.html',{'studentdata_form':studentdata_form})



def sdelete(request,stid):
    if request.method == 'POST':
        studentdata.objects.get(id=stid).delete()
        return redirect('suserview')





def admin_notification(request):
    form3 = notificationform()
    if request.method == 'POST':
        form3 = notificationform(request.POST)
        if form3.is_valid():
            form3.save()
    return render(request, 'admin/notification.html', {'form3': form3})



def add_courses(request):
    form2=courseform()
    if request.method=='POST':
        form2=courseform(request.POST)
        if form2.is_valid():
            form2.save()
    return render(request, 'admin/add_courses.html',{'form2':form2})



def admin_courses(request):
    u=request.user
    courseform= courses.objects.all()
    print(courseform)
    return render(request, 'admin/courses.html',{'courseform':courseform})


def coursedelete(request,dcid):
    if request.method == 'POST':
        courses.objects.get(id=dcid).delete()
        return redirect('admin_courses')


def approve_teacher(request,id):
    teacher=teacherdata.objects.get(id=id)
    teacher.status=1
    teacher.save()
    messages.info(request,'accepts teacher login')
    return redirect('tuserview')


def reject_teacher(request,id):
    teacher=teacherdata.objects.get(id=id)
    teacher.status=2
    teacher.save()
    messages.info(request,'Reject teacher login')
    return redirect('tuserview')


def a_t_leave(request):
    teacher_leave=teacherleave.objects.all()
    return render(request, 'admin/a_t_leave.html',{'teacher_leave':teacher_leave})


def t_leaveapprove(request,tid):
    leave = teacherleave.objects.get(id=tid)
    leave.status = 1
    leave.save()
    return redirect('a_t_leave')


def t_leavereject(request,tid):
    leave = teacherleave.objects.get(id=tid)
    leave.status = 2
    leave.save()
    return redirect('a_t_leave')

def a_tcomplaint(request):
    u = request.user
    cform = teachercomplaint.objects.all()
    print(cform)
    return render(request,'admin/a_tcomplaint.html',{'cform':cform})












# Teacher

def dash(request):
   return render(request, 'teacher/teacherview.html')


def teacherview(request):
    u=request.user
    teacherdata_form= teacherdata.objects.filter(user=u)
    print(teacherdata_form)
    return render(request, 'teacher/teacherview.html',{'teacherdata_form':teacherdata_form})


def studentview(request):
    u = request.user
    studentdata_form = studentdata.objects.all()
    print(studentdata_form)
    return render(request, 'teacher/studentview.html', {'studentdata_form': studentdata_form})


def student_register(request):
    login_form = loginform()
    studentdata_form = studentdataform()
    if request.method == "POST":
        login_form = loginform(request.POST)
        studentdata_form = studentdataform(request.POST, request.FILES)
        if login_form.is_valid() and studentdata_form.is_valid():
            user = login_form.save(commit=False)
            print(user)
            user.is_student = True
            user.save()
            c= studentdata_form.save(commit=False)
            c.user = user
            c.save()
            print(c)
            messages.info(request,'registration successfully')
        return redirect('dash')
    return render(request,'teacher/student_register.html', {'login_form': login_form ,'studentdata_form':studentdata_form})



def student_update(request,stid):
    user=studentdata.objects.get(id=stid)
    form1=studentdataform(instance=user )
    if request.method=="POST":
        form1=studentdataform(request.POST or None,request.FILES,instance=user or None)
        if form1.is_valid():
            form1 = form1.save(commit=False)
            form1.save()
            return redirect('studentview')
    return render(request,'teacher/student_update.html',{'form1':form1})



def t_notification(request):
    u = request.user
    nform1 = notification.objects.all()
    print(nform1)
    return render(request,'teacher/t_notification.html',{'nform1':nform1})



def t_sleave(request):
    student_leave=studentleave.objects.all()
    return render(request,'teacher/t_sleave.html',{'student_leave':student_leave})



def t_sleaveapprove(request,id):
    leave = studentleave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('t_sleave')


def t_sleavedisapprove(request,id):
    leave = studentleave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('t_sleave')


def t_leaver(request):
    form1 = teacherleaveform()

    if request.method == 'POST':
        form1 = teacherleaveform(request.POST)
        if form1.is_valid():
            leave = form1.save(commit=False)
            leave.name = request.user
            # leave.title=form.get('title')
            # leave.messages=form.get('messages')
            leave.save()
            return redirect('dash')
    else:
        form1 = teacherleaveform()

    return render(request, 'teacher/t_leaver.html', {'form1': form1})



def t_leavestatus(request):
    u = request.user
    data1 = teacherleave.objects.filter(name=u)
    print(data1)
    return render(request, 'teacher/t_leavestatus.html', {'data1': data1})

def t_scomplaint(request):
    u = request.user
    cform = studentcomplaint.objects.all()
    print(cform)
    return render(request,'teacher/t_scomplaint.html',{'cform':cform})


def t_complaint(request):
    t_form = teachercomplaintform()
    if request.method == 'POST':
        t_form = teachercomplaintform(request.POST)
        if t_form.is_valid():
            t_form.save()
    return render(request, 'teacher/t_complaint.html', {'t_form': t_form})




def add_notes(request):
    nform = noteform()
    u=request.user
    if request.method == 'POST':
        nform = noteform(request.POST,request.FILES)
        if nform.is_valid():
            obj=nform.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('dash')
    return render(request, 'teacher/add_notes.html', {'nform': nform})


def ts_attandance(request):
    student =studentdata.objects.all()
    return render(request,'teacher/ts_attandance.html',{'student':student})


def t_markattendance(request,id):
    user =studentdata.objects.get(id=id)
    att=Attendance.objects.filter(student=user,date=datetime.date.today())
    if att.exists():
        messages.info(request,"Today attendance  already marked ")
        return redirect('ts_attandance')
    else:
        if request.method=='POST':
            atten=request.POST.get('attendance')
            Attendance(student=user,date= datetime.date.today(),attendance=atten).save()
            messages.info(request,"attendance added successfully")
            return redirect('ts_attandance')
    return render(request,'teacher/t_markattendance.html')


def view_attendance(request):
    value_list=Attendance.objects.values_list('date',flat=True).distinct()
    attendance={}
    for value in value_list:
        attendance[value]=Attendance.objects.filter(date=value)

    return render(request,'teacher/view_attendance.html',{'attendance':attendance})



def day_attendance(request,date):
    attendance=Attendance.objects.filter(date=date)
    return render(request,'teacher/day_attendance.html',{'attendance':attendance,'date':date})

def add_assignment_topic(request):
    form=topicassignmentform()
    u=request.user
    if request.method=='POST':
        form=topicassignmentform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('dash')
    return render(request,'teacher/add_assignment_topic.html',{'form':form})


def view_assignment(request):
    u = request.user
    form = uploadassign.objects.all()
    print(form)
    return render(request,'teacher/view_assignment.html', {'form': form})



def add_questions(request):
    form=Questionform()
    u=request.user
    if request.method=='POST':
        form=Questionform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('dash')
    return render(request,'teacher/add_questions.html',{'form':form})


def view_questions(request):
    u =request.user
    data =Question.objects.all()
    return render(request,'teacher/view_questions.html',{'data':data})

def delete_question(request,id):
    if request.method == 'POST':
        Question.objects.get(id=id).delete()
        return redirect('view_questions')


def question_update(request,id):
    user = Question.objects.get(id=id)
    form1 = Questionform(instance=user)
    if request.method == "POST":
        form1 = Questionform(request.POST or None, request.FILES, instance=user or None)
        if form1.is_valid():
            form1 = form1.save(commit=False)
            form1.save()
            return redirect('dash')
    return render(request,'teacher/question_update.html', {'form1': form1})





def t_markview(request):
    return render(request,'teacher/t_markview.html')







# Student

def s_dash(request):
    return render(request, 'student/s_dash.html')

def s_view(request):
    u = request.user
    studentdata_form = studentdata.objects.filter(user=u)
    print(studentdata_form)
    return render(request, 'student/s_view.html',{'studentdata_form': studentdata_form})


def s_notification(request):
    u = request.user
    nform1 = notification.objects.all()
    print(nform1)
    return render(request,'student/s_notification.html',{'nform1':nform1})


def s_tview(request):
    u=request.user
    teacherdata_form= teacherdata.objects.all()
    print(teacherdata_form)
    return render(request, 'student/s_tview.html',{'teacherdata_form':teacherdata_form})




def sr_leave(request):
    form = studentleaveform()

    if request.method == 'POST':
        form = studentleaveform(request.POST)
        if form.is_valid():
            leave=form.save(commit=False)
            leave.name=request.user
            # leave.title=form.get('title')
            # leave.messages=form.get('messages')
            leave.save()
            return redirect('s_dash')
    else:
        form=studentleaveform()

    return render(request, 'student/sr_leave.html', {'form': form})




def ss_leave(request):
    u = request.user
    data=studentleave.objects.filter(name=u)
    print(data)
    return render(request, 'student/ss_leave.html',{'data':data})


def s_complaint(request):
    s_form = studentcomplaintform()
    if request.method == 'POST':
        s_form = studentcomplaintform(request.POST)
        if s_form.is_valid():
            s_form.save()
    return render(request, 'student/s_complaint.html', {'s_form': s_form})


def view_note(request):
    u = request.user
    tnote=noteupload.objects.all()
    print(tnote)
    return render(request, 'student/view_note.html',{'tnote':tnote})

def s_view_attendance(request):
    u=studentdata.objects.get(user=request.user)
    attendance=Attendance.objects.filter(student=u)
    return render(request,'student/s_view_attendance.html',{'attendance':attendance})




def upload_assignment(request):
    assignment=uploadassignmentform()
    u=request.user
    if request.method=='POST':
        assignment=uploadassignmentform(request.POST,request.FILES)
        if assignment.is_valid():
            obj=assignment.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('s_dash')
    return render(request,'student/upload_assignment.html',{'assignment':assignment})


def assignmenttopic(request):
    u = request.user
    data = Assignment.objects.all()
    print(data)
    return render(request, 'student/assignmenttopic.html', {'data': data})

def s_questionview(request):
    if request.method=='POST':
        print(request.POST)
        qustions=Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in qustions:
            total+=1
            print(request.POST.get(q.question))
            print(q.Ans)
            print()
            if q.Ans == request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent=score/(total*10 *100)
        context={
            'score':score,
            'time':request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return redirect(s_dash)
    else:
        questions=Question.objects.all()
        context={
            'questions':questions
        }
    return render(request,'student/s_questionview.html',context)


