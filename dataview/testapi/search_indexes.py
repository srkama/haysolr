__author__ = 'Kamal.S'

import datetime
from haystack import indexes
from .models import Sample



class SampleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    company = indexes.EdgeNgramField(model_attr='company')
    name=indexes.EdgeNgramField(model_attr='name')
    email=indexes.EdgeNgramField(model_attr='email')

    def get_model(self):
        return Sample

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

