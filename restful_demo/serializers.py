# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 11:55 下午
# @Author  : renwoxing
# @File    : serializers.py
# @Software: PyCharm

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
