from django.shortcuts import render
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
# Create your views here.
def post_list(request):
	posts = Post.objects.order_by('created_date')
	return render(request, 'nasledie/post_list.html', {'posts': posts})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created_date = timezone.now()
			post.save()
			return redirect('post_list')
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html',{'form': form})	