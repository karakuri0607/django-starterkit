from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, FormView
from .models import t_table
from .forms import ContactForm, SearchForm
from django.core.paginator import Paginator
from django.db.models import Q

# 一覧画面
class ListView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        # パラメータの作成
        deletedate = Q(deletedate__isnull=True)
        newadddate = Q(newadddate__lte=timezone.now())
        category   = Q()
        tag        = Q()
        keyword    = Q()
        order      = 'newadddate'
        page       = 1
        if "category" in self.request.GET:
            param_category=self.request.GET.get('category')
            if param_category != "" :
                category = Q(category=param_category)
        if "tag" in self.request.GET:
            param_tag=self.request.GET.get('tag')
            if param_tag != "" :
                tag = Q(tag=param_tag)
        if "keyword" in self.request.GET:
            param_keyword=self.request.GET.get('keyword')
            if param_keyword != "" :
                keyword = Q(title__icontains=param_keyword) | Q(content__icontains=param_keyword)
        if "order" in self.request.GET:
            order=self.request.GET.get('order')
        #　データ取得
        table = t_table.objects.filter(deletedate & newadddate & category & tag & keyword).order_by('-' + order)

        # ページネーション
        if "page" in self.request.GET:
            page = self.request.GET.get('page') 
        paginator = Paginator(table, 20)       # 1ページに表示する件数
        list = paginator.get_page(page)        # 指定のページのデータ取得

        context = super().get_context_data(**kwargs)
        context['list'] = list
        context['searchform'] = SearchForm(self.request.GET)
        return context

# 詳細画面
class DetailView(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        # パラメータ作成
        deletedate = Q(deletedate__isnull=True)
        newadddate = Q(newadddate__lte=timezone.now())
        # 対象データ取得
        detail = get_object_or_404(t_table.objects.filter(deletedate & newadddate), id=self.kwargs['id'])

        # 閲覧数の加算
        detail.views += 1
        detail.save()
        
        context = super().get_context_data(**kwargs)
        context['detail'] = detail
        return context

# お問合せ画面
class ContactFormView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('app:contact_result')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

# お問合せ完了画面
class ContactResultView(TemplateView):
    template_name = 'contact_result.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context