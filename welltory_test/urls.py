from django.conf.urls import url
from welltory_test.views import data_views

urlpatterns = [
    url(r'^welltory_test$', data_views.get_data_list)
]
