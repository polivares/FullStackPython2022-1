from mysqlconnection import connectToMySQL

# Crearemos una clase llamada Grupo
class Course:
    def __init__(self, data):
        self.CourseID = data['CourseID']
        self.Code = data['Code']
        self.Name = data['Name']
        self.students = []
    
    @classmethod
    def get_students_by_course(cls, data):
        query = "select * from Course left join CourseMembership on Course.CourseID = CourseMembership.Course left join Student on CourseMembership.Student = Student.StudentID where Course.CourseID=%(CourseID)s;"
        mysql = connectToMySQL('University')
        results = mysql.query_db(query, data)
        course = cls(results[0])
        for row_from_db in results:
            student_data={
                'StudentID': row_from_db['StudentID'],
                'FirstName': row_from_db['FirstName'],
                'LastName': row_from_db['LastName'],
            }

            course.students.append(Student(student_data))
        return course

# Clase de estudiantes
class Student:
    def __init__(self, data):
        self.StudentID = data['StudentID']
        self.FirstName = data['FirstName']
        self.LastName = data['LastName']

# Clase entre CourseMembership (no usada en este ejemplo, pero recomendada)
class CourseMembership:
    def __init__(self, data):
        self.Student = data['Student']
        self.Course = data['Course']

# Curso a recuperar
data = {'CourseID': 1}
curso = Course.get_students_by_course(data)
# Imprimo información del curso
print("Código del curso", curso.Code)
print("Nombre del curso", curso.Name)
print("Alumnos del curso")
for student in curso.students:
    print(student.FirstName, student.LastName)
