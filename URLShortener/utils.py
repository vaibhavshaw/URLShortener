import random
import string


def generator(size=6, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def codeGenerator(instance, size=6):
    code = generator(size=size)
    Class = instance.__class__
    isCodeExist = Class.objects.filter(shortcode=code).exists()
    if isCodeExist:
        return codeGenerator(instance, size=size)
    return code
