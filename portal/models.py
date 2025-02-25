from django.db import models
import datetime
# Create your models here.
class Category(models.Model):
	category=models.CharField(max_length=200)
	likes=models.IntegerField(default=0)
class Department(models.Model):
	dept_name=models.CharField(max_length=40,primary_key=True)
	hod_name=models.CharField(max_length=40)
	def __unicode__(self):              # __unicode__ on Python 2
        	return '%s' % (self.dept_name)

class Hostel(models.Model):
	hostel_name=models.CharField(max_length=50,primary_key=True)
	g_floor=models.IntegerField(default=0)
	f_floor=models.IntegerField(default=0)
	s_floor=models.IntegerField(default=0)
	image_path=models.CharField(max_length=200)
	rating=models.IntegerField(max_length=1)
	def __unicode__(self):              # __unicode__ on Python 2
        	return '%s' % (self.hostel_name)


class Student(models.Model):
	roll_no=models.CharField(max_length=10,primary_key=True)
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	email=models.EmailField(unique=True)
	contact_no=models.CharField(max_length=10)
	room_alloted=models.IntegerField(default=0)
	father_name=models.CharField(max_length=40)
	mother_name=models.CharField(max_length=40)
	address=models.CharField(max_length=400)
	gender=models.CharField(max_length=6)
	def __unicode__(self):              # __unicode__ on Python 2
        	return '%s' % (self.roll_no)
class Registration(models.Model):
	roll_no=models.ForeignKey(Student)
	year=models.IntegerField(max_length=1)
	semester=models.IntegerField()
	no_dues=models.IntegerField(default=0)
	fee_id=models.CharField(max_length=15)
	def __unicode__(self):              # __unicode__ on Python 2
        	return '%s' % (self.roll_no)

class Notifications(models.Model):
	roll_no_sender=models.CharField(max_length=10)
	roll_no_reciever=models.CharField(max_length=10)
	status=models.IntegerField(default=0)
	def __unicode__(self):              # __unicode__ on Python 2
        	return '%s' % (self.roll_no_reciever)
	
class Warden(models.Model):
	warden_id=models.IntegerField(primary_key=True)
	warden_name=models.CharField(max_length=40)
	contact_no=models.CharField(max_length=10)
	hostel_name=models.ForeignKey(Hostel)

class Complaints(models.Model):
	roll_no=models.ForeignKey(Student)
	category=models.CharField(max_length=50,default="other")
	date_time=models.DateTimeField( auto_now_add=True)
	message=models.CharField(max_length=1000)

class Batch(models.Model):
	roll_no=models.ForeignKey(Student,unique=True)
	year=models.IntegerField()
	department=models.ForeignKey(Department)
	def __unicode__(self):              # __unicode__ on Python 2
        	return '%s' % (self.roll_no)

class HostelAlloted(models.Model):
	year=models.IntegerField()
	department=models.ForeignKey(Department)
	hostel_name=models.ForeignKey(Hostel)
class Preference(models.Model):
	roll_no=models.ForeignKey(Student,unique=True)
	pref1=models.IntegerField()
	pref2=models.IntegerField()
	hostel_name=models.ForeignKey(Hostel)
class Verification(models.Model):
	roll_no=models.CharField(max_length=10,unique=True)
	hash_value=models.CharField(max_length=200)
	email=models.EmailField(unique=True)
	password=models.CharField(max_length=50)
class Suggestions(models.Model):
	roll_no=models.ForeignKey(Student)
	category=models.CharField(max_length=50,default="other")
	date_time=models.DateTimeField( auto_now_add=True)
	message=models.CharField(max_length=1000)
class Rooms(models.Model):
	room_no=models.IntegerField()	
	hostel_name=models.ForeignKey(Hostel)
	roll_no_1=models.CharField(max_length=10)
	roll_no_2=models.CharField(max_length=10)
	