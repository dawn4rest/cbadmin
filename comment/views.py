import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from utils.decorators import login_required
from django.db.models import Count, Q

from .models import ProComment, ConComment
from .forms import ProCommentForm, ConCommentForm, CommentOnProCommentForm, CommentOnConCommentForm, ReportProCommentForm, ReportConCommentForm
from post import models as post_models


def pro_comment_detail(request, comment_pk):
    pro_comment = get_object_or_404(ProComment, pk=comment_pk)
    comment = pro_comment

    return render(request, 'include/pro_comment.html', {'comment': comment})


def con_comment_detail(request, comment_pk):
    con_comment = get_object_or_404(ConComment, pk=comment_pk)
    comment = con_comment

    return render(request, 'include/con_comment.html', {'comment': comment})


@login_required
def pro_comment_create(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(post_models.Post, pk=post_pk)
        pro_comment_form = ProCommentForm(request.POST)

        if pro_comment_form.is_valid():
            pro_comment = pro_comment_form.save(commit=False)
            pro_comment.post = post
            pro_comment.author = request.user
            pro_comment.save()

            comment = pro_comment
            return render(request, 'include/pro_comment.html', {'comment': comment})
        else:
            error_msg = '댓글 등록에 실패했습니다\n{}'.format(
                '\n'.join(
                    [f'- {error}'
                     for key, value in pro_comment_form.errors.items()
                     for error in value]))
            messages.error(request, error_msg)

    return redirect('post:post_detail', post_pk=post_pk)


def con_comment_create(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(post_models.Post, pk=post_pk)
        con_comment_form = ConCommentForm(request.POST)

        if con_comment_form.is_valid():
            con_comment = con_comment_form.save(commit=False)
            con_comment.post = post
            con_comment.author = request.user
            con_comment.save()

            comment = con_comment
            return render(request, 'include/con_comment.html', {'comment': comment, 'post': post})
        else:
            error_msg = '댓글 등록에 실패했습니다\n{}'.format(
                '\n'.join(
                    [f'- {error}'
                     for key, value in con_comment_form.errors.items()
                     for error in value]))
            messages.error(request, error_msg)

    return redirect('post:post_detail', post_pk=post_pk)


@login_required
def pro_comment_update(request, comment_pk):
    pro_comment = get_object_or_404(ProComment, pk=comment_pk)
    post_pk = pro_comment.post.pk

    if pro_comment.author != request.user:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_detail', post_pk=post_pk)
    else:
        if request.method == 'POST':
            pro_comment_form = ProCommentForm(request.POST, request.FILES, instance=pro_comment)

            if pro_comment_form.is_valid():
                pro_comment = pro_comment_form.save()
                messages.success(request, '게시물이 수정되었습니다')
        else:
            pro_comment_form = ProCommentForm(instance=pro_comment)

    context = {
        'type': "PRO",
        'pro_comment': pro_comment,
        'pro_comment_form': pro_comment_form,
    }
    return render(request, 'post/comment_update.html', context)


@login_required
def con_comment_update(request, comment_pk):
    con_comment = get_object_or_404(ConComment, pk=comment_pk)
    post_pk = con_comment.post.pk

    if con_comment.author != request.user:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_detail', post_pk=post_pk)
    else:
        if request.method == 'POST':
            con_comment_form = ConCommentForm(request.POST, request.FILES, instance=con_comment)

            if con_comment_form.is_valid():
                con_comment = con_comment_form.save()
                messages.success(request, '게시물이 수정되었습니다')
        else:
            con_comment_form = ConCommentForm(instance=con_comment)

    context = {
        'type': "CON",
        'con_comment': con_comment,
        'con_comment_form': con_comment_form,
    }
    return render(request, 'post/comment_update.html', context)


@login_required
def pro_comment_delete(request, comment_pk):
    pro_comment = get_object_or_404(ProComment, pk=comment_pk)
    post_pk = pro_comment.post.pk

    if request.method == 'POST' and request.user == pro_comment.author :
        pro_comment.delete()
        message = '댓글이 삭제되었습니다.'
    else:
        message = '잘못된 접근입니다.'
    return HttpResponse(json.dumps({'message': message}), content_type="application/json")


@login_required
def con_comment_delete(request, comment_pk):
    con_comment = get_object_or_404(ConComment, pk=comment_pk)
    post_pk = con_comment.post.pk

    if request.method == 'POST' and request.user == con_comment.author:
        con_comment.delete()
        message = '댓글이 삭제되었습니다.'
    else:
        message = '잘못된 접근입니다.'
    return HttpResponse(json.dumps({'message': message}), content_type="application/json")




@login_required
def comment_pro_comment(request, comment_pk):
    pro_comment = get_object_or_404(ProComment, pk=comment_pk)
    post_pk = pro_comment.post.pk
    user = request.user
    comment_pro_comment_form = CommentOnProCommentForm(request.POST)

    if comment_pro_comment_form.is_valid():
        comment_pro_comment = comment_pro_comment_form.save(commit=False)
        comment_pro_comment.pro_comment = pro_comment
        comment_pro_comment.author = request.user
        comment_pro_comment.save()
        messages.success(request, '댓글을 등록했습니다')
        return redirect('post:post_detail', post_pk=post_pk)

    context = {
        'type': "PRO",
        'comment_pro_comment_form': comment_pro_comment_form,
    }
    return render(request, 'post/comment_on_comment.html', context)


@login_required
def comment_con_comment(request, comment_pk):
    con_comment = get_object_or_404(ConComment, pk=comment_pk)
    post_pk = con_comment.post.pk
    user = request.user
    comment_con_comment_form = CommentOnConCommentForm(request.POST)

    if comment_con_comment_form.is_valid():
        comment_con_comment = comment_con_comment_form.save(commit=False)
        comment_con_comment.con_comment = con_comment
        comment_con_comment.author = request.user
        comment_con_comment.save()
        messages.success(request, '댓글을 등록했습니다')
        return redirect('post:post_detail', post_pk=post_pk)

    context = {
        'type': "PRO",
        'comment_con_comment_form': comment_con_comment_form,
    }
    return render(request, 'post/comment_on_comment.html', context)


@login_required
def pro_comment_report(request, comment_pk):
    pro_comment = get_object_or_404(ProComment, pk=comment_pk)
    post_pk = pro_comment.post.pk
    user = request.user
    report_pro_comment_form = ReportProCommentForm(request.POST)

    if report_pro_comment_form.is_valid():
        report_pro_comment = report_pro_comment_form.save(commit=False)
        report_pro_comment.pro_comment = pro_comment
        report_pro_comment.author = request.user
        report_pro_comment.save()
        messages.success(request, '댓글이 신고되었습니다')
        return redirect('post:post_detail', post_pk=post_pk)

    context = {
        'type': "PRO",
        'report_pro_comment_form': report_pro_comment_form,
    }
    return render(request, 'post/comment_report.html', context)


@login_required
def con_comment_report(request, comment_pk):
    con_comment = get_object_or_404(ConComment, pk=comment_pk)
    post_pk = con_comment.post.pk
    user = request.user
    report_con_comment_form = ReportConCommentForm(request.POST)

    if report_con_comment_form.is_valid():
        report_con_comment = report_con_comment_form.save(commit=False)
        report_con_comment.con_comment = con_comment
        report_con_comment.author = request.user
        report_con_comment.save()
        messages.success(request, '댓글이 신고되었습니다')
        return redirect('post:post_detail', post_pk=post_pk)

    context = {
        'type': "CON",
        'report_con_comment_form': report_con_comment_form,
    }
    return render(request, 'post/comment_report.html', context)


@login_required
def pro_comment_like_toggle(request, comment_pk):
    pro_comment = get_object_or_404(ProComment, pk=comment_pk)
    post_pk = pro_comment.post.pk
    user = request.user
    filtered_like_pro_comments = user.like_pro_comments.filter(pk=pro_comment.pk)

    if filtered_like_pro_comments.exists():
        user.like_pro_comments.remove(pro_comment)
    else:
        user.like_pro_comments.add(pro_comment)

    return redirect('post:post_detail', post_pk=post_pk)

@login_required
def con_comment_like_toggle(request, comment_pk):
    con_comment = get_object_or_404(ConComment, pk=comment_pk)
    post_pk = con_comment.post.pk
    user = request.user
    filtered_like_con_comments = user.like_con_comments.filter(pk=con_comment.pk)

    if filtered_like_con_comments.exists():
        user.like_con_comments.remove(con_comment)
    else:
        user.like_con_comments.add(con_comment)

    return redirect('post:post_detail', post_pk=post_pk)


@login_required
def pro_comment_hate_toggle(request, comment_pk):
    pro_comment = get_object_or_404(ProComment, pk=comment_pk)
    post_pk = pro_comment.post.pk
    user = request.user
    filtered_hate_pro_comments = user.hate_pro_comments.filter(pk=pro_comment.pk)

    if filtered_hate_pro_comments.exists():
        user.hate_pro_comments.remove(pro_comment)
    else:
        user.hate_pro_comments.add(pro_comment)

    return redirect('post:post_detail', post_pk=post_pk)


@login_required
def con_comment_hate_toggle(request, comment_pk):
    con_comment = get_object_or_404(ConComment, pk=comment_pk)
    post_pk = con_comment.post.pk
    user = request.user
    filtered_hate_con_comments = user.hate_con_comments.filter(pk=con_comment.pk)

    if filtered_hate_con_comments.exists():
        user.hate_con_comments.remove(con_comment)
    else:
        user.hate_con_comments.add(con_comment)

    return redirect('post:post_detail', post_pk=post_pk)
