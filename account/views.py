from django.contrib.auth import logout
from django.shortcuts import redirect, render

def logout_view(request):
	logout(request)
	return redirect('logged_out')


def logged_out_view(request):
	return render(request, 'registration/logged_out.html')