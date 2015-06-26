# coding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('parsifal.library.views',
    url(r'^$', 'index', name='index'),
    url(r'^new_folder/$', 'new_folder', name='new_folder'),
    url(r'^edit_folder/$', 'edit_folder', name='edit_folder'),
    url(r'^folders/(?P<slug>[-\w]+)/$', 'folder', name='folder'),
    url(r'^new_document/$', 'new_document', name='new_document'),
    url(r'^documents/(?P<slug>[-\w]+)/$', 'document', name='document'),
)
