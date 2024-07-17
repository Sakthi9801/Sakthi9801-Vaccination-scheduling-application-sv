from django.urls import path
from center import views 
app_name="center"

urlpatterns = [
    path("list/",views.center_list,name="list"),
    path("detail/<int:id>",views.center_detail,name="detail"),
    path("create/",views.create_center,name="create")
]
