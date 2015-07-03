__author__ = 'Kamal.S'

from django.db.models import Q, CharField
from tastypie.resources import ModelResource, ALL, fields
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from django.conf.urls.defaults import *
from tastypie.paginator import Paginator
from .models import Sample


class SampleResource(ModelResource):
    apply_values = fields.CharField('get_apply_values')

    class Meta:
        queryset = Sample.objects.all()
        resource_name = 'sample'
        ordering = ['id', 'company', 'email']
        filtering = {
            'id': ALL,
            'company': ['contains'],
            'email': ['contains'],
            'phonenumber': ['contains'],
            'name': ['contains']
        }

    def apply_filters(self, request, applicable_filters):
        result_set = super(SampleResource, self).apply_filters(request,
                                                     applicable_filters)
        fields_length = int(request.GET.get('iColumns', 0))
        query_string = request.GET.get('sSearch', None)
        filters = {}
        for i in xrange(fields_length):
            search_string = request.GET.get("sSearch_%s" % str(i))
            if search_string:
                column_name = request.GET.get("mDataProp_%s" % str(i))
                filter_name = "%s__contains" % column_name
                filters.update({filter_name: search_string})
        if query_string:
            query_set = (
                Q(company__icontains=query_string,**filters) |
                Q(email__icontains=query_string, **filters) |
                Q(name__icontains=query_string, **filters) |
                Q(phonenumber__icontains=query_string, **filters)
            )
            return result_set.filter(query_set)
        return result_set.filter(**filters)

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search/?$" % (
                self._meta.resource_name), self.wrap_view('get_search'),
                name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        '''
        Custom endpoint for search
        '''
        self.method_check(request, allowed=['get'])
        query = request.GET.get('q', "*:*")
        if not query:
            raise BadRequest(
                'Please supply the search parameter (e.g. '
                '"/api/v1/clips/search/?q=css")')

        results = SearchQuerySet().raw_search(query)
        if not results:
            results = EmptySearchQuerySet()

        paginator = Paginator(request.GET, results,
                              resource_uri='/api/v1/sample/search/')

        bundles = []
        for result in paginator.page()['objects']:
            bundle = self.build_bundle(obj=result.object, request=request)
            bundles.append(self.full_dehydrate(bundle))

        object_list = {
            'meta': paginator.page()['meta'],
            'objects': bundles
        }
        object_list['meta']['search_query'] = query

        self.log_throttled_access(request)
        return self.create_response(request, object_list)

    def calculation(self, data):
        print type(data)
        data['calculated_data'] = 'mdata'
        return data

    def dehydrate(self, bundle):
        bundle.data = self.calculation(bundle.data)
        return bundle