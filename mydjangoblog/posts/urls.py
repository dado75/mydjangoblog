from django.urls import path
from . import views as posts_views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post

# lista dei posts|Homepage del blog
# post singoli del blog
# sezione contatti

urlpatterns = [
    path('', ListView.as_view(
        queryset = Post.objects.all().order_by("-data"),
        template_name = "Lista_post.html",
    paginate_by = 5), name="lista"),
    path('<int:id>/<slug:slug>/', DetailView.as_view(
        model = Post,
        template_name = "post_singolo.html"), name="singolo"),

    path('contatti/' , posts_views.contatti, name="contatti"),
]
