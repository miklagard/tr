from django.shortcuts import render
from turkish_suffix_library.turkish import Turkish


def get_function(request, **kwargs):
    verb = request.POST.get('verb', '')
    tense = request.POST.get('tense', '')
    negative = request.POST.get('negative', '') == 'on'
    question = request.POST.get('question', '') == 'on'
    morph = request.POST.get('morph', '')
    affix = request.POST.get('affix', '')

    if verb:
        func = Turkish(verb)

        if morph == 'passive':
            func = func.passive()

        if affix:
            func = func.unify_verbs(auxiliary=affix, negative=negative)

        func = {
            'pt': func.present_simple,
            'pct': func.present_continuous,
            'pct2': func.present_continuous_alternative,
            'pat': func.past,
            'ft': func.future,
            'lpt': func.learned_past,
            'lptlpt': func.learned_past_learned_past,
        }.get(tense)

        if func:
            return func(
                negative=negative,
                question=question,
                person=kwargs.get('person', 1),
                plural=kwargs.get('plural', False)
            ).to_string()
    else:
        return None


def home(request):
    if request.POST:
        result = {
            's1': get_function(request, person=1),
            's2': get_function(request, person=2),
            's3': get_function(request, person=3),
            'p1': get_function(request, person=1, plural=True),
            'p2': get_function(request, person=2, plural=True),
            'p3': get_function(request, person=3, plural=True),
        }
    else:
        result = []

    return render(request, 'home.html', {
        'request': request.POST,
        'result': result
    })
