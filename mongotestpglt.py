from utilities import *
from pagelet import *
from viewcategory import *

u1 = User("Student","1")
u2 = User("Student","2")
u3 = User("Teacher","1")
u4 = User("Teacher","2")

workflow = Role("AugustPaper","AugustPaper Role")
workflow.adduser(u1.getid())
workflow.adduser(u2.getid())
workflow.adduser(u3.getid())
workflow.adduser(u4.getid())

stud_grp = Group("Students")
stud_grp.adduser(u1.getid())
stud_grp.adduser(u2.getid())

teach_grp = Group ("Teachers")
teach_grp.adduser(u3.getid())
teach_grp.adduser(u4.getid())

sessionuser = u3
q1 = Field(sessionuser.getid(),{"format":"textbox"},"Sin(30)=")
q2 = Field(sessionuser.getid(),{"format":"textbox"},"Cos(30)=")
q3 = Field(sessionuser.getid(),{"format":"textbox"},"tan(45)=")
q4 = Field(sessionuser.getid(),{"format":"textbox"},"tan(90)=")
g = Field(sessionuser.getid(),{"format":"textbox"},"Grade=")


qp_perm = Permissions({stud_grp.getid():{q1.getid():"-w",q2.getid():"-w",q3.getid():"-w",q4.getid():"-w",g.getid():"--"},teach_grp.getid():{q1.getid():"r-",q2.getid():"r-",q3.getid():"r-",q4.getid():"r-",g.getid():"--"}})


qpaper = ViewCategory(sessionuser.getid(),'qpaper', qp_perm.convert_dict_values(),qp_perm, workflow)

gp_perm = Permissions({stud_grp.getid():{q1.getid():"rn",q2.getid():"rn",q3.getid():"rn",q4.getid():"rn",g.getid():"r-"},teach_grp.getid():{q1.getid():"r-",q2.getid():"r-",q3.getid():"r-",q4.getid():"r-",g.getid():"rw"}})

gpaper = ViewCategory(sessionuser.getid(),'gpaper', gp_perm.convert_dict_values(), gp_perm,workflow)

p = Pagelet(sessionuser.getid(), "pagelet1",[qpaper],[q1,q2,q3,q4,g])
print "\nQpaper view attached:"  
#****************************************************************************************
# Session user is the student 1 now
#****************************************************************************************
sessionuser = u1
print "\nNow you are Student 1"
u1_p = p.postsimilar(sessionuser.getid(), p.name)

u1_p.edit(sessionuser.getid())

u1_p.view(sessionuser.getid())

sessionuser = u2
print "\nNow you are Student 2"
u2_p = p.postsimilar(sessionuser.getid(), p.name)

u2_p.edit(sessionuser.getid())

u2_p.view(sessionuser.getid())

pgtlist = [u1_p,u2_p]
p.listpagelets(u1.getid(),pgtlist)
#****************************************************************************************
# Session user is teacher now
#****************************************************************************************
sessionuser = u3
p.attachcategory(gpaper)
print "Grade the answers for student 1\n"
u1_p.edit(sessionuser.getid())
u1_p.view(sessionuser.getid())
print "Grade the answers for student 2\n"
u2_p.edit(sessionuser.getid())
u2_p.view(sessionuser.getid())

print "After grading!!!!\n"
print "Student 2"
p.listpagelets(u2.getid(),pgtlist)
