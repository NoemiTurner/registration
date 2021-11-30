from django.db import models

# Create your models here.
 class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    idnumber = models.PostiveBigIntegerField()
    email = models.EmailField(blank=True)
    datecreated = models.DateTimeField(blank=True, auto_now_add=True)
    datemodified = models.DateTimeField(blank=True, auto_now=True)
    
    @property
    def full_name(self):
        return f'{self.firstname} {self.full_name}'
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return f'ID: {self.id}, name: {self.full_name}, student id: {self.idnumber}, email: {self.email}, datecreated: {self.datecreated}, datemodified: {self.datemodified}'
    
    class Student(Person):
    YEARS_IN_SCHOOL = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]

    year_in_school = models.CharField(max_length=2, choices=YEARS_IN_SCHOOL)
    
    gpa = models.FloatField(max_length=4, blank=True)
    
    def __str__(self):
        return f'ID: {self.id}: {super(Student, self).__str__()} - year in school: {self.year_in_school}, major: {self.major}, gpa: {self.gpa}'    
    

