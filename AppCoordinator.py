from UI.UI import *

gRepository=GradeRepository("grades.txt")
sRepository=StudentRepository("students.txt",gRepository)
sController=StudentController(sRepository)
gController=GradeController(gRepository)
ui=UI(sController,gController)

ui.mainMenu()