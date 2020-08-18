from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import loader
from django.urls import reverse


# Create your views here.

def index(request):
    subject_list = Subject.objects.order_by('subject_title')
    template = loader.get_template('notetaking/index.html')
    temp = ""
    count = 0
    for subject in Subject.objects.all():

        temp = temp + " " + subject.subject_title
        count = count + 1
    context = {
        'subject_list': subject_list,
    }
    return HttpResponse(template.render(context, request))


def chapters(request, subject_id):
    try:
        subject = Subject.objects.all()[subject_id - 1]
    except Subject.DoesNotExist:
        subject = ""
    chapter_list = subject.chapter_set.all()
    template = loader.get_template('notetaking/subject.html')
    context = {
        'chapter_list': chapter_list,
        'subject': subject,
    }
    return HttpResponse(template.render(context, request))
    # try:
    # subject = Subject.objects.all()[subject_id]
    # except Subject.DoesNotExist:
    #   return HttpResponse("oof")
    # else:
    #   return HttpResponse("you're looking at the chapters of %s" % subject.subject_title)


def topics(request, subject_id, chapter_id):
    try:
        subject = Subject.objects.all()[subject_id - 1]
        chapter = subject.chapter_set.filter(id=chapter_id)[0]

    except Subject.DoesNotExist:
        subject = ""
        chapter = ""
    topic_list = chapter.topic_set.all()
    template = loader.get_template('notetaking/chapter.html')
    context = {
        'topic_list': topic_list,
        'chapter': chapter,
        'subject': subject,
    }
    return HttpResponse(template.render(context, request))


def definitions(request, subject_id, chapter_id, topic_id):
    try:
        subject = Subject.objects.all()[subject_id - 1]
        chapter = subject.chapter_set.filter(id=chapter_id)[0]
        topic = chapter.topic_set.filter(id=topic_id)[0]

    except Subject.DoesNotExist:
        subject = ""
        chapter = ""
        topic = ""
    definition_list = topic.definition_set.all()
    template = loader.get_template('notetaking/topic.html')
    context = {
        'definition_list': definition_list,
        'topic': topic,
        'chapter': chapter,
        'subject': subject,
    }
    return HttpResponse(template.render(context, request))


def new_subject(request):
    subject = Subject.objects.create(subject_title=request.POST['sub'])
    return HttpResponseRedirect(reverse('notetaking:index'))


def new_chapter(request, subject_id):
    subject = Subject.objects.all()[subject_id - 1]
    chapter = subject.chapter_set.create(chapter_title=request.POST['sub'])
    return HttpResponseRedirect(reverse('notetaking:chapters', kwargs={'subject_id': subject.id}))


def new_topic(request, subject_id, chapter_id):
    subject = Subject.objects.all()[subject_id - 1]
    chapter = subject.chapter_set.filter(id=chapter_id)[0]
    topic = chapter.topic_set.create(topic_title=request.POST['sub'])
    return HttpResponseRedirect(
        reverse('notetaking:topics', kwargs={'subject_id': subject.id, 'chapter_id': chapter.id})
    )


def new_definition(request, subject_id, chapter_id, topic_id):
    subject = Subject.objects.all()[subject_id - 1]
    chapter = subject.chapter_set.filter(id=chapter_id)[0]
    topic = chapter.topic_set.filter(id=topic_id)[0]
    definition = topic.definition_set.create(definition_term=request.POST['term'], definition_text=request.POST['text'])
    return HttpResponseRedirect(
        reverse(
            'notetaking:definitions',
            kwargs={'subject_id': subject.id, 'chapter_id': chapter.id, 'topic_id': topic.id}
        )
    )


def delete_subject(request):
    subject = Subject.objects.filter(id=request.POST['delete'])
    subject.delete()
    return HttpResponseRedirect(reverse('notetaking:index'))


def delete_chapter(request, subject_id):
    subject = Subject.objects.all()[subject_id - 1]
    chapter = subject.chapter_set.all()[0]
    chapter.delete()
    return HttpResponseRedirect(reverse('notetaking:chapters', kwargs={'subject_id': subject.id}))


def delete_topic(request, subject_id, chapter_id):
    subject = Subject.objects.all()[subject_id - 1]
    chapter = subject.chapter_set.all().filter(id=chapter_id)[0]
    topic = chapter.topic_set.all()[0]
    topic.delete()
    return HttpResponseRedirect(reverse('notetaking:topics', kwargs={'subject_id': subject.id, 'chapter_id': chapter.id}))


def delete_definition(request, subject_id, chapter_id, topic_id):
    subject = Subject.objects.all()[subject_id - 1]
    chapter = subject.chapter_set.all().filter(id=chapter_id)[0]
    topic = chapter.topic_set.all().filter(id=topic_id)[0]
    definition = topic.definition_set.all()[0]
    definition.delete()
    return HttpResponseRedirect(reverse('notetaking:definitions', kwargs={'subject_id': subject.id, 'chapter_id': chapter.id, 'topic_id': topic.id}))
