# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
import logging
import json
from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate

from django.contrib.auth.models import User
# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

def logout_request(request):
    logout(request)
    return JsonResponse({"message": "Logged out successfully"})

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return JsonResponse({"message": "User created and logged in"})
    return JsonResponse({"error": "Invalid request"}, status=400)



import json
from django.shortcuts import render

def get_dealerships(request):
    with open('C:\\Users\\Mr.Code\\Desktop\\fullstack_developer_capstone-mainv1\\server\\database\\data\\dealerships.json') as f:
        data = json.load(f)
    dealerships = data.get('dealerships', [])
    return JsonResponse({"dealerships": dealerships})

def get_car(request):
    with open('C:\\Users\\Mr.Code\\Desktop\\fullstack_developer_capstone-mainv1\\server\\database\\data\\car_records.json') as f:
        data = json.load(f)
        print(data)
    cars = data.get('cars', [])
    # print(car_records)
    return JsonResponse({"cars": cars})


def get_dealer_reviews(request, dealer_id):
    with open("C:\\Users\\Mr.Code\\Desktop\\fullstack_developer_capstone-mainv1\\server\\database\\data\\reviews.json") as f:
        data = json.load(f)
    reviews = [review for review in data.get('reviews', []) if review['id'] == dealer_id]
    return JsonResponse({"reviews":reviews})


def get_dealer_details(request, dealer_id):
    with open('C:\\Users\\Mr.Code\\Desktop\\fullstack_developer_capstone-mainv1\\server\\database\\data\\dealerships.json') as f:
        data = json.load(f)
    dealership = next((dealer for dealer in data.get('dealerships', []) if dealer['id'] == dealer_id), None)
    return JsonResponse({"dealarship":dealership})


def add_review(request):
    if request.method == 'POST':
        with open('C:\\Users\\Mr.Code\\Desktop\\fullstack_developer_capstone-mainv1\\server\\database\\data\\reviews.json', 'r+') as f:
            data = json.load(f)
            review_id = data.get('next_review_id', 1)
            review_data = json.loads(request.body)
            new_review = {
                'id': review_id,
                'dealer_id': review_data['dealer_id'],
                'rating': review_data['rating'],
                'comment': review_data['comment']
            }
            data['reviews'].append(new_review)
            data['next_review_id'] = review_id + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return JsonResponse({"message": "Review added successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)