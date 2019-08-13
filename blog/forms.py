from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Blog, Profile

class BlogForm(ModelForm):

	class Meta:
		model = Blog
		fields = ('title', 'content')

class UserForm(UserCreationForm):
	
	class Meta(UserCreationForm):
		model = Profile
		fields = ['username','first_name','last_name','password1','password2','email','gender','date_of_birth','bio']