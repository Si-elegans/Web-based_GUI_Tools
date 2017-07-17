#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.conf import settings
from django.http import Http404

from spirit.utils.ratelimit.decorators import ratelimit
from spirit.models.topic import Topic
from spirit.utils import paginator, markdown, render_form_errors
from spirit.utils.decorators import moderator_required
from spirit.utils import json_response, render_form_errors

from spirit.models.comment import Comment
from spirit.forms.comment import CommentForm, CommentMoveForm, CommentImageForm
from spirit.signals.comment import comment_posted, comment_pre_update, comment_post_update


@login_required
@ratelimit(rate='1/10s')
def comment_publish(request, topic_id, pk=None):
    topic = get_object_or_404(Topic.objects.for_access_open(request.user),
                              pk=topic_id)

    if request.method == 'POST':
        form = CommentForm(user=request.user, topic=topic, data=request.POST)

        if not request.is_limited and form.is_valid():
            comment = form.save()
            comment_posted.send(sender=comment.__class__, comment=comment, mentions=form.mentions)
            return redirect(request.POST.get('next', comment.get_absolute_url()))
    else:
        initial = None

        if pk:
            comment = get_object_or_404(Comment.objects.for_all(), pk=pk)
            quote = markdown.quotify(comment.comment, comment.user.username)
            initial = {'comment': quote, }

        form = CommentForm(initial=initial)

    return render(request, 'spirit/comment/comment_publish.html', {'form': form, 'topic': topic})


@login_required
def comment_update(request, pk):
    comment = Comment.objects.for_update_or_404(pk, request.user)

    if request.method == 'POST':
        form = CommentForm(data=request.POST, instance=comment)

        if form.is_valid():
            comment_pre_update.send(sender=comment.__class__, comment=Comment.objects.get(pk=comment.pk))
            comment = form.save()
            comment_post_update.send(sender=comment.__class__, comment=comment)
            return redirect(request.POST.get('next', comment.get_absolute_url()))
    else:
        form = CommentForm(instance=comment)

    return render(request, 'spirit/comment/comment_update.html', {'form': form, })


@moderator_required
def comment_delete(request, pk, remove=True):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        Comment.objects.filter(pk=pk)\
            .update(is_removed=remove)

        return redirect(comment.get_absolute_url())

    return render(request, 'spirit/comment/comment_moderate.html', {'comment': comment, })


@require_POST
@moderator_required
def comment_move(request, topic_id):
    # TODO: comment_move signal (update topic comment_count)
    topic = get_object_or_404(Topic, pk=topic_id)
    form = CommentMoveForm(topic=topic, data=request.POST)

    if form.is_valid():
        comments = form.save()

        for comment in comments:
            comment_posted.send(sender=comment.__class__, comment=comment, mentions=None)
    else:
        messages.error(request, render_form_errors(form))

    return redirect(request.POST.get('next', topic.get_absolute_url()))

@login_required
def comment_find(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment_number = Comment.objects.filter(topic=comment.topic, date__lte=comment.date).count()
    url = paginator.get_url(comment.topic.get_absolute_url(),
                            comment_number,
                            settings.ST_COMMENTS_PER_PAGE,
                            settings.ST_COMMENTS_PAGE_VAR)
    return redirect(url)


@require_POST
@login_required
def comment_image_upload_ajax(request):
    if not request.is_ajax():
        return Http404()

    form = CommentImageForm(user=request.user, data=request.POST, files=request.FILES)

    if form.is_valid():
        image = form.save()
        return json_response({'url': image.url, })

    return json_response({'error': dict(form.errors.items()), })