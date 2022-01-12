from django.conf.urls import url
from welltory_test.views import data_views

urlpatterns = [
    url(r'^welltory_test$', data_views.get_data_list),
    url(r'^welltory_test/(?P<user>[0-9]+)$', data_views.get_data_detail)
]
