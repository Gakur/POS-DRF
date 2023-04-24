from django.urls import path

from .views import StoreAPIView

app_name = "store"

urlpatterns = [
    path('store/', StoreAPIView.as_view()),
                                                                                                                                                                                                                                                                                                                                 
]
