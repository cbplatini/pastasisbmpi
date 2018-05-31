from django.urls import path
from .views import index, militar_list, militar_new, militar_update, militar_delete


urlpatterns = [
    path('', militar_list, name='militar_list'),
    path('militar_new/', militar_new, name='militar_new'),
    path('militar_update/<int:id>', militar_update, name='militar_update'),
    path('militar_delete/<int:id>', militar_delete, name='militar_delete')
]
