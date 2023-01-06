from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer, MessageSerializer, BuddySerializer
from .models import User, Message, Buddy
### ALLOWS YOU TO SEND JSON AS A RESPONSE
from django.http import JsonResponse
### ALLOWS YOU TO TRANSLATE DICTIONARIES INTO JSON DATA
import json


# for creating a new user
def create_user(request):
    if request.method == 'POST':

        registrationData = json.loads(request.body)
        username = registrationData['username']
        password = registrationData['password']

        newUser = User(username=username, password=password)
        newUser.save()
        id = newUser.id

        return JsonResponse({'id': id, 'username': username, 'password': password})

# login function
def check_user(request):
    if request.method == 'POST':

        registrationData = json.loads(request.body)
        username = registrationData['username']
        password = registrationData['password']

        if User.objects.get(username=username):
            user = User.objects.get(username=username)
            
            if password == user.password:
                return JsonResponse({'id': user.id, 'username': user.username, 'password': user.password})
            else:
                return JsonResponse({"No Match": "no matches"})
        else:
            return JsonResponse({"Failed": "no user found"})

# function to update username and pw
def edit_user(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        new_username = data['username']
        new_password = data['password']

        user = User.objects.get(id=data['id'])
        user.username = new_username
        user.password = new_password
        user.save()

        return JsonResponse({'id': user.id, 'username': user.username, 'password': user.password})

# function to get all users => friends or not
def online_users(request):
    if request.method == 'GET':
        allUsers = User.objects.all()
        allUsersList = []

        for obj in allUsers:
            allUsersList.append({'id': obj.id, 'username': obj.username})

        return JsonResponse(allUsersList, safe=False)

# function that allows users to add others to Buddy table.
def add_buddy(request):
    if request.method == 'POST':
        usersID = json.loads(request.body)
        
        user_1 = User.objects.get(id=usersID['user1'])
        user_2 = User.objects.get(id=usersID['user2'])
        
        new_buddy = Buddy(user1=user_1, user2=user_2, active=True)
        new_buddy.save()

        target_buddy = Buddy.objects.get(id=new_buddy.id)

        return JsonResponse({'id': target_buddy.id, 'user1': target_buddy.user1.id, 'user2': target_buddy.user2.id, 'active': target_buddy.active})

# function to delete a user from buddy list
def delete_buddy(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        buddy_id = data['id']
        my_id = data['my_id']
        target_buddy = Buddy.objects.get(user1=my_id, user2=buddy_id)

        target_buddy.delete()
        return JsonResponse({})

# function that gets a users buddylist
def get_buddies(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_id = data['id']

        all_buddies = Buddy.objects.all()
        my_buddies = []
        for obj in all_buddies:
            # print(obj.user1.id)
            if obj.user1.id == target_id:
                my_buddies.append({'id': obj.user2.id, 'username': obj.user2.username})
                # my_buddies.append(obj)
            else:
                print("Failed")
      
        return JsonResponse(my_buddies, safe=False)

# function that will add new message to Message table
def add_message(request):
    if request.method == "POST":
        data = json.loads(request.body)

        user1 = data['user1']
        user2 = data['user2']
        message = data['message']

        the_message = Message(sender=User.objects.get(id=user1), recipient=User.objects.get(id=user2), message=message)

        the_message.save()

        return JsonResponse({'id': the_message.id, 'sender': the_message.sender.id, 'recipient': the_message.recipient.id, 'message': the_message.message})

# function to get all messages that happened between 2 users.
def all_messages(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        my_id = data['my_id']
        other_id = data['other_id']

        all_msgs = Message.objects.all()
        my_msgs = []

        for obj in all_msgs:
            if obj.sender.id == my_id or obj.sender.id == other_id:
                if obj.recipient.id == my_id or obj.recipient.id == other_id:
                    my_msgs.append({'id': obj.id, 'sender': obj.sender.id, 'recipient': obj.recipient.id, 'message': obj.message})

        return JsonResponse(my_msgs, safe=False)