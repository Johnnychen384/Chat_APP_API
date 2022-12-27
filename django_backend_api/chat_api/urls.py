from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('api/register', csrf_exempt(views.create_user), name="create_user"),
    path('api/login', csrf_exempt(views.check_user), name="check_user"),
    path('api/allUsers', csrf_exempt(views.online_users), name="online_users"),
    path('api/addBuddy', csrf_exempt(views.add_buddy), name="add_buddy"),
    path('api/delete', csrf_exempt(views.delete_buddy), name="delete_buddy"),
    path('api/editUser', csrf_exempt(views.edit_user), name="edit_user"),
    path('api/allbuddies', csrf_exempt(views.get_buddies), name="get_buddies"),
    path('api/sendmessage', csrf_exempt(views.add_message), name="add_message"),
    path('api/allmessages', csrf_exempt(views.all_messages), name="all_messages")
]
