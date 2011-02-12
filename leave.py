from utilities import *
from pagelet import *
from viewcategory import *

u1 = User("Student","1")
u2 = User("Parent","1")
u3 = User("Teacher","1")
u4 = User("Admin","Boy")

workflow = Role("Leave letter","Leave letter Role")
workflow.adduser(u1.getid())
workflow.adduser(u2.getid())
workflow.adduser(u3.getid())

stud_grp = Group("Students")
stud_grp.adduser(u1.getid())

parnt_grp = Group("Parents")
parnt_grp.adduser(u2.getid())

teachr_grp = Group ("Teachers")
teachr_grp.adduser(u3.getid())
teachr_grp.adduser(u4.getid())

sessionuser = u4
q1 = Field(sessionuser.getid(),{"format":"textbox"},"Name:")
q2 = Field(sessionuser.getid(),{"format":"textbox"},"Description:")
q3 = Field(sessionuser.getid(),{"format":"textbox"},"Student signature:")
q4 = Field(sessionuser.getid(),{"format":"textbox"},"Parent signature:")
q5 = Field(sessionuser.getid(),{"format":"textbox"},"Teacher signature:")


student = Permissions({stud_grp.getid():{q1.getid():"rw",q2.getid():"rw",q3.getid():"rw",q4.getid():"--",q5.getid():"--"},parnt_grp.getid():{q1.getid():"--",q2.getid():"--",q3.getid():"--",q4.getid():"--",q5.getid():"--"},teachr_grp.getid():{q1.getid():"--",q2.getid():"--",q3.getid():"--",q4.getid():"--",q5.getid():"--"}})


student = ViewCategory(sessionuser.getid(),'student', student.convert_dict_values(),student, workflow)

parent = Permissions({stud_grp.getid():{q1.getid():"rn",q2.getid():"rn",q3.getid():"rn",q4.getid():"r-",q5.getid():"--"},parnt_grp.getid():{q1.getid():"r-",q2.getid():"rw",q3.getid():"r-",q4.getid():"rw",q5.getid():"--"},teachr_grp.getid():{q1.getid():"--",q2.getid():"--",q3.getid():"--",q4.getid():"--",q5.getid():"--"}})


parent = ViewCategory(sessionuser.getid(),'parent', parent.convert_dict_values(), parent,workflow)

third_perm =  Permissions({stud_grp.getid():{q1.getid():"rn",q2.getid():"rn",q3.getid():"rn",q4.getid():"rn",q5.getid():"rn"},parnt_grp.getid():{q1.getid():"rn",q2.getid():"rn",q3.getid():"rn",q4.getid():"rw",q5.getid():"rn"},teachr_grp.getid():{q1.getid():"r-",q2.getid():"r-",q3.getid():"r-",q4.getid():"r-",q5.getid():"rw"}})

teacher = ViewCategory(sessionuser.getid(), 'teacher', third_perm.convert_dict_values(), third_perm,workflow)

p = Pagelet(sessionuser.getid(), "Leave letter",[student],[q1,q2,q3,q4,q5])
print "\nStudent view attached:"  
#****************************************************************************************
# Session user is the student 1 now
#****************************************************************************************
sessionuser = u1
print "\nNow you are Student 1"
u1_p = p.postsimilar(sessionuser.getid(), p.name)

u1_p.edit(sessionuser.getid())

u1_p.view(sessionuser.getid())

sessionuser = u2
p.attachcategory(parent)
print "\nNow you are Parent"

u1_p.edit(sessionuser.getid())

u1_p.view(sessionuser.getid())
"""pgtlist = [p,u1_p,u2_p]
p.listpagelets(u1.getid(),pgtlist)
#****************************************************************************************
# Session user is teacher now
#****************************************************************************************
"""
sessionuser = u3
p.attachcategory(teacher)
print "You are the teacher now\n"
u1_p.edit(sessionuser.getid())
u1_p.view(sessionuser.getid())
