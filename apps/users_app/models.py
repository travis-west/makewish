from __future__ import unicode_literals
from django.db import models
import re

#form validation stuff
class UserManager(models.Manager):
    def basic_validator(self, postData):
        # Regex stuff
        password_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.*\s).{8,}$')
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        name_regex = re.compile('.*\\d+.*') 

        errors = {}
        ### FIRST NAME VALIDATION ###
        if len(postData['first_name']) == 0:
            errors["first_name"] = "First name must be entered"
        elif len(postData['first_name']) < 2:
            errors["first_name"] = "Please provide full first name"
        elif len(postData['first_name']) > 254:
            errors["first_name"] = "Real humans don't have more than 250 letters in their first name"
        elif name_regex.match(postData['first_name']):
            errors["first_name"] = "First name cannot contain numbers"

        ### LAST NAME VALIDATION ###
        if len(postData['last_name']) == 0:
            errors["last_name"] = "Last name must be entered"        
        elif len(postData['last_name']) < 2:
            errors["last_name"] = "Please provide full last name"
        elif len(postData['last_name']) > 254:
            errors["last_name"] = "Real humans don't have more than 250 letters in their last name"
        elif name_regex.match(postData['last_name']):
            errors["last_name"] = "Last name cannot contain numbers"

        ### LAST NAME VALIDATION ###
        if len(postData['alias']) == 0:
            errors["alias"] = "Alias is required"        
        elif len(postData['alias']) < 4:
            errors["alias"] = "Alias should be 5 characters or longer"
        elif len(postData['alias']) > 254:
            errors["alias"] = "Real humans don't have an alias with 250 letters"

        ### EMAIL VALIDATION
        if len(postData['email_address']) == 0:
            errors["email_address"] = "Email is required"
        elif not email_regex.match(postData['email_address']):
            errors["email_address"] = "Not a valid email address"

        ### PASSWORD VALIDATION ###
        if len(postData['password1']) == 0:
            errors["password"] = "Password is required"

        elif len(postData['password1']) < 8:
            errors["password"] = "Password must be at least 8 characters"

        elif len(postData['password2']) == 0:
            errors["password"] = "Password confirmation is required"

        elif postData['password2'] != postData['password1']:
            errors["password"] = "Passwords do not match"

        elif password_regex.search(postData['password1']):
            errors["password"] = "Password must contain at least 1 uppercase letter and 1 number"

        return errors

#user model        
class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {}>".format(self.first_name, self.last_name)
