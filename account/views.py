from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View
from django.contrib.auth.views import FormView, LoginView, AuthenticationForm
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserCreationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            next_ = request.GET.get('next')
            print(next_)
            next_post = request.POST.get('next')
            redirect_path = next_ or next_post or None
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,
                                    username=cd['username'],
                                    password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
                            return redirect(redirect_path)
                        else:
                            return redirect('index')
                    else:
                        return HttpResponse("<script>alert('Access Denied')</script><script>window.location='/accounts'</script>")
                else:
                    return HttpResponse("<script>alert('Invalid Login')</script><script>window.location='/accounts'</script>")
        else:
            form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts')
    logout(request)
    return redirect('index')
