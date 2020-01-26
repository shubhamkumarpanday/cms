from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=30)
    course_code = models.CharField(max_length=30)
    course_details = models.CharField(max_length=30)
    course_date = models.DateField(max_length=30)
    course_price = models.CharField(max_length=30)
    professor_name = models.CharField(max_length=30)
    maximum_students = models.IntegerField(max_length=30)
    contact_number = models.CharField(max_length=12)

class Fees(models.Model):
    roll_no = models.CharField(max_length=10)
    student_name = models.CharField(max_length=10)
    department_class = models.CharField(max_length=10)
    fees_type = models.CharField(max_length=10)
    amount = models.IntegerField(max_length=10)
    collection_date = models.DateField(max_length=10)
    payment_reference = models.CharField(max_length=10)

class Library(models.Model):
    title = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    author_name = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    asset_details = models.CharField(max_length=30)
    date_added = models.DateField(auto_now=True)

class Events(models.Model):
    event_name = models.CharField(max_length=30)
    from_date = models.DateField(max_length=30)
    to_date = models.DateField(max_length=30)
    organised_by = models.CharField(max_length=30)



    
