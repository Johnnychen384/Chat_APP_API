from rest_framework import serializers 
from .models import User, Buddy, Message


# User serials
class UserSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = User # tell django which model to use
        fields = ('id', 'username', 'password',) # tell django which fields to include


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username')
    recipient = serializers.CharField(source='recipient.username')
    
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'message']


class BuddySerializer(serializers.ModelSerializer):
    user_one = serializers.CharField(source='user_one.username')
    user_two = serializers.CharField(source='user_two.username')
    
    class Meta:
        model = Buddy
        fields = ['id', 'user_one', 'user_two', 'active']

