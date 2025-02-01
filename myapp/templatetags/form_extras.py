from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={"class": css})
    return field  # or return an error message or just return field as-is
