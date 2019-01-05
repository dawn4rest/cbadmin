import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from utils.decorators import login_required
from django.db.models import Count, Q

from .models import Post, Category
from .forms import PostForm
from comment import models as comment_models
from comment import forms as comment_forms


def search(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort','')
    posts = Post.objects.filter(Q(title__icontains=q) | Q(tag__icontains=q))

    if sort == 'likes':
        posts = posts.annotate(like_count = Count('like_users')).order_by('-like_count')
    elif sort == 'new':
        posts = posts.all().order_by('-created_at')
    elif sort == 'views':
        posts = posts.all().order_by('-view_count')
    elif sort == 'comments':
        posts = Post.objects.annotate(count = Count('comment')).order_by('-count')
    else:
        posts = posts.all().order_by('-updated_at')

    context = {'posts' : posts, 'q' : q}
    return render(request, 'post/search.html', context)


def post_list(request):
    # author, author_id, background, category, category_id, con_title, concomment, created_at,
    # id, like_users, photo, pro_title, procomment, share_count, tag, thumbnail, title, updated_at, view_count
    sort = request.GET.get('sort','')
    categories = Category.objects.all()

    if sort == 'likes':
        posts = Post.objects.annotate(like_count = Count('like_users')).order_by('-like_count')
    elif sort == 'new':
        posts = Post.objects.all().order_by('-updated_at')
    elif sort == 'views':
        posts = Post.objects.all().order_by('-view_count')
    elif sort == 'comments':
        posts = Post.objects.annotate(count = Count('comment')).order_by('-count')
    else:
        posts = Post.objects.all().order_by('-created_at')

    context = {'posts' : posts, 'categories': categories}
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    procomments = comment_models.Comment.objects.filter(post=post, type=True).order_by('-created_at')
    procomments_mine = procomments.filter(author=request.user).order_by('-created_at')
    procomments_exclude = procomments.exclude(author=request.user).order_by('-created_at')
    concomments = comment_models.Comment.objects.filter(post=post, type=False).order_by('-created_at')
    concomments_mine = concomments.filter(author=request.user).order_by('-created_at')
    concomments_exclude = concomments.exclude(author=request.user).order_by('-created_at')
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

            messages.success(request, '게시물이 등록되었습니다')
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
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_detail', post_pk=post_pk)
    else:
        if request.method == 'POST':
            post_form = PostForm(request.POST, request.FILES, instance=post)

            if post_form.is_valid():
                post = post_form.save()

                messages.success(request, '게시물이 수정되었습니다')
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
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, '게시물이 삭제되었습니다.')
        return redirect('post:post_list')


def show_category(request,hierarchy= None):
    categories = Category.objects.all()
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None

    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Post, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "post-detail.html", {'instance':instance,'breadcrumbs':breadcrumbs})

    return render(request, "post/category_list.html", {
        'post_set':parent.post_set.all(),
        'sub_categories':parent.children.all(),
        'categories': categories,
    })


@login_required
def add_share_count(request, post_pk):
    target = get_object_or_404(Post, pk=post_pk)
    target.share_count = target.share_count + 1
    target.save()
    return redirect('post:post_detail', post_pk=post_pk)


@login_required
def post_like_toggle(request, post_pk):
    # GET파라미터로 전달된 이동할 URL
    next_path = request.GET.get('next')
    # post_pk에 해당하는 Post객체
    post = get_object_or_404(Post, pk=post_pk)
    # 요청한 사용자
    user = request.user

    # 사용자의 like_posts목록에서 like_toggle할 Post가 있는지 확인
    filtered_like_posts = user.like_posts.filter(pk=post.pk)
    # 존재할경우, like_posts목록에서 해당 Post를 삭제
    if filtered_like_posts.exists():
        user.like_posts.remove(post)
        messages.success(request, '해당 게시물 좋아요 취소')
    else:
        user.like_posts.add(post)
        messages.success(request, '게시물 좋아요 성공')

    # 이동할 path가 존재할 경우 해당 위치로, 없을 경우 Post상세페이지로 이동
    if next_path:
        return redirect(next_path)
    return redirect('post:post_detail', post_pk=post_pk)
