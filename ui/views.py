from django.shortcuts import render
from turkish_suffix_library.sample_verbs_list import VERBS
from ui.utils import get_verb_function, get_noun_function, capitalize
from ui.models import History
import ui.consonants as con


def nouns(request):
    title = 'Turkish Conjunction Maker - Nouns'
    code = 'from turkish_suffix_library.turkish import Turkish\n\n'
    show_code = request.GET.get('show_code', '') == 'on'
    proper_noun = request.GET.get('proper_noun', '') == 'on'
    noun = request.GET.get('noun', '')
    print(proper_noun)
    result = []

    if noun:
        for case in con.CASES:
            result.append({
                'case': case,
                'result': get_noun_function(case, noun, proper_noun)
            })

    return render(
        request,
        'nouns.html',
        {
            'title': title,
            'show_code': show_code,
            'proper_noun': proper_noun,
            'noun': noun,
            'code': code,
            'result': result
        }
    )


def home(request):
    code = 'from turkish_suffix_library.turkish import Turkish\n\n'
    show_code = request.GET.get('show_code', '') == 'on'

    if request.GET.get('verb'):

        title = capitalize(request.GET.get('tense', ''))
        title += ' of verb '
        title += request.GET.get('verb')

        history = History(
            verb=request.GET.get('verb', ''),
            tense=request.GET.get('tense', ''),
            negative=request.GET.get('negative', '') == 'on',
            question=request.GET.get('question', '') == 'on',
            morph=request.GET.get('morph', ''),
            affix=request.GET.get('affix', '')
        )

        history.save()

        result = {
            's1': get_verb_function(request, person=1),
            's2': get_verb_function(request, person=2),
            's3': get_verb_function(request, person=3),
            'p1': get_verb_function(request, person=1, plural=True),
            'p2': get_verb_function(request, person=2, plural=True),
            'p3': get_verb_function(request, person=3, plural=True),
        }

        code += get_verb_function(request, person=1, code=True)
        code += get_verb_function(request, person=2, code=True)
        code += get_verb_function(request, person=3, code=True)
        code += get_verb_function(request, person=1, plural=True, code=True)
        code += get_verb_function(request, person=2, plural=True, code=True)
        code += get_verb_function(request, person=3, plural=True, code=True)
    else:
        result = []
        title = 'Turkish Conjunction Maker'

    return render(request, 'home.html', {
        'request': request.GET,
        'result': result,
        'code': code,
        'show_code': show_code,
        'tenses': con.TENSES,
        'title': title
    })


def example_verbs(request):
    return render(request, 'example_verbs.html', {
        'verbs': VERBS
    })


def conjunct_verb(request):
    verb = request.GET.get('verb')

    title = f'Conjunction of the verb {verb} in Turkish'

    return render(request, 'conjunct_verb.html', {
        'tenses': con.TENSES,
        'verb': verb,
        'title': title
    })
