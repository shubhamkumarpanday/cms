from django.urls import path
from . import views

app_name = "features"

urlpatterns = [
    path("viewcourse/", views.viewCourse, name="viewcourse"),
    path("addcourse/", views.addCourse, name="addcourse"),
    path("viewlibrary/", views.viewLibrary, name="viewlibrary"),
    path("addlibrary/", views.addLibrary, name="addlibrary"),
    path("viewevents/", views.viewEvent, name="viewevent"),
    path("addevents/", views.addEvent, name="addevent"),
    path("addfees/", views.addFees, name="addfees"),
    path("viewfees/", views.viewFees, name="viewfees")
]

