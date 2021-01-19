from turkish_suffix_library.turkish import Turkish
import ui.consonants as con


def get_noun_function(case, noun, proper_noun, show_code=False):
    code = f"Turkish('{noun}')"

    if noun:
        func = Turkish(noun)
        func = func.__getattribute__(case)(proper_noun=proper_noun)

        code += f".{case}(proper_noun={proper_noun})"
        code = f"print({code})\n"

        if show_code:
            return code
        else:
            return func.to_string()
    else:
        return ''


def get_possessive_function(noun, proper_noun, person, plural, show_code=False):
    code = f"Turkish('{noun}')"
    case = 'possessive'

    if noun:
        func = Turkish(noun)
        func = func.__getattribute__(case)(person=person, plural=plural, proper_noun=proper_noun)

        code += f".{case}(person={person}, plural={plural}, proper_noun={proper_noun})"
        code = f"print({code})\n"

        if show_code:
            return code
        else:
            return func.to_string()
    else:
        return ''


def get_infinitive_case(verb, negative):
    return Turkish(verb).infinitive(negative=negative).to_string()

def get_verb_function(request, **kwargs):
    if request.GET.get('english'):
        verb = request.GET.get('verb_english', '')
    else:
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

        if tense in con.TENSES:
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


def capitalize(value):
    value = value.replace('_', ' ')

    return value[0].upper() + value[1:]


def tr_slugify(word):
    return word.replace(' ', '__').replace('ı', 'i_').replace('ş', 's_').replace('ü', 'u_')\
        .replace('ğ', 'g_').replace('ö', 'o_').replace('ç', 'c_')


def tr_unslugify(word):
    return word.replace('__', ' ').replace('i_', 'ı').replace('s_', 'ş').replace('u_', 'ü')\
        .replace('g_', 'ğ').replace('o_', 'ö').replace('c_', 'ç')
