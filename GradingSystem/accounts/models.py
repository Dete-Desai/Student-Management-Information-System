from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.postgres.fields import JSONField

# Create your models here.

COURSES_CHOICES = (
    ('csc 111 computer system', 'CSC 111 COMPUTER SYSTEM'),
    ('csc 112 algebra', 'CSC 112 ALGEBRA'),
    ('csc 113 calculus', 'CSC 113 CALCULUS'),
    ('csc 114 communication skills', 'CSC 114 COMMUNICATION SKILLS'),
    ('csc 115 hiv & aids', 'CSC 115 HIV & AIDS'),
    ('csc 116 programming', 'CSC 116 PROGRAMMING'),
    ('csc 117 economics', 'CSC 117 ECONOMICS'),
    
)
class smisformsdb(models.Model):
    student_name = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=18)
    course = models.CharField(max_length=30, choices=COURSES_CHOICES, default='g1')
    marks = models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=0)

    def __str__(self):
        return "{}-{}".format(self.student_name, self.registration_no, self.course, self.marks)

