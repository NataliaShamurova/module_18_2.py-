from django.shortcuts import render
from .forms import UserRegister

# Псевдо-список существующих пользователей
users = ['user1', 'user2', 'admin']


def sign_up_by_django(request):
    info = ''

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info = "Ошибка: пользователь уже существует."
            elif password != repeat_password:
                info = "Ошибка: пароли не совпадают."
            elif age < 18:
                info = "Ошибка: возраст должен быть не менее 18 лет."
            else:
                users.append(username)  # Добавление нового пользователя в псевдо-список
                info = f"Приветствуем, {username}!"

    else:
        form = UserRegister()

    context = {'form': form, 'info': info}
    return render(request, 'fifth_task/registration_page.html', context)


from django.shortcuts import render


def sign_up_by_html(request):
    info = ''  # Пустая строка для информации

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверка условий
        if username in users:
            info = "Ошибка: пользователь уже существует."
        elif password != repeat_password:
            info = "Ошибка: пароли не совпадают."
        elif int(age) < 18:  # Приводим к int для проверки возраста
            info = "Ошибка: возраст должен быть не менее 18 лет."
        else:
            users.append(username)  # Добавление нового пользователя в список
            info = f"Приветствуем, {username}!"  # Успешное сообщение

    context = {'info': info}  # Передаем информацию в шаблон
    return render(request, 'fifth_task/registration_page.html', context)  # Отображение шаблона

    return sign_up_by_django(request)  # Используем то же представление
