from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from . import models


class FiisListView(generic.ListView):
    model = models.Fii
    context_object_name = 'fiis'
    template_name = 'fiis_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request.GET
        print(request)  
        search = request.get('search', '') 
        segment = request.get('segment', '')
        if search:
            queryset = queryset.filter(name__icontains=search)
        if segment:
            queryset = queryset.filter(indicators__segmento__icontains=segment)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_segment'] = self.request.GET.get('segment', '')
        context['segments'] = models.Fii.objects.values_list('indicators__segmento', flat=True).distinct()
        return context

         


class FiisDetailView(generic.DetailView):
    model = models.Fii
    context_object_name = 'fii'
    template_name = 'fiis_detail.html'