from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from itertools import chain
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)

from .models import ContactChat
from .forms import LoginForm, SignupForm, ProfileForm, ContactChatForm
from post import models as post_models
from comment import models as comment_models


def login(request):
    if request.method == 'POST':
        # 로그인 성공 후 이동할 URL. 주어지지 않으면 None
        next = request.GET.get('next')

        # Data bounded form인스턴스 생성
        # AuthenticationForm의 첫 번째 인수는 해당 request가 되어야 한다
        login_form = LoginForm(request=request, data=request.POST)

        # 유효성 검증에 성공할 경우
        # AuthenticationForm을 사용하면 authenticate과정까지 완료되어야 유효성 검증을 통과한다
        if login_form.is_valid():
            # AuthenticatonForm에서 인증(authenticate)에 성공한 유저를 가져오려면 이 메서드를 사용한다
            user = login_form.get_user()
            # Django의 auth앱에서 제공하는 login함수를 실행해 앞으로의 요청/응답에 세션을 유지한다
            django_login(request, user)
            # next가 존재하면 해당 위치로, 없으면 Post목록 화면으로 이동
            return redirect(next if next else 'post:post_list')
        # 인증에 실패하면 login_form에 non_field_error를 추가한다
        login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }
    return render(request, 'member/login.html', context)


@login_required
def logout(request):
    django_logout(request)
    return redirect('post:post_list')


def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST, files=request.FILES)
        # 유효성 검증에 통과한 경우 (username의 중복과 password1, 2의 일치 여부)
        if signup_form.is_valid():
            # 유저를 생성 후 해당 User를 로그인 시킨다
            user = signup_form.save()
            django_login(request, user)
            return redirect('post:post_list')
    else:
        signup_form = SignupForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'member/signup.html', context)


@login_required
def my_page(request):
    user = request.user
    chats = ContactChat.objects.filter(owner=user)
    chat_form = ContactChatForm()

    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, files=request.FILES, instance=user)

        if profile_form.is_valid():
            user = profile_form.save()
            django_login(request, user)
            messages.success(request, '프로필이 수정되었습니다')
            return redirect('member:my_page')
    else:
        profile_form = ProfileForm(instance=user)

    context = {
        'user': user,
        'chats': chats,
        'profile_form': profile_form,
        'chat_form': chat_form,
    }
    return render(request, 'member/my_page.html', context)


@login_required
def password_change(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호가 정상적으로 변경되었습니다.')
            return redirect('member:my_page')
        else:
            messages.error(request, '오류가 발생하였습니다.')
    else:
        password_form = PasswordChangeForm(request.user)

    context = {
        'password_form': password_form,
    }
    return render(request, 'member/password_change.html', context)


@login_required
def user_delete(request):
    user = request.user

    if request.method == 'POST':
        user.delete()
        messages.success(request, '사용자가 삭제되었습니다.')
        return redirect('member:my_page')
    else:
        messages.error(request, '오류가 발생하였습니다.')
        return redirect('member:my_page')


@login_required
def user_log(request):
    user = request.user
    sort = request.GET.get('sort', '')

    if sort == 'my_comments':
        comments_pro = comment_models.Comment.objects.filter(
            author=user, type=True)  # 내가 만든 찬성의견
        comments_con = comment_models.Comment.objects.filter(
            author=user, type=False)  # 내가 만든 반대의견
        comments_sorted = sorted(
            chain(comments_pro, comments_con), key=lambda instance: instance.created_at)
        log_sorted = comments_sorted
        context = {'comments_pro': comments_pro, 'comments_con': comments_con,
                   'comments_sorted': comments_sorted, 'log_sorted': log_sorted, 'sort': sort, }
        return render(request, 'member/log.html', context)
    elif sort == 'like_hate':
        likes_pro = user.like_comments.filter(type=True)  # 추천한 찬성 의견
        hates_pro = user.hate_comments.filter(type=True)  # 반대한 찬성 의견
        likes_con = user.like_comments.filter(type=False)  # 추천한 반대 의견
        hates_con = user.hate_comments.filter(type=False)  # 반대한 반대 의견
        lh_sorted = sorted(chain(likes_pro, hates_pro, likes_con,
                                 hates_con), key=lambda instance: instance.created_at)
        log_sorted = lh_sorted
        context = {'likes_pro': likes_pro, 'hates_pro': hates_pro, 'likes_con': likes_con,
                   'hates_con': hates_con, 'lh_sorted': lh_sorted, 'log_sorted': log_sorted, 'sort': sort, }
        return render(request, 'member/log.html', context)
    else:
        posts_log = post_models.Post.objects.filter(author=user)  # 내가 만든 채터박스
        log_sorted = posts_log
        context = {'posts_log': posts_log,
                   'log_sorted': log_sorted, 'sort': sort, }
    return render(request, 'member/log.html', context)


@login_required
def contact(request):
    user = request.user
    chats = ContactChat.objects.filter(owner=user)
    chat_form = ContactChatForm()

    context = {
        'user': user,
        'chats': chats,
        'chat_form': chat_form,
    }
    return render(request, 'member/contact.html', context)


@login_required
def create_chat(request):
    user = request.user

    if request.method == 'POST':
        chat_form = ContactChatForm(request.POST)
        if chat_form.is_valid():
            chat = chat_form.save(commit=False)
            chat.owner = request.user
            chat.author = request.user
            chat.save()
            return redirect('member:my_page')
        else:
            return redirect('member:my_page')


@login_required
def get_liked_posts(request):
    user = request.user
    liked_posts = user.like_posts.all()

    context = {
        'liked_posts': liked_posts,
    }
    return render(request, 'include/slide_menu.html', context)
