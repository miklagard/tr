from django.urls import path
import ui.views as ui


urlpatterns = [
    path('', ui.home, name='home'),
    path('nouns/', ui.nouns, name='nouns'),
    path('example/verbs/', ui.example_verbs, name='example_verbs'),
    path('verb/conjunct/', ui.conjunct_verb, name='conjunct_verb'),
    path('verb/conjunct/<slug:verb>/', ui.conjunct_verb_slug, name='conjunct_verb'),
    path('robots.txt', ui.robots, name='robots'),
    path('sitemap.xml', ui.sitemap, name='sitemap'),
]
