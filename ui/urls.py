from django.urls import path
import ui.views as ui


urlpatterns = [
    path('', ui.home, name='home'),
    path('nouns/', ui.nouns, name='nouns'),
    path('example/verbs/', ui.example_verbs, name='example_verbs'),
    path('verb/conjunct/', ui.conjunct_verb, name='conjunct_verb'),
    path('verb/conjunct/<slug:verb>/', ui.conjunct_verb_slug, name='conjunct_verb'),
    path('davidnathan/', ui.david, name='david'),
    path('robots.txt', ui.robots, name='robots'),
    path('sitemap.xml', ui.sitemap, name='sitemap'),
    path('.well-known/acme-challenge/j6HDxDY34uCtqLQKiAC1tT_t_bVPQ3cG9vFzjYwsRdo', ui.cert, name='rt')
]

handler404 = ui.page_not_found
handler500 = ui.server_error
