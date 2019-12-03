from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .get_html import amazon


from .models import Item
from .filters import ItemFilter
from .forms import ItemForm,SignUpForm


# Create your views here.
# 検索一覧画面
class ItemFilterView(FilterView):
    model = Item
    filterset_class = ItemFilter
    # デフォルトの並び順を新しい順とする
    queryset = Item.objects.all().order_by('-created_at')

    # クエリ未指定の時に全件検索を行うために以下のオプションを指定（django-filter2.0以降）
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 12

    # 検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(ItemFilterView, self).get_context_data(**kwargs)
        ctx['randitem'] = Item.objects.order_by('?')[:3]
        return ctx

# 詳細画面
class ItemDetailView(DetailView):
    model = Item


# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        item = form.save(commit=False) # formの情報を保存
        item.author = self.request.user.username
        str = amazon(item.link)
        if(str[0]=="sippai"):
            self.object = item
            return redirect('error')
        else:
            item.name=str[0]
            item.image=str[1]
            item.cat=str[2]
            item.save()
            self.object = item
            return HttpResponseRedirect(self.get_success_url()) # リダイレクト


# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')

    '''
    def form_valid(self, form):
        item = form.save(commit=False)
        if (item.author == self.request.user.username):
            item.save()
            return HttpResponseRedirect(self.get_success_url())  # リダイレクト
        else:
            return HttpResponseRedirect(self.get_success_url())  # リダイレクト
    '''

    def form_valid(self, form):
        item = form.save(commit=False) # formの情報を保存
        item.author = self.request.user.username
        str = amazon(item.link)
        if(str[0]=="sippai"):
            self.object = item
            return redirect('error')
        else:
            item.name=str[0]
            item.image=str[1]
            item.cat=str[2]
            item.save()
            self.object = item
            return HttpResponseRedirect(self.get_success_url()) # リダイレクト

# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))
        return result


# 会員登録画面
class ItemSignUpView(CreateView):
    form_class = SignUpForm
    template_name = "app/signup.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        user.is_staff = True
        user.save()
        login(self.request, user) # 認証
        self.object = user
        return HttpResponseRedirect(self.get_success_url()) # リダイレクト


class ItemErrorView(TemplateView):
    template_name= "app/error.html"

    def get(self, request, **kwargs):

        context = {
            'error': 'Amazonサーバーが混み合っております。',
            'text': 'お手数ですが一度時間を空けてからお試しください。',

        }
        return self.render_to_response(context)