__author__ = 'Kamal.S'

from haystack.forms import SearchForm

class SampleSearchForm(SearchForm):

    def search(self):
        sqs = super(SampleSearchForm, self).search()

        if not self.is_valid():
            self.no_query_found()
        print len(sqs), sqs
        return sqs