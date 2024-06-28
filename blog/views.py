from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost, Comment  
from .forms import CommentForm
import pyrebase

config = {
   'apiKey': "AIzaSyBe4ilBMIxD8S_umI87iAvfUEs0QA1do3o",
  'authDomain': "fir-a0040.firebaseapp.com",
  'projectId': "fir-a0040",
  'databaseURL': "https://fir-a0040-default-rtdb.firebaseio.com",
  'storageBucket': "fir-a0040.appspot.com",
  'messagingSenderId': "1045990739754",
  'appId': "1:1045990739754:web:95172527626aa7c0995853",
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def blog_list(request):
    # Retrieve all blog posts from the database
    blog_posts = BlogPost.objects.all()
    
    # Paginate the blog posts
    paginator = Paginator(blog_posts, 10)  # Show 10 blog posts per page
    page_number = request.GET.get('page')
    try:
        blog_posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog_posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def blog_detail(request, blog_id):
    blog_post = get_object_or_404(BlogPost, id=blog_id)
    comments = Comment.objects.filter(post=blog_post)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog_post
            comment.author = request.user  # Assuming you have authentication set up
            comment.save()
            return redirect('blog_detail', blog_id=blog_id)  # Redirect back to the same blog detail page
    else:
        form = CommentForm()

    return render(request, 'blog_detail.html', {'blog_post': blog_post, 'comments': comments, 'form': form})