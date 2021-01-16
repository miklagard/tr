from turkish_suffix_library.turkish import Turkish


def get_verb_function(request, **kwargs):
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


def capitalize(value):
    value = value.replace('_', ' ')

    return value[0].upper() + value[1:]