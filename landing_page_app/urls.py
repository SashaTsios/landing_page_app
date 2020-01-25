"""landing_page_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import landing_page_view
from core.views import about_page_view
from core.views import contact_us_view
from core.views import feedbacks_view
from core.views import subjects_view
from core.views import subject_item_view
from core.views import subject_stats_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page_view),
    path('about-us/', about_page_view),
    path('contact-us/', contact_us_view),
    path('feedbacks-lalala/', feedbacks_view, name="feedbacks"),
    path('subjects<>/', subjects_view, name="subject"),
    path('subjects/', subjects_view),
    path('subjects/<str:subject_name_s>/', subject_item_view, name='subject'),
    path('subjects/<str:statistic_s1>/', subject_stats_view, name='subject_stats'),
    
]

#or    path('feedbacks/', feedbacks_view),