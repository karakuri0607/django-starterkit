from django import forms
from .models import m_category, m_tag
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail

#　検索フォーム
class SearchForm(forms.Form):    
    keyword = forms.CharField(label='キーワード', max_length=100, required=False,
                                widget=forms.TextInput(attrs={"class":"form-control"}))
    category = forms.ModelChoiceField(label='カテゴリ', empty_label='未選択', queryset=m_category.objects.all(), required=False,
                                        widget=forms.Select(attrs={"class":"form-select"}))
    tag = forms.ModelChoiceField(label='タグ', empty_label='未選択', 
                                queryset=m_tag.objects.all(), 
                                required=False,
                                widget=forms.Select(attrs={"class":"form-select"}))

    ORDER_CHOICES = (
        ('newadddate', '新着順'),
        ('views', '人気順'),
    )

    order = forms.fields.ChoiceField(
        choices=ORDER_CHOICES,
        initial = 'newadddate',
        required=False,
        label='並び替え',
        widget=forms.Select(attrs={"class":"form-select"})
    )

#　問い合わせフォーム
class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "お名前",
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス",
        }),
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容",
        }),
    )

    def send_email(self):
        subject = "お問い合わせ"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
