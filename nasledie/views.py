from django.shortcuts import render
from django.views.generic import DetailView
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .models import Block
# Create your views here.
def post_list(request):
	posts = Post.objects.order_by('created_date')
	blocks = Block.objects.order_by('created_date')
	return render(request, 'nasledie/post_list.html', {'posts': posts, 'blocks': blocks})
def index(request):
	blocks = Block.objects.order_by('created_date')
	return render(request, 'nasledie/index.html', {'blocks': blocks})
def list_block(request):
	posts = Post.objects.order_by('created_date')
	blocks = Block.objects.order_by('created_date')
	return render(request, 'nasledie/list_block.html', {'posts': posts,'blocks': blocks})
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
class PostDetailView(DetailView):

    queryset = Post.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(PostDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        date=[]
        date.append(object)
        # Return the object
        return object
