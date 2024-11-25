from django.db import models
from datetime import datetime
import os

class Employee(models.Model):
    
	id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=50)
	contact_number = models.CharField(max_length=50)
	email = models.CharField(max_length = 200)
	age = models.IntegerField()
	emotion = models.CharField(max_length=200)
	heart_rate = models.CharField(max_length=200)


	def __str__(self):
		return self.name

	def num_photos(self):
		try:
			DIR = f"app/facerec/dataset/{self.name}_{self.id}"
			img_count = len(os.listdir(DIR))
			return img_count
		except:
			return 0 

class Detected(models.Model):
	emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
	time_stamp = models.DateTimeField()
	photo = models.ImageField(upload_to='detected/')

	def __str__(self):
		emp = Employee.objects.get(name=self.emp_id)
		return f"{emp.name} {self.time_stamp} {self.photo}"

class DetectedEmotion(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    emotion = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.emotion} at {self.timestamp}"
    

class DetectedEmotion1(models.Model):
    
    emotion = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.emotion} at {self.timestamp}"