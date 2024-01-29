from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Post, Page, Tag
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404
from django.views.generic import ListView


PER_PAGE = 9


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = '-pk',
    paginate_by = PER_PAGE
    queryset = Post.objects.get_published()

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_published=True)
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'page_title': 'Home - ',
        })

        return context


# def index(request):
#     posts = (
#         Post.objects.get_published()
#     )

#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return render(
#         request,
#         'blog/index.html',
#         {
#             'page_obj': page_obj,
#             'page_title': 'Home - ',
#         }
#     )


class CreatedByListView(PostListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._temp_context: dict[str, Any] = {}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self._temp_context['user']
        user_full_name = user.username

        if user.first_name:
            user_full_name = f'{user.first_name} {user.last_name}'
        page_title = 'Posts de ' + user_full_name + ' - '

        ctx.update({
            'page_title': page_title,
        })

        return ctx

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        qs = qs.filter(created_by__pk=self._temp_context['user'].id)
        return qs

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        user = User.objects.filter(id=id).first()

        if user is None:
            raise Http404()

        self._temp_context.update({
            'author_pk': id,
            'user': user,
        })

        return super().get(request, *args, **kwargs)


# def created_by(request, id):

#     posts = (
#         Post.objects.get_published()
#         .filter(created_by__id=id)
#     )

#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     user = User.objects.filter(id=id).first()
#     user_full_name = user.username

#     if user is None:
#         raise Http404()

#     if user.first_name:
#         user_full_name = f'{user.first_name} {user.last_name}'

#     page_title = user_full_name + ' posts -'

#     return render(
#         request,
#         'blog/index.html',
#         {
#             'page_obj': page_obj,
#             'page_title': page_title,
#         }
#     )


def category(request, slug):
    posts = (
        Post.objects.get_published()
        .filter(category__slug=slug)
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    page_title = f'{page_obj[0].category.name} - Categoria -'

    return render(
        request,
        'blog/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
        }
    )


def tags(request, slug):

    tag = get_object_or_404(Tag, slug=slug)

    posts = (
        Post.objects.get_published()
        .filter(tags__slug=slug)
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    page_title = f'{tag.name} - Tag -'

    return render(
        request,
        'blog/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
        }
    )


def search(request):

    search_value = request.GET.get('search').strip()

    posts = (
        Post.objects.get_published()
        .filter(
            Q(title__icontains=search_value) |
            Q(excerpt__icontains=search_value) |
            Q(content__icontains=search_value)
        )[:PER_PAGE]
    )

    page_title = f'{search_value[:15]} - Search -'

    return render(
        request,
        'blog/index.html',
        {
            'page_obj': posts,
            'search_value': search_value,
            'page_title': page_title,
        }
    )


def page(request, slug):
    page_obj = (
        Page.objects.filter(is_published=True)
        .filter(slug=slug)
        .first()
    )

    if page_obj is None:
        raise Http404()

    page_title = f'{page_obj.title} - Página -'

    return render(
        request,
        'blog/page.html',
        {
            'page': page_obj,
            'page_title': page_title,
        }
    )


def post(request, slug):
    post_obj = (
        Post.objects.get_published()
        .filter(slug=slug)
        .first()
    )

    if post_obj is None:
        raise Http404()

    page_title = f'{post_obj.title} - Post-'

    return render(
        request,
        'blog/post.html',
        {
            'post': post_obj,
            'page_title': page_title,
        }
    )
