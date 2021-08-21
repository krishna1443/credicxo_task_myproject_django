from django.db import models

class Teacher(models.Model):
	POSITION_NAME  = (
            ("INSTRUCTOR","INSTRUCTOR"),			
			("ACADEMIC","ACADEMIC"),
            ("PROFESSOR","PROFESSOR"),
            ("SUPERVISOR","SUPERVISOR")
            
		)
	first_name = models.CharField(max_length = 200, null = True)
	last_name = models.CharField(max_length = 200, null = True)
	email = models.EmailField(null=True, unique=True, blank=True)
	address = models.CharField(max_length = 500, null = True)
	position = models.CharField(max_length =  255, default="NOT SELECTED", choices=POSITION_NAME)
	created_date = models.DateTimeField(auto_now = True)
	updated_date = models.DateTimeField(auto_now_add = True)



class Student(models.Model):
	first_name = models.CharField(max_length = 200, null = True)
	last_name = models.CharField(max_length = 200, null = True)
	email = models.EmailField(null=True, unique=True, blank=True)
	address = models.CharField(max_length = 500, null = True)
	created_date = models.DateTimeField(auto_now = True)
	updated_date = models.DateTimeField(auto_now_add = True)

