# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def updatepass(self, postdata):
        errors=[]
        if postdata['password']!=postdata['confirm_password']:
            errors.append('passwords must match')
        response={}
        if errors:
            response['Status']=False
            response['errors'] = errors
        else:
            password= bcrypt.hashpw(postdata['password'].encode(),bcrypt.gensalt())
            user = self.update(password=password)
            response['Status']=True
            response['user'] = user
        return response

    def register(self, postdata):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        errors=[]
        # print postdata
        if len(postdata['first_name']) < 3 or len(postdata['last_name']) < 3:
            errors.append('names need to be longet than 2 characters')

        if not NAME_REGEX.match(postdata['first_name']):
            errors.append('only letters')

        if not NAME_REGEX.match(postdata['last_name']):
            errors.append('only letters')

        if len(postdata['email']) < 0:
            errors.append('cannot be empty')

        if not EMAIL_REGEX.match(postdata['email']):
            errors.append('email format')

        if postdata['password']!=postdata['confirm_password']:
            errors.append('passwords must match')


        user = self.filter(email=postdata['email'])
        if user:
            errors.append('email already in use')
        response={}
        if errors:
            response['Status']=False
            response['errors'] = errors
        else:
            # print self.all()
            if not self.all():
                password= bcrypt.hashpw(postdata['password'].encode(),bcrypt.gensalt())
                user = self.create(first_name = postdata["first_name"],last_name= postdata["last_name"],email = postdata['email'],password=password, user_level=9)
                response['Status']=True
                response['user'] = user
            else:
                password= bcrypt.hashpw(postdata['password'].encode(),bcrypt.gensalt())
                user =self.create(first_name = postdata["first_name"],last_name= postdata["last_name"],email = postdata['email'],password=password, user_level=1)
                response['Status']=True
                response['user'] = user

        return response


    def login(self, postdata):
        user = self.filter(email=postdata['email'])
        if len(user) == 0:
            message = "you need to register"
            return {"Status":False, "errors":message}
        else:
            if bcrypt.hashpw(postdata['password'].encode(),user[0].password.encode()) != user[0].password:
                message="password incorrect"
                return{"Status":False,"errors":message}
        return {"Status":True, "user":user[0]}




class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email =models.CharField(max_length=140, default='SOME STRING')
    password = models.CharField(max_length=255)
    user_level = models.IntegerField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
