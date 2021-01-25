from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from turkish_suffix_library.sample_verbs_list import VERBS
from turkish_suffix_library.turkish_string import make_upper
from django.utils.translation import gettext as _
from django.conf import settings
from ui.models import History
from ui.english import ENGLISH_TO_TURKISH
import os
import json
import ui.consonants as con
import ui.utils as utils


def nouns(request):
    title = _('Turkish Conjunction Maker - Nouns')
    code = 'from turkish_suffix_library.turkish import Turkish\n\n'
    show_code = request.GET.get('show_code', '') == 'on'
    proper_noun = request.GET.get('proper_noun', '') == 'on'
    noun = request.GET.get('noun', '')
    result = []

    if noun:
        for case in con.CASES:
            result.append({
                'case': case,
                'result': utils.get_noun_function(case, noun, proper_noun)
            })

            code += utils.get_noun_function(case, noun, proper_noun, show_code=True)

        history = History(
            noun=noun,
            proper_noun=proper_noun
        )

        history.save()

    possessive = {
        's1': utils.get_possessive_function(noun, proper_noun, 1, False, show_code=False),
        's2': utils.get_possessive_function(noun, proper_noun, 2, False, show_code=False),
        's3': utils.get_possessive_function(noun, proper_noun, 3, False, show_code=False),
        'p1': utils.get_possessive_function(noun, proper_noun, 1, True, show_code=False),
        'p2': utils.get_possessive_function(noun, proper_noun, 2, True, show_code=False),
        'p3': utils.get_possessive_function(noun, proper_noun, 3, True, show_code=False),
    }

    code += utils.get_possessive_function(noun, proper_noun, 1, False, show_code=True)
    code += utils.get_possessive_function(noun, proper_noun, 2, False, show_code=True)
    code += utils.get_possessive_function(noun, proper_noun, 3, False, show_code=True)
    code += utils.get_possessive_function(noun, proper_noun, 1, True, show_code=True)
    code += utils.get_possessive_function(noun, proper_noun, 2, True, show_code=True)
    code += utils.get_possessive_function(noun, proper_noun, 3, True, show_code=True)

    copulas = []

    for copula in con.COPULAS:
        copulas.append({
            'tense': copula,
            'conjunct': {
                's1p': utils.get_copula_function(copula, noun, proper_noun, 1, False, False, False, show_code=False),
                's2p': utils.get_copula_function(copula, noun, proper_noun, 2, False, False, False, show_code=False),
                's3p': utils.get_copula_function(copula, noun, proper_noun, 3, False, False, False, show_code=False),
                'p1p': utils.get_copula_function(copula, noun, proper_noun, 1, True, False, False, show_code=False),
                'p2p': utils.get_copula_function(copula, noun, proper_noun, 2, True, False, False, show_code=False),
                'p3p': utils.get_copula_function(copula, noun, proper_noun, 3, True, False, False, show_code=False),
                's1n': utils.get_copula_function(copula, noun, proper_noun, 1, False, False, True, show_code=False),
                's2n': utils.get_copula_function(copula, noun, proper_noun, 2, False, False, True, show_code=False),
                's3n': utils.get_copula_function(copula, noun, proper_noun, 3, False, False, True, show_code=False),
                'p1n': utils.get_copula_function(copula, noun, proper_noun, 1, True, False, True, show_code=False),
                'p2n': utils.get_copula_function(copula, noun, proper_noun, 2, True, False, True, show_code=False),
                'p3n': utils.get_copula_function(copula, noun, proper_noun, 3, True, False, True, show_code=False),
                's1pq': utils.get_copula_function(copula, noun, proper_noun, 1, False, True, False, show_code=False),
                's2pq': utils.get_copula_function(copula, noun, proper_noun, 2, False, True, False, show_code=False),
                's3pq': utils.get_copula_function(copula, noun, proper_noun, 3, False, True, False, show_code=False),
                'p1pq': utils.get_copula_function(copula, noun, proper_noun, 1, True, True, False, show_code=False),
                'p2pq': utils.get_copula_function(copula, noun, proper_noun, 2, True, True, False, show_code=False),
                'p3pq': utils.get_copula_function(copula, noun, proper_noun, 3, True, True, False, show_code=False),
                's1nq': utils.get_copula_function(copula, noun, proper_noun, 1, False, True, True, show_code=False),
                's2nq': utils.get_copula_function(copula, noun, proper_noun, 2, False, True, True, show_code=False),
                's3nq': utils.get_copula_function(copula, noun, proper_noun, 3, False, True, True, show_code=False),
                'p1nq': utils.get_copula_function(copula, noun, proper_noun, 1, True, True, True, show_code=False),
                'p2nq': utils.get_copula_function(copula, noun, proper_noun, 2, True, True, True, show_code=False),
                'p3nq': utils.get_copula_function(copula, noun, proper_noun, 3, True, True, True, show_code=False)
            }
        })

        code += utils.get_copula_function(copula, noun, proper_noun, 1, False, False, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 2, False, False, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 3, False, False, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 1, True, False, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 2, True, False, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 3, True, False, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 1, False, False, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 2, False, False, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 3, False, False, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 1, True, False, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 2, True, False, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 3, True, False, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 1, False, True, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 2, False, True, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 3, False, True, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 1, True, True, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 2, True, True, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 3, True, True, False, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 1, False, True, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 2, False, True, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 3, False, True, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 1, True, True, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 2, True, True, True, show_code=True)
        code += utils.get_copula_function(copula, noun, proper_noun, 3, True, True, True, show_code=True)

    return render(
        request,
        'nouns.html',
        {
            'title': title,
            'show_code': show_code,
            'proper_noun': proper_noun,
            'noun': noun,
            'code': code,
            'result': result,
            'possessive': possessive,
            'path': 'noun',
            'copulas': copulas
        }
    )


