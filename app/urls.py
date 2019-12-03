from django.contrib import admin
from django.urls import path, include
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView,ItemSignUpView,ItemErrorView


admin.site.site_title = '最強アイテム'
admin.site.site_header = '最強アイテム'
admin.site.index_title = '管理画面'

urlpatterns = [
    path('',  ItemFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    path('signup/', ItemSignUpView.as_view(), name='signup'),
    path('error/', ItemErrorView.as_view(), name='error')
]
