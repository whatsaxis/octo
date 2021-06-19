from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                _('This account is inactive.'),
                code='inactive'
            )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')