from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('page/<slug:slug>/', views.page, name='page'),

    path(
        'created_by/<int:id>/',
        views.CreatedByListView.as_view(),
        name='created_by'
        ),

    path('category/<slug:slug>/', views.category, name='category'),
    path('tag/<slug:slug>/', views.tags, name='tag'),
    path('search/', views.search, name='search'),

]
