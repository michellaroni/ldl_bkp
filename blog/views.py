from django.shortcuts import render
from django.views import generic
from .models import Post
import markdown
import bleach

# def index(request):
#     #aqui puxo dados deo banco de dados importando o model (tabela)
#     teste = "Alô alô, marciano!!"
#     return render(request, 'blog/index.html', {'msg': teste})
    
class PostList(generic.ListView):
    """
    Return all posts that are with status 1 (published) and order from the latest one.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'blog/index.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     for post in queryset:
    #         html_content = markdown.markdown(post.content)
    #         post.content = bleach.clean(html_content, tags=[], strip=True)
    #     return queryset

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    # def get_object(self, queryset=None):
    #     post = super().get_object(queryset)
    #     # Converte markdown para HTML com suporte a blocos de código
    #     html_content = markdown.markdown(post.content, extensions=['fenced_code', 'codehilite'])
    #     post.content = html_content  # Não precisa mais de bleach.clean aqui
    #     return post


# ListView:
# Usada para exibir uma lista de objetos.
# Por padrão, a variável de contexto será object_list ou post_list.

# DetailView:
# Usada para exibir detalhes de um único objeto.
# Por padrão, a variável de contexto será object.