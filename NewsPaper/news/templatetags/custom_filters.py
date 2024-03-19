import re
from django import template
from django.core.exceptions import ValidationError


register = template.Library()

BAD_WORD_PATTERNS = ["дур\w*", "дебил\w*", "урод\w*"]


@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        for pattern in BAD_WORD_PATTERNS:
            regex = re.compile(pattern, re.IGNORECASE)
            value = regex.sub(lambda m: m.group(0)[0] + '*' * (len(m.group(0)) - 1), value)
    else:
        raise ValidationError("custom_filter can only be applied to strings.")
    return value

