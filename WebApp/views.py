from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token
from .forms import *
from django.contrib import messages, auth
from django.core.mail import EmailMessage


@login_required
def ListEmp(request):
    if User.is_authenticated:
        object_list = officemodel.objects.all()

        return render(request, 'list_emp.html', {'object_list': object_list})
    else:
        return render(request, 'registration/login.html')


@login_required
def CreateEmp(request):
    form = CreateForm
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create_emp.html', {'form': form})


@login_required
def UpdateEmp(request, id):
    form = UpdateForm
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=officemodel.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update_emp.html', {'form': form})


@login_required
def DeleteEmp(request, id):
    if request.method == 'POST':
        officemodel.objects.get(id=id).delete()
        return redirect('home')
    return render(request, 'delete_emp.html', {'id': id})


def signup(request):
    form = UserCreation
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(
                request, 'Verification email Sent successfully, please verify your email address')
            return redirect('login')

    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            messages.success(request, "{} you're  successfully logged in".format(user.username))
            return redirect('home')
        else:
            messages.success(request, "Invalid username or password.")


@login_required
def log_out(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request)
        messages.success(request, user.username + ' is now active')
        return redirect('home')

    else:
        messages.success(request, 'Activation failed')
        return redirect('login')
