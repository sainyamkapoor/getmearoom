from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from portal.models import *



class StudentForm(forms.Form):
	firstName = forms.CharField(label='First Name:',widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=20)
	lastName = forms.CharField(label='Last Name:',widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=20)
	gender = forms.ChoiceField(label='Gender:',widget=forms.Select(attrs={'class' : 'form-control'}),choices=(('Male','Male'),('Female','Female'),))
	
	fatherName = forms.CharField(label="Father's Name:",widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=40)
	motherName = forms.CharField(label="Mother's Name:",widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=40)
	address = forms.CharField(label='Permanent Address:',widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=400)
	department = forms.ModelChoiceField(label='Department:',widget=forms.Select(attrs={'class' : 'form-control'}),queryset=Department.objects.all())
	year = forms.ChoiceField(label='Year:',widget=forms.Select(attrs={'class' : 'form-control'}),choices=(('1','1'),("2",'2'),("3",'3'),("4",'4'),("5",'5'),))
		
	course = forms.ChoiceField(label='Course:',widget=forms.Select(attrs={'class' : 'form-control'}),choices=(('Btech.','Btech.'),("IDD",'IDD'),))
	mobile = forms.CharField(label='Mobile No.:',widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=10)

class PreferenceForm(forms.Form):
	pref1 = forms.IntegerField(label='Preference 1:',widget=forms.TextInput(attrs={'class' : 'form-control','id':'pref1'}),)
	pref2 = forms.IntegerField(label='Preference 2:',widget=forms.TextInput(attrs={'class' : 'form-control'}),)
	
class PassRecoveryForm(forms.Form):
	password = forms.CharField(label='New Password:',widget=forms.PasswordInput(attrs={'class' : 'form-control','id':'pass'}),)
	passwordC = forms.CharField(label='Confirm Password:',widget=forms.PasswordInput(attrs={'class' : 'form-control','id':'passConfirm'}),)
	
		
