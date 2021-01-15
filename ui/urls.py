from django.urls import path
import ui.views as ui

urlpatterns = [
    path('', ui.home, name='home'),
    path('example/verbs/', ui.example_verbs, name='example_verbs'),
    path('verb/conjunct/', ui.conjunct_verb, name='conjunct_verb')

]
