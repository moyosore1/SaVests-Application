from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from .decorators import check_if_is_staff
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
	return render(request, 'users/home.html')


@login_required()
@check_if_is_staff
def send_mail_to_all(request):

	if request.method == 'POST':
		User = get_user_model()	
		subject = request.POST.get('subject')
		body = request.POST.get('body')
		users = User.objects.all()
		print(users)
		for user in users:
			send_mail(subject, "Hello "+user.username+".\n\n"+body, 'moyosore@gmail.com', [user.email], fail_silently=False)


	return render(request, 'users/mailusers.html')


