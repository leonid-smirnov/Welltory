"""urls to main project url file"""

from django.conf.urls import url
from welltory_test.views import data_views

urlpatterns = [
    url(r'^welltory_test$', data_views.get_data_list),
    url(r'^welltory_test/(?P<pk>[0-9]+)$', data_views.get_data_detail),
    url(r'^welltory_test/user/(?P<user_id>[0-9]+)$', data_views.get_all_data_by_user_id)
]
