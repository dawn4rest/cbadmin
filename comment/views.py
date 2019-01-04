import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from utils.decorators import login_required
from django.db.models import Count, Q

from .models import Comment
from .forms import CommentForm, CommentOnCommentForm, ReportCommentForm
from post import models as post_models


def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    return render(request, 'include/comment.html', {'comment': comment})


@login_required
def comment_create(request, post_pk):
    if request.method == 'POST':
        type = request.POST.get('type', None)
        post = get_object_or_404(post_models.Post, pk=post_pk)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            if type == "con":
                comment.type = False
            comment.save()

            comment = comment
            return render(request, 'include/comment.html', {'comment': comment})

    return redirect('post:post_detail', post_pk=post_pk)


@login_required
def comment_update(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    post_pk = comment.post.pk

    if comment.author != request.user:
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_detail', post_pk=post_pk)
    else:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST, request.FILES, instance=comment)

            if comment_form.is_valid():
                comment = comment_form.save()
                messages.success(request, '게시물이 수정되었습니다')
        else:
            comment_form = CommentForm(instance=comment)

    context = {
        'comment': comment,
        'comment_form': comment_form,
    }
    return render(request, 'comment/comment_update.html', context)


@login_required
def comment_delete(request):
    comment_pk = request.POST.get('comment_pk', None)
    comment = get_object_or_404(Comment, pk=comment_pk)
    post_pk = comment.post.pk

    if request.method == 'POST' and request.user == comment.author :
        comment.delete()
        message = '댓글이 삭제되었습니다.'
    else:
        message = '잘못된 접근입니다.'
    return HttpResponse(json.dumps({'message': message}), content_type="application/json")




@login_required
def comment_on_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    post_pk = comment.post.pk
    user = request.user
    comment_on_comment_form = CommentOnCommentForm(request.POST)

    if comment_on_comment_form.is_valid():
        comment_on_comment = comment_on_comment_form.save(commit=False)
        comment_on_comment.comment = comment
        comment_on_comment.author = request.user
        comment_on_comment.save()
        messages.success(request, '댓글을 등록했습니다')
        return redirect('post:post_detail', post_pk=post_pk)

    context = {
        'type': "PRO",
        'comment_on_comment_form': comment_on_comment_form,
    }
    return render(request, 'comment/comment_on_comment.html', context)


@login_required
def comment_report(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    post_pk = comment.post.pk
    user = request.user
    report_comment_form = ReportCommentForm(request.POST)

    if report_comment_form.is_valid():
        report_comment = report_comment_form.save(commit=False)
        report_comment.comment = comment
        report_comment.author = request.user
        report_comment.save()
        messages.success(request, '댓글이 신고되었습니다')
        return redirect('post:post_detail', post_pk=post_pk)

    context = {
        'type': "PRO",
        'report_comment_form': report_comment_form,
    }
    return render(request, 'comment/comment_report.html', context)


@login_required
def comment_like_toggle(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    post_pk = comment.post.pk
    user = request.user
    filtered_like_comments = user.like_comments.filter(pk=comment.pk)

    if filtered_like_comments.exists():
        user.like_comments.remove(comment)
    else:
        user.like_comments.add(comment)

    return redirect('post:post_detail', post_pk=post_pk)


@login_required
def comment_hate_toggle(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    post_pk = comment.post.pk
    user = request.user
    filtered_hate_comments = user.hate_comments.filter(pk=comment.pk)

    if filtered_hate_comments.exists():
        user.hate_comments.remove(comment)
    else:
        user.hate_comments.add(comment)

    return redirect('post:post_detail', post_pk=post_pk)
