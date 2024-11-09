from django import template

register = template.Library()

@register.filter
def add_class(field, class_name):
    """
    Adds the provided CSS class to the form field's widget.
    """
    return field.as_widget(attrs={'class': class_name})