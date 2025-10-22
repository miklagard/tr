from django import template
from ui.utils import tr_slugify
from django.utils.translation import gettext as _
from django.utils import translation
from django.urls import resolve, reverse
from django.urls import translate_url


register = template.Library()


@register.filter(name='tr_slugify')
def tr_slugify_func(value):
    return tr_slugify(value)


@register.filter(name='capitalize')
def capitalize(value):
    value = value.replace('_', ' ')

    return _(value[0].upper() + value[1:])


@register.filter(name='switch_language')
def switch_language(path):
    current_lang = translation.get_language()
    new_lang = 'tr' if current_lang == 'en' else 'en'

    # Mevcut view'ı al
    try:
        match = resolve(path)
        url_name = match.url_name
        kwargs = match.kwargs

        # Yeni dilde URL oluştur
        with translation.override(new_lang):
            return reverse(url_name, kwargs=kwargs)
    except:
        # Fallback: sadece dil prefix'ini değiştir
        if path.startswith(f'/{current_lang}/'):
            return path.replace(f'/{current_lang}/', f'/{new_lang}/', 1)
        else:
            return f'/{new_lang}{path}'


@register.filter(name='get_language')
def get_language(value):
    if value.startswith('/tr/'):
        return 'en'
    else:
        return 'tr'


@register.simple_tag(takes_context=True)
def get_switch_language_url(context, lang_code):
    request = context.get('request')
    if not request:
        return ''

    # Mevcut URL'i al ve dilini değiştir
    current_path = request.get_full_path()
    return translate_url(current_path, lang_code)

@register.simple_tag
def switch_language_url(path, lang_code):
    """Path ve lang_code alarak URL oluşturur"""
    return translate_url(path, lang_code)