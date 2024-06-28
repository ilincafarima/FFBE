from django.shortcuts import render, redirect
from .forms import RegistrationForm, SearchForm, ModifyForm
from django.shortcuts import redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q
from blog.models import BlogPost  # Import the BlogPost mode
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')  # Redirect to home page after successful login
        else:
            # Check if the username exists in the database
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Invalid password. Please try again.')
            else:
                messages.error(request, 'User does not exist. Please register.')
    
    return render(request, 'login.html')

def landing_page(request):
    # Fetch the last three blog posts
    last_three_posts = BlogPost.objects.order_by('-timestamp')[:3]

    # Pass the last three blog posts to the template context
    return render(request, 'home.html', {'last_three_posts': last_three_posts})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query').strip()
            if query:
                results = CustomUser.objects.filter(
                    Q(role='Fixer') &
                    (Q(username__icontains=query) |
                    Q(email__icontains=query) |
                    Q(first_name__icontains=query) |
                    Q(last_name__icontains=query)
                    # Add more fields as needed
                    )
                )
                return render(request, 'search_results.html', {'form': form, 'results': results, 'query': query})
            else:
                return render(request, 'search_results.html', {'form': form, 'results': [], 'query': ''})
        else:
            return render(request, 'search_results.html', {'form': form, 'results': [], 'query': ''})
    else:
        form = SearchForm()
        return render(request, 'search_results.html', {'form': form, 'results': [], 'query': ''})

@login_required
def profile_view(request):
    # Assuming you have a template named 'profile.html' to render the user's profile
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout
    return redirect('landing_page')  # Redirect to the landing page after logout


# @login_required
# def modify_user(request, id):
    