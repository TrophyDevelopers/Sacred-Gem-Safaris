from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

# client folder views
def index(request):
    usernames = User.objects.all()
    return render(request, 'client/index.html', {
        'usernames': usernames,
    })
    
# form folder views
def progess_form(request):
    usernames = User.objects.all()
    return render(request, 'client/form/form.html')

# destination folder views
def main_destination_page(request):
    usernames = User.objects.all()
    return render(request, 'client/destination/destination.html')
def particular_destination_page(request):
    usernames = User.objects.all()
    return render(request, 'client/destination/particular_destination.html')
def buhoma(request):
    usernames = User.objects.all()
    return render(request, 'client/destination/buhoma.html')
def bwindi(request):
    usernames = User.objects.all()
    return render(request, 'client/destination/bwindi.html')
def kidepo(request):
    usernames = User.objects.all()
    return render(request, 'client/destination/kidepo.html')
def murchison(request):
    usernames = User.objects.all()
    return render(request, 'client/destination/murchison.html')
def nkuringo(request):
    usernames = User.objects.all()
    return render(request, 'client/destination/nkuringo.html')
def mutanda(request):
    usernames = User.objects.all()
    return render(request, 'client/destination/mutanda.html')


# experiences folder views
def main_experience_page(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/experience.html')

def particular_experience_page(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/particular_experience.html')

def bwindi_intinerary(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/bwindi_intinerary.html')

def intinerary(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/intinerary.html')

def kidepo_intinerary(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/kidepo_intinerary.html')

def kigali_intinerary(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/kigali_intinerary.html')

def kenya_intinerary(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/kenya_intinerary.html')

def murchison_intinerary(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/murchison_intinerary.html')

def boat_safari(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/boat-safari.html')

def game_drives(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/game-drives.html')

def gorilla_trekking(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/gorilla.html')

def guided_quad_bike(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/guided-quad-bike.html')

def helicopter_safari(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/helicopter-safari.html')

def rhino_tracking(request):
    usernames = User.objects.all()
    return render(request, 'client/experience/rhino-tracking.html')

# journey folder views
# def main_journey_page(request):
#     usernames = User.objects.all()
#     return render(request, 'client/journey/journey.html')

# def view_journey_page(request):
#     usernames = User.objects.all()
#     return render(request, 'client/journey/view_journey_packages.html')

# def journey_details(request):
#     usernames = User.objects.all()
#     return render(request, 'client/journey/journey_details.html')

# blog folder views
def main_blog_page(request):
    usernames = User.objects.all()
    return render(request, 'client/blog/blog.html')

def read_blog_page(request):
    usernames = User.objects.all()
    return render(request, 'client/blog/read_blog.html')

# about folder views
def main_about_page(request):
    usernames = User.objects.all()
    return render(request, 'client/about/about.html')
def our_team_page(request):
    usernames = User.objects.all()
    return render(request, 'client/about/our_team.html')
def read_about(request):
    usernames = User.objects.all()
    return render(request, 'client/about/read_about.html')
def our_impact(request):
    usernames = User.objects.all()
    return render(request, 'client/about/our_impact.html')

# read more folder views
def read_more(request):
    usernames = User.objects.all()
    return render(request, 'client/read/read_more.html')

# shop folder urls
def shop(request):
    return render(request, 'client/shop/shop.html')

# dashboard
@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')