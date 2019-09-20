from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import ProfileForm
from .models import Profile


@login_required(login_url='/accounts/login/')
def UserProfileEditView(request): 
    obj = None
    try:
        obj = get_object_or_404(Profile, usuario = request.user)
    except:
        pass
    
    if obj != None:
        form = ProfileForm(request.POST or None,request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()

    else:
        form = ProfileForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
    
    template_name = 'appUsuarios/profile.html'

    context = {"form": form, "perfil": obj,}

   
    return render(request, template_name, context)
  

   



#class UserProfileEditView(DetailView):
#    template_name = 'users/profile.html'
#
#    def get_object(self):
#        return self.request.user


#def signup(request):
#    if request.method == 'POST':
#        form = SignUpForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(request, email=user.email, password=raw_password)
#            if user is not None:
#                login(request, user)
#            else:
#                print("user is not authenticated")
#            return redirect('users:profile')
#    else:
#        form = SignUpForm()
#    return render(request, 'users/signup.html', {'form': form})
  
