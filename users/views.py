from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


# Create your views here.

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