def home(request):
    code = 'from turkish_suffix_library.turkish import Turkish\n\n'
    show_code = request.GET.get('show_code', '') == 'on'

    if request.GET.get('english'):
        verb = request.GET.get('verb_english')
    else:
        verb = request.GET.get('verb')

    if verb:
        tense = _(utils.capitalize(request.GET.get('tense', '')))

        title = _('{tense} of the  verb {verb}').replace('{tense}', tense).replace('{verb}', verb)

        history = History(
            verb=verb,
            tense=request.GET.get('tense', ''),
            negative=request.GET.get('negative', '') == 'on',
            question=request.GET.get('question', '') == 'on',
            morph=request.GET.get('morph', ''),
            affix=request.GET.get('affix', '')
        )

        history.save()

        result = {
            's1': utils.get_verb_function(request, person=1),
            's2': utils.get_verb_function(request, person=2),
            's3': utils.get_verb_function(request, person=3),
            'p1': utils.get_verb_function(request, person=1, plural=True),
            'p2': utils.get_verb_function(request, person=2, plural=True),
            'p3': utils.get_verb_function(request, person=3, plural=True),
        }

        code += utils.get_verb_function(request, person=1, code=True)
        code += utils.get_verb_function(request, person=2, code=True)
        code += utils.get_verb_function(request, person=3, code=True)
        code += utils.get_verb_function(request, person=1, plural=True, code=True)
        code += utils.get_verb_function(request, person=2, plural=True, code=True)
        code += utils.get_verb_function(request, person=3, plural=True, code=True)

    else:
        result = []
        title = _('Turkish Conjunction Maker')

    return render(request, 'home.html', {
        'request': request,
        'result': result,
        'code': code,
        'show_code': show_code,
        'tenses': con.TENSES,
        'title': title,
        'path': 'verb',
        'vocabulary': ENGLISH_TO_TURKISH
    })


def example_verbs(request):
    title = _('Example verbs - Turkish Conjunction Maker')
    verb_list = {}
    verbs = []

    for verb in VERBS:
        if make_upper(verb[0]) not in verb_list:
            verb_list[make_upper(verb[0])] = []

        verb_list[make_upper(verb[0])].append(verb)

    for key in verb_list:
        verbs.append({
            'letter': make_upper(key),
            'verbs': verb_list[key]
        })

    return render(request, 'example_verbs.html', {
        'verbs': verbs,
        'path': 'verb',
        'title': title
    })


def conjunct_verb(request):
    verb = request.GET.get('verb')

    title = _('Conjunction of the verb {verb} in Turkish').replace('{verb}', verb)

    infinitive = utils.get_infinitive_case(verb, False)
    infinitive_negative = utils.get_infinitive_case(verb, True)

    return render(request, 'conjunct_verb.html', {
        'tenses': con.TENSES,
        'verb': verb,
        'title': title,
        'path': 'verb',
        'infinitive': infinitive,
        'infinitive_negative': infinitive_negative
    })


def conjunct_verb_slug(request, verb):
    verb_real = utils.tr_unslugify(verb)

    title = _('Conjunction of the verb {verb} in Turkish').replace('{verb}', verb_real)

    if verb_real in VERBS:
        file_name = os.path.join(settings.BASE_DIR, 'data', f'{verb}.json')
        conjunction_file = open(file_name, 'r')
        conjunction = json.load(conjunction_file)

        return render(request, 'conjunct_verb.html', {
            'tenses': con.TENSES,
            'verb': verb_real,
            'title': title,
            'path': 'verb',
            'conjunctions': conjunction
        })


def robots(request):
    text = 'Sitemap: https://trstem.com/sitemap.xml\n'
    text += 'User-agent: * Disallow: \n'
    return HttpResponse(text, content_type='text/plain; charset=utf8')


def sitemap(request):
    return render(request, 'sitemap.xml', content_type='application/xml; charset=utf8')

