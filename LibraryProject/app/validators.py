from django.core.exceptions import ValidationError

def validate_integer(value):
    if int(value) != value:
        raise ValidationError('Цена должна быть положительным числом')
    else:
        return value