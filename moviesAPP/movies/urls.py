from django.urls import path, include


urlpatterns = [
    path("", render('template/index.html'), name="homepage")
    
]
