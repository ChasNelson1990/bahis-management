from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token


@login_required
def permissions(request):
    user = request.user

    if request.user.is_superuser:
        token = Token.objects.get(user=user)
        return render(request, "frontend/index.html", {"token": token})
    else:
        messages.add_message(request, messages.INFO, "You are not a Admin. You are a regular user!")
        return redirect(to="home")
