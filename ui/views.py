from django.shortcuts import render
from turkish_suffix_library.turkish import Turkish
from turkish_suffix_library.sample_verbs_list import VERBS
from ui.models import History


TENSES = (
    'imperative_mood',
    'present_continuous_simple',
    'simple_tense',
    'past_definite',
    'past_progressive_dubitative',
    'past_progressive_alternative_dubitative',
    'indefinite_past',
    'past_progressive_narrative',
    'past_progressive_alternative_narrative',
    'past_perfect_narrative',
    'doubtful_distant_past',
    'past_in_the_future',
    'past_conditional_narrative',
    'past_conditional_dubitative',
    'future_simple',
    'future_in_the_past',
    'future_dubitative',
    'future_conditional',
    'necessitative_mood_simple_tense',
    'necessitative_past_narrative',
    'necessitative_past_dubitative',
    'conditional_mood_simple_tense',
    'subjunctive_mood_simple_tense',
    'past_definite_narrative',
    'past_indefinite_past',
    'indefinite_past_future',
    'past_future'
)


def capitilize(value):
    value = value.replace('_', ' ')

    return value[0].upper() + value[1:]


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

    if verb.lower().endswith('mek') or verb.lower().endswith('mak'):
        verb = verb[0:-3]

    if verb:
        func = Turkish(verb)

        if morph == 'passive':
            code += '.passive()'
            func = func.passive()

        if affix:
            func = func.unify_verbs(auxiliary=affix, negative=negative)
            code += f".unify_verbs(auxiliary='{affix}', negative={negative})"

        if tense in TENSES:
            func_method = tense

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

            title = capitilize(request.GET.get('tense', ''))
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
            title = 'Turkish Conjunction Maker'
    else:
        title = 'Turkish Conjunction Maker'
        result = []

    return render(request, 'home.html', {
        'request': request.GET,
        'result': result,
        'code': code,
        'show_code': show_code,
        'tenses': TENSES,
        'title': title
    })


def example_verbs(request):
    return render(request, 'example_verbs.html', {
        'verbs': VERBS
    })


def conjunct_verb(request):
    conjunctions = {}

    verb = request.GET.get('verb')

    title = f'Conjunction of the verb {verb} in Turkish'

    return render(request, 'conjunct_verb.html', {
        'tenses': TENSES,
        'verb': verb,
        'title': title
    })
