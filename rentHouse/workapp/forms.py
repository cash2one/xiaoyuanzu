from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from .models import UserInfo


def yyname_validator(yyname):
    if len(yyname) > 8:
        raise ValidationError(u'请输入 8 个字符以内的用户名')


def yyphone_validator(yyphone):
    if len(yyphone) != 11:
        raise ValidationError(u'请输入11位手机号码')



class AppointmentForm(forms.Form):
    yyname = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': u'姓名'}),
        error_messages={
            'requied': 'please write something'
        },
        validators=[yyname_validator]
    )
    yyphone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': u'手机号'}),
        error_messages={
            'requied': 'please write something'
        },
        validators=[yyphone_validator]
    )


ARTICLE_CHOICES = (
    (u'一室一厅一卫', u'一室一厅一卫'),
    (u'二室一厅一卫', u'二室一厅一卫'),
    (u'三室一厅一卫', u'三室一厅一卫'),
    (u'三室一厅两卫', u'三室一厅两卫'),
    (u'三室两厅两卫', u'三室两厅两卫'),
    (u'四室两厅两卫', u'四室两厅两卫'),
)

RADIO_CHOICES = (
    (u'整租', u'整租'),
    (u'合租', u'合租'),
    (u'月租', u'月租'),
)


class List_form(forms.Form):
    type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=RADIO_CHOICES, label=u'类型'
    )
    housetype = forms.MultipleChoiceField(
        label=u'户型',
        choices=ARTICLE_CHOICES,
        widget=forms.CheckboxSelectMultiple()
    )
    rent_start = forms.IntegerField()
    rent_end = forms.IntegerField()


# def email_validator(email):
#     user = UserInfo.objects.filter(email=email)
#     if user:
#         raise ValidationError(u'此邮箱已被注册过')


def username_validator(username):
    if len(username) > 14:
        raise ValidationError(u'请输入 14 个字符以内的用户名')


class LoginForm(forms.ModelForm):
    email = forms.CharField(
        # label=u'邮箱',
        widget=forms.TextInput(attrs={'placeholder': u'邮箱'}),
        validators=[EmailValidator]
    )
    password = forms.CharField(
        # label=u'密码',
        widget=forms.PasswordInput(attrs={'placeholder': u'密码'}),
        validators=[validate_password]
    )

    class Meta:
        model = UserInfo
        fields = ('email', 'password')


class RegisterForm(forms.ModelForm):
    email = forms.CharField(
        # label=u'邮箱',
        widget=forms.TextInput(attrs={'placeholder': u'邮箱'}),
        validators=[EmailValidator]
    )
    username = forms.CharField(
        # label=u'用户名',
        widget=forms.TextInput(attrs={'placeholder': u'用户名'}),
        validators=[username_validator]
    )
    password = forms.CharField(
        # label=u'密码',
        widget=forms.PasswordInput(attrs={'placeholder': u'密码'}),
        validators=[validate_password]
    )

    class Meta:
        model = UserInfo
        fields = ('email', 'username', 'password')
