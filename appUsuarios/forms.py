from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('email',)