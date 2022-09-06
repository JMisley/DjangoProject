from django.shortcuts import render
import random


def index(request):
    return render(request, 'pw/index.html')


def result(request):
    generated_passwords = ''
    length = int(request.GET.get('length', 8))
    has_uppercase = request.GET.get('uppercaseCheckbox')
    has_numbers = request.GET.get('numbersCheckbox')
    has_special = request.GET.get('specialCheckbox')

    password_list = list('abcdefghijklmnopqrstuvwxyz')

    if has_uppercase:
        password_list.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if has_numbers:
        password_list.extend('1234567890')
    if has_special:
        password_list.extend('`~!@#$%^&*()-_+=[]{}|\\:;\"\'/?.>,<')

    for x in range(10):
        password = ''
        for y in range(length):
            password += random.choice(password_list)
        generated_passwords += password + '\n'

    return render(request, 'pw/result.html',
                  context={'length': length, 'generated_password': generated_passwords, 'list': password_list})
