import markdown
import bleach
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def markdown_format(value):
    return markdown.markdown(value, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'])

@register.filter
@stringfilter
def markdown_remove(value):
    html_content = markdown.markdown(value)
    return bleach.clean(html_content, tags=[], strip=True)