from django.shortcuts import render
from turkish_suffix_library.turkish import Turkish
from turkish_suffix_library.sample_verbs_list import VERBS
from ui.models import History

def get_function(request, **kwargs):
    verb = request.GET.get('verb', '')
    tense = request.GET.get('tense', '')
    negative = request.GET.get('negative', '') == 'on'
    question = request.GET.get('question', '') == 'on'
    morph = request.GET.get('morph', '')
    affix = request.GET.get('affix', '')
    code = f"Turkish('{verb}')"

    person = kwargs.get('person', 1)
    plural = kwargs.get('plural', False)

    if verb:
        func = Turkish(verb)

        if morph == 'passive':
            func = func.passive()

        if affix:
            func = func.unify_verbs(auxiliary=affix, negative=negative)
            code += f".unify_verbs(auxiliary='{affix}', negative={negative})"

        func_method = {
            'pt': 'present_simple',
            'pct': 'present_continuous',
            'pct2': 'present_continuous_alternative',
            'pat': 'past',
            'ft': 'future',
            'lpt': 'learned_past',
            'lptlpt': 'learned_past_learned_past',
        }.get(tense)

        if func:
            func = func.__getattribute__(func_method)

            code += f".{func_method}(negative={negative}, question={question}, person={person}, plural={plural})"
            code = f"print({code})\n"

            if kwargs.get('code'):
                return code
            else:
                return func(
                    negative=negative,
                    question=question,
                    person=kwargs.get('person', person),
                    plural=kwargs.get('plural', plural),
                ).to_string()
    else:
        return None


def home(request):
    code = 'from turkish_suffix_library.turkish import Turkish\n\n'
    show_code = request.GET.get('show_code', '') == 'on'

    if request.GET:
        if request.GET.get('verb'):

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
                's1': get_function(request, person=1),
                's2': get_function(request, person=2),
                's3': get_function(request, person=3),
                'p1': get_function(request, person=1, plural=True),
                'p2': get_function(request, person=2, plural=True),
                'p3': get_function(request, person=3, plural=True),
            }

            code += get_function(request, person=1, code=True)
            code += get_function(request, person=2, code=True)
            code += get_function(request, person=3, code=True)
            code += get_function(request, person=1, plural=True, code=True)
            code += get_function(request, person=2, plural=True, code=True)
            code += get_function(request, person=3, plural=True, code=True)
        else:
            result = []
    else:
        result = []

    return render(request, 'home.html', {
        'request': request.GET,
        'result': result,
        'code': code,
        'show_code': show_code
    })
