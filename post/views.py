import json
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from utils.decorators import login_required
from django.db.models import Count, Q, Func, F

from .models import Post, Category
from .forms import PostForm
from comment import models as comment_models
from comment import forms as comment_forms


def search(request):
    q = request.GET.get('q', '')
    posts = Post.objects.filter(Q(title__icontains=q) | Q(tag__icontains=q))

    context = {'posts': posts, 'q': q, }
    return render(request, 'post/search.html', context)


def show_category(request, hierarchy=None):
    sort = request.GET.get('sort', '')
    categories = Category.objects.all()
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [x.slug for x in category_queryset]
    parent = None

    for slug in category_slug:
        if slug in all_slugs:
            target = slug
            parent = get_object_or_404(Category, slug=slug, parent=parent)

            if sort == 'likes':
                post_set = parent.post_set.annotate(
                    like_count=Count('like_users')).order_by('-like_count')
            elif sort == 'new':
                post_set = parent.post_set.all().order_by('-created_at')
            elif sort == 'views':
                post_set = parent.post_set.all().order_by('-view_count')
            elif sort == 'comments':
                post_set = parent.post_set.annotate(
                    count=Count('comment')).order_by('-count')
            else:
                post_set = parent.post_set.all().order_by('-created_at')

        else:
            instance = get_object_or_404(Post, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-'))
                             for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "post-detail.html", {'instance': instance, 'breadcrumbs': breadcrumbs})

    return render(request, "post/category_list.html", {
        'post_set': post_set,
        'sub_categories': parent.children.all(),
        'categories': categories,
        'target': target,
        'sort': sort,
    })


def post_list(request):
    sort = request.GET.get('sort', '')
    categories = Category.objects.all()

    if sort == 'likes':
        posts = Post.objects.annotate(like_count=Count(
            'like_users')).order_by('-like_count')
    elif sort == 'vs':
        posts = Post.objects.annotate(vs_abs=Count('comment', filter=Q(comment__type=True))-Count(
            'comment', filter=Q(comment__type=False))).order_by('-vs_abs')
    elif sort == 'views':
        posts = Post.objects.all().order_by('-view_count')
    elif sort == 'comments':
        posts = Post.objects.annotate(
            count=Count('comment')).order_by('-count')
    else:
        posts = Post.objects.all().order_by('-created_at')

    context = {'posts': posts, 'categories': categories, 'sort': sort, }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    procomments = comment_models.Comment.objects.filter(
        post=post, type=True).order_by('-created_at')
    concomments = comment_models.Comment.objects.filter(
        post=post, type=False).order_by('-created_at')

    if request.user.is_authenticated():
        procomments_mine = procomments.filter(
            author=request.user).order_by('-created_at')
        procomments_exclude = procomments.exclude(
            author=request.user).order_by('-created_at')
        concomments_mine = concomments.filter(
            author=request.user).order_by('-created_at')
        concomments_exclude = concomments.exclude(
            author=request.user).order_by('-created_at')
    else:
        procomments_mine = None
        procomments_exclude = procomments
        concomments_mine = None
        concomments_exclude = concomments

    comment_form = comment_forms.CommentForm()
    comment_on_comment_form = comment_forms.CommentOnCommentForm()
    report_comment_form = comment_forms.ReportCommentForm()

    post.view_count = post.view_count + 1
    post.save()

    context = {
        'post': post,
        'procomments_mine': procomments_mine,
        'procomments_exclude': procomments_exclude,
        'concomments_mine': concomments_mine,
        'concomments_exclude': concomments_exclude,
        'comment_form': comment_form,
        'comment_on_comment_form': comment_on_comment_form,
        'report_comment_form': report_comment_form,
    }
    return render(request, 'post/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(
                request, '<h4>새로운 채터박스가 만들어졌어요!</h4><p>성공적으로 채터박스가 만들어졌습니다.</p><p>익명으로 많은 사람들에게 공유하고 의견을 받아보세요.</p>')
            return redirect('post:post_detail', post_pk=post.pk)
    else:
        post_form = PostForm()

    context = {
        'post_form': post_form,
    }
    return render(request, 'post/post_create.html', context)


@login_required
def post_update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if post.author != request.user:
        return redirect('post:post_detail', post_pk=post_pk)
    else:
        if request.method == 'POST':
            post_form = PostForm(request.POST, request.FILES, instance=post)

            if post_form.is_valid():
                post = post_form.save()
                messages.success(
                    request, '<h4>채터박스를 수정했어요!</h4><p>성공적으로 채터박스를 수정하셨습니다.</p><p>익명으로 많은 사람들에게 공유하고 의견을 받아보세요.</p>')
                return redirect('post:post_detail', post_pk=post_pk)
        else:
            post_form = PostForm(instance=post)

    context = {
        'post': post,
        'post_form': post_form,
    }
    return render(request, 'post/post_update.html', context)


@login_required
def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if post.author != request.user or request.method == 'GET':
        return redirect('post:post_list')

    if request.method == 'POST':
        post.delete()
        messages.success(
            request, '<h4>채터박스를 삭제했어요.</h4><p>성공적으로 채터박스를 삭제하셨습니다.</p><p>새로운 채터박스를 기다릴게요!</p>')
        return redirect('post:post_list')


@login_required
def add_share_count(request, post_pk):
    target = get_object_or_404(Post, pk=post_pk)
    target.share_count = target.share_count + 1
    target.save()
    return redirect('post:post_detail', post_pk=post_pk)


@login_required
def post_like_toggle(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    user = request.user

    filtered_like_posts = user.like_posts.filter(pk=post.pk)
    if filtered_like_posts.exists():
        user.like_posts.remove(post)
    else:
        user.like_posts.add(post)
        messages.success(
            request, '<h4>"좋아요"를 누르셨어요!</h4><p>언제든  ♥좋아요 목록에서 확인하실 수 있어요.</p>')

    return redirect('post:post_detail', post_pk=post_pk)
