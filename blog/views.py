from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Blog
from .forms import BlogForm, UserForm
from django.utils import timezone

def post_index(request):
	posts = Blog.objects.all()
	context = {'posts': posts}
	return render(request, 'blog/post_index.html', context)

def post_detail(request, pk):
	post = get_object_or_404(Blog, pk = pk)
	context = {'post': post}
	return render(request, 'blog/post_detail.html', context)

def new_post(request):
	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			blog = form.save(commit = False)
			blog.author = request.user
			blog.publish_date = timezone.now()
			blog.save()
			return redirect('post_index')

	else:
		form = BlogForm()

	return render(request, 'blog/new_post.html', {'form': form})

def edit_post(request, pk):
	blog = get_object_or_404(Blog, pk = pk)
	if request.method == 'POST':
		form = BlogForm(request.POST, instance = blog)
		if form.is_valid():
			blog = form.save(commit = False)
			blog.author = request.user
			blog.publish_date = timezone.now()
			blog.save()
			return redirect('post_index')

	else:
		form = BlogForm(instance = blog)

	return render(request, 'blog/new_post.html', {'form': form})

def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user.save()
			user = authenticate(username=username, password= raw_password)
			login(request,user)
			return redirect('post_index')

	else:
		form=UserForm()
	return render(request, 'blog/register.html', {'form': form})

def my_posts(request):
	user = request.user
	posts = Blog.objects.filter(author = user)
	context = {'posts': posts}
	return render(request, 'blog/post_index.html', context)

def delete_post(request, pk):
	post = get_object_or_404(Blog, pk = pk)
	post.delete()
	return redirect('post_index')
