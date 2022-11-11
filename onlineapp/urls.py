from django.urls import path

from onlineapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register', views.register, name='register'),

# Admin

    path('adminpage',views.adminpage,name='adminpage'),
    path('tuserview', views.tuserview, name='tuserview'),
    path('tdelete/<int:id>/', views.tdelete, name='tdelete'),
    path('suserview', views.suserview, name='suserview'),
    path('sdelete/<int:stid>/', views.sdelete, name='sdelete'),
    path('admin_notification', views.admin_notification, name='admin_notification'),
    path('admin_courses/', views.admin_courses, name='admin_courses'),
    path('add_courses/', views.add_courses, name='add_courses'),
    path('coursedelete/<int:dcid>/', views.coursedelete, name='coursedelete'),
    path('approve_teacher/<int:id>/', views.approve_teacher, name='approve_teacher'),
    path('reject_teacher/<int:id>/', views.reject_teacher, name='reject_teacher'),
    path('a_t_leave', views.a_t_leave, name='a_t_leave'),
    path('t_leaveapprove//<int:tid>', views.t_leaveapprove, name='t_leaveapprove'),
    path('t_leavereject//<int:tid>', views.t_leavereject, name='t_leavereject'),
    path('a_tcomplaint', views.a_tcomplaint, name='a_tcomplaint'),

    # Teacher

    path('dash', views.dash, name='dash'),
    path('studentview',views.studentview,name='studentview'),
    path('student_register',views.student_register,name='student_register'),
    path('student_update/<int:stid>/',views.student_update, name='student_update'),
    path('teacherview', views.teacherview, name='teacherview'),
    path('t_notification', views.t_notification, name='t_notification'),
    path('t_sleave', views.t_sleave, name='t_sleave'),
    path('t_sleaveapprove/<int:id>/', views.t_sleaveapprove, name='t_sleaveapprove'),
    path('t_sleavedisapprove/<int:id>/', views.t_sleavedisapprove, name='t_sleavedisapprove'),
    path('t_leaver', views.t_leaver, name='t_leaver'),
    path('t_leavestatus', views.t_leavestatus, name='t_leavestatus'),
    path('t_scomplaint', views.t_scomplaint, name='t_scomplaint'),
    path('t_complaint', views.t_complaint, name='t_complaint'),
    path('add_notes', views.add_notes, name='add_notes'),
    path('ts_attandance', views.ts_attandance, name='ts_attandance'),
    path('t_markattendance/<int:id>/', views.t_markattendance, name='t_markattendance'),
    path('view_attendance', views.view_attendance, name='view_attendance'),
    path('day_attendance/<date>/', views.day_attendance, name='day_attendance'),
    path('add_assignment_topic', views.add_assignment_topic, name='add_assignment_topic'),
    path('view_assignment', views.view_assignment, name='view_assignment'),
    path('add_questions', views.add_questions, name='add_questions'),
    path('view_questions', views.view_questions, name='view_questions'),
    path('delete_question/<int:id>/', views.delete_question, name='delete_question'),
    path('question_update/<int:id>/', views.question_update, name='question_update'),
    path('t_markview', views.t_markview, name='t_markview'),


    # Student

    path('s_dash',views.s_dash, name='s_dash'),
    path('s_view',views.s_view, name='s_view'),
    path('s_notification',views.s_notification, name='s_notification'),
    path('ss_leave',views.ss_leave, name='ss_leave'),
    path('sr_leave',views.sr_leave, name='sr_leave'),
    path('s_tview',views.s_tview, name='s_tview'),
    path('s_complaint',views.s_complaint, name='s_complaint'),
    path('view_note',views.view_note, name='view_note'),
    path('s_view_attendance',views.s_view_attendance, name='s_view_attendance'),
    path('upload_assignment',views.upload_assignment, name='upload_assignment'),
    path('assignmenttopic',views.assignmenttopic, name='assignmenttopic'),
    path('s_questionview',views.s_questionview, name='s_questionview'),




]