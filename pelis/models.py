from django.db import models

# Create your models here.

from mongoengine import *

connect('movies', host='mongo')

class Pelis(Document):
    title = StringField(required=True)
    year = IntField(min_value=1900, max_value=2222)
    rated = StringField()
    runttime = IntField()
    countries = ListField(StringField())
    genres = ListField(StringField())
    director = StringField()
    writers = ListField(StringField())
    actors = ListField(StringField())
    plot = StringField()
    poster = StringField()
    imdb = DictField()
    tomato = DistField()
    metacritic = IntField()
    awards = DictField()
