from django.conf.urls import patterns, url

from books_pc_multi_view import views

urlpatterns = [
  url(r'^$', views.home, name='home'),

  url(r'^book_view/(?P<pk>\d+)$', views.book_view, name='book_view'),
  url(r'^book_new$', views.book_create, name='book_new'),
  url(r'^book_edit/(?P<pk>\d+)$', views.book_update, name='book_edit'),
  url(r'^book_delete/(?P<pk>\d+)$', views.book_delete, name='book_delete'),

  url(r'^review_new/(?P<parent_pk>\d+)$', views.review_create, name='review_new'),
  url(r'^review_edit/(?P<pk>\d+)$', views.review_update, name='review_edit'),
  url(r'^review_delete/(?P<pk>\d+)$', views.review_delete, name='review_delete'),
]