
from django.test import TestCase, Client
class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()
    def test_response(self):
        response = self.test_client.get('/regserve/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello world from django backend")
        
class DataTest(TestCase):
    def setUp(self):
        student1 = Student.objects.create(
            firstname = "First",
            lastname = "Student",
            email="first@student.edu"
            schoolyear = "FR",
            major = "CS",
            gpa = 4.0,
        )
        
        student2 = Student.objects.create(
            firstname = "Second",
            lastname = "Student",
            email="second@student.edu"
            schoolyear = "SE",
            major = "ENG",
            gpa = 2.0,
        )
        
    def test_student(self):
        student_list = Student.objects.all()
        student = student_list[0]
        print(f'Inside test student: student is {student}')
        self.assertEqual(student.id, 100)
        
            