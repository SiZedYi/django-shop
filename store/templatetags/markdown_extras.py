from django import template
from markdown.extensions.toc import TocExtension
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=[TocExtension(permalink=True)])