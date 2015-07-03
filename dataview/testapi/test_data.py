__author__ = 'Kamal.S'
from models import Sample,Sample1



def create_test_data():
    for x in range(50):
        s1 = Sample1()
        s1.text = "text-"+str(x)
        s1.save()

    for x in range(100):
        s = Sample()
        s.name = "name - " + str(x)
        s.company = "company - " + str(x)
        s.phonenumber = "company - " + str(x)
        s.email = "email"+str(x)+"@email.com"
        s.save()
        for y in range(1,5):
            s.samples.add(Sample1.objects.get(id=y))
        s.save()

def sample_search(qstr):
    from haystack.query import SearchQuerySet
    from haystack.inputs import AutoQuery
    sqs = SearchQuerySet().models(Sample).raw_search(qstr).order_by('id')
    print dir(sqs.values)
    print str(sqs.query)
    print sqs[0]
