from django import template
from turkish_suffix_library.turkish import Turkish

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value):
    value = value.replace('_', ' ')

    return value[0].upper() + value[1:]


@register.filter(name='person_1')
def person_1(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=1).to_string()


@register.filter(name='person_1_plural')
def person_1_plural(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=1, plural=True).to_string()


@register.filter(name='person_2')
def person_2(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=2).to_string()


@register.filter(name='person_2_plural')
def person_2_plural(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=2, plural=True).to_string()


@register.filter(name='person_3')
def person_3(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=3).to_string()


@register.filter(name='person_3_plural')
def person_3_plural(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=3, plural=True).to_string()


@register.filter(name='person_1_negative')
def person_1_negative(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=1, negative=True).to_string()


@register.filter(name='person_1_plural_negative')
def person_1_plural_negative(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=1, plural=True, negative=True).to_string()


@register.filter(name='person_2_negative')
def person_2_negative(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=2, negative=True).to_string()


@register.filter(name='person_2_plural_negative')
def person_2_plural_negative(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=2, plural=True, negative=True).to_string()


@register.filter(name='person_3_negative')
def person_3_negative(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=3, negative=True).to_string()


@register.filter(name='person_3_plural_negative')
def person_3_plural_negative(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=3, plural=True, negative=True).to_string()


@register.filter(name='person_1_q')
def person_1_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=1, question=True).to_string()


@register.filter(name='person_1_plural_q')
def person_1_plural_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=1, plural=True, question=True).to_string()


@register.filter(name='person_2_q')
def person_2_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=2, question=True).to_string()


@register.filter(name='person_2_plural_q')
def person_2_plural_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=2, plural=True, question=True).to_string()


@register.filter(name='person_3_q')
def person_3_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=3, question=True).to_string()


@register.filter(name='person_3_plural_q')
def person_3_plural_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=3, plural=True, question=True).to_string()


@register.filter(name='person_1_negative_q')
def person_1_negative_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=1, negative=True, question=True).to_string()


@register.filter(name='person_1_plural_negative_q')
def person_1_plural_negative_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=1, plural=True, negative=True, question=True).to_string()


@register.filter(name='person_2_negative_q')
def person_2_negative(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=2, negative=True, question=True).to_string()


@register.filter(name='person_2_plural_negative_q')
def person_2_plural_negative_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=2, plural=True, negative=True, question=True).to_string()


@register.filter(name='person_3_negative_q')
def person_3_negative_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=3, negative=True, question=True).to_string()


@register.filter(name='person_3_plural_negative_q')
def person_3_plural_negative_q(verb, tense):
    func = Turkish(verb)
    return func.__getattribute__(tense)(person=3, plural=True, negative=True, question=True).to_string()

