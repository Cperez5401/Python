from django.db import models

import bcrypt
import re

class UserManager(models.Manager):
    def registration_validator(self, post_data):
        errors ={}

        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters."

        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"

        if len(post_data['password']) < 4:
            errors['password'] = "Password must be at least 4 characters."

        if post_data['password'] != post_data['confirmPw']:
            errors['confrimPw'] = "Password does not match Confirm password"

        return errors

    def login_validator(self, post_data):
        errors ={}
        user_list = User.objects.filter(email=post_data['email'])
        if len(user_list) > 0:
            user = user_list[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                error['password'] = "Invalid Credentials"
        else:
            errors['email'] = "Invalid Credentials"

        return errors


class TripsManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        if len(post_data['destination']) < 3:
            errors['destination'] = "Destination should be longer than 3 characters"

        if len(post_data['startDate']) < 1:
            errors['startDate'] = "Start Date must be entered"

        if len(post_data['endDate']) < 1:
            errors['endDate'] = "End date must be enterd"

        if len(post_data['plan']) < 3:
            errors['plan'] = "Plan must be longer than 3 characters"

        return errors



class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    objects = UserManager()

class Trips(models.Model):
    user = models.ForeignKey(User, related_name='trips', on_delete = models.CASCADE, null=True)
    destination = models.CharField(max_length=255)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    plan = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TripsManager()



