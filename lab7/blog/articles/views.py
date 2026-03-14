from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

from articles.models import Article


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, "article.html", {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            # Проверка на уникальность названия
            if Article.objects.filter(title=form['title']).exists():
                form['errors'] = "Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form})
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # если поля заполнены без ошибок
                article = Article.objects.create(text=form["text"],
                                                 title=form["title"],
                                                 author=request.user)
                return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def registration(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password1 = request.POST.get("password1", "").strip()
        password2 = request.POST.get("password2", "").strip()

        form = {
            "username": username
        }

        # 1. Проверка на пустые поля
        if not username or not password1 or not password2:
            form["errors"] = "Все поля должны быть заполнены"
            return render(request, "registration.html", {"form": form})

        # 2. Проверка совпадения паролей
        if password1 != password2:
            form["errors"] = "Пароли не совпадают"
            return render(request, "registration.html", {"form": form})

        # 3. Проверка уникальности username
        if User.objects.filter(username=username).exists():
            form["errors"] = "Пользователь с таким именем уже существует"
            return render(request, "registration.html", {"form": form})

        # 4. Создание пользователя
        User.objects.create_user(
            username=username,
            password=password1
        )

        # после регистрации сразу на главную
        return redirect("archive")

    return render(request, "registration.html")


def login(request):
    if request.method == "POST":

        form = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password")
        }
        # проверка на пустые поля
        if not form["username"] or not form["password"]:
            form["error"] = "Заполните все поля"
            return render(request, "login.html", {"form": form})
        # аутентификация
        user = authenticate(
            request,
            username=form["username"],
            password=form["password"]
        )
        # если пользователь найден
        if user is not None:
            login_user(request, user)
            return redirect("archive")  # куда перекинуть после входа
        # если неверный логин/пароль
        else:
            form["error"] = "Нет аккаунта с таким сочетанием логина и пароля"
            return render(request, "login.html", {"form": form})
    # GET запрос
    return render(request, "login.html", {})