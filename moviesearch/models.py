# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your models here.
import mongoengine
from mongoengine import connect
connect('assest')

class letv(mongoengine.Document):
    name = mongoengine.StringField()
    vids = mongoengine.StringField()
    category = mongoengine.StringField()
    description = mongoengine.StringField()
    area = mongoengine.StringField()
    lgName = mongoengine.StringField()
    directory = mongoengine.StringField()
    subCategoryName = mongoengine.StringField()
    ispay = mongoengine.StringField()
    tag = mongoengine.StringField()
    duration = mongoengine.StringField()
    aid = mongoengine.StringField()
    videoTypeName = mongoengine.StringField()
    images = mongoengine.DictField()


class aiqiyi(mongoengine.Document):
    name = mongoengine.StringField()
    url = mongoengine.StringField()
    img = mongoengine.StringField()