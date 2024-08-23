from django.urls import path
from . import views

urlpatterns = [
    path('fiis/list/', views.FiisListView.as_view(), name='fiis_list'),
    path('fiis/<int:pk>/detail/', views.FiisDetailView.as_view(), name='fiis_detail'),
]