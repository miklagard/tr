from django.urls import path
import ui.views as ui

urlpatterns = [
    path('', ui.home, name='home'),
]
