from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from .views import tj_views, ky_views
#from .views import TodoViewset

router = routers.DefaultRouter()
#router.register("todo", TodoViewset, "todo")

tj_patterns = [
    path("monthnew", tj_views.MonthNewView.as_view(), name="tj_monthnew"),
    path("hitsong", tj_views.HitSongView.as_view(), name="th_hitsong")
]

ky_patterns = [
#    path("monthnew", ky_views.monthnew, name="ky_monthnew")
]

urlpatterns = [
    path("tj/", include(tj_patterns)),
    path("ky/", include(ky_patterns))
]

