from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.

def abcd(request):
	return render(request,'abcd.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def index(request):
	return render(request,'index.html')

def services(request):
	return render(request,'services.html')

def head(request):
	return render(request,'head.html')

def reg(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		password=request.POST['password']
		phone=request.POST['phone']
		img=request.FILES['image']
		check=u_tab.objects.filter(email=email)
		if check:
			return render(request,'reg.html',{"error":"email already taken"})
		else:
			user=u_tab(uname=name,email=email,password=password,phone=phone,image=img)
			user.save()
			return render(request,'index.html')
	else:
	    return render(request,'reg.html')

def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		check=u_tab.objects.filter(email=email,password=password)
		if check:
			for x in check:
				request.session['myid']=x.id
				request.session['myname']=x.uname
			return render(request,'index.html',{"success":"logged in"})
		else:
			return render(request,'login.html',{"error":"invalid details"})
	else:
		return render(request,'login.html')

def logout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['myname']
		return HttpResponseRedirect('/')
	else:
		return redirect('/')

def contact(request):
	if request.method=='POST':
		name=request.POST['name']
		subject=request.POST['subject']
		email=request.POST['email']
		phone=request.POST['phone']
		message=request.POST['message']
		check=contab.objects.filter(email=email)
		if check:
			return render(request,'contact.html',{"error":"email already taken"})
		else:
			data=contab(name=name,subject=subject,email=email,phone=phone,message=message)
			data.save()
			return redirect('/')
	else:
		return render(request,'contact.html')

def display(request):
	data=u_tab.objects.all()
	return render(request,'display.html',{'datas':data})

def update(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		password=request.POST['password']
		phone=request.POST['phone']
		regid=request.GET['regid']
		data=u_tab.objects.filter(id=regid).update(uname=name,email=email,password=password,phone=phone)
	
		return redirect('/display')
	else:
		regid=request.GET['regid']
		data=u_tab.objects.filter(id=regid)

		return render(request,'update.html',{'data':data})

def delete(request):
	regid=request.GET['regid']
	data=u_tab.objects.filter(id=regid).delete()
	return redirect('/display')




##############################################################################################################
################################################## ADMIN ########################################################



def admin_index(request):
	return render(request,'admin/index.html')

def blocks(request):
	return render(request,'admin/blocks.html')

def cards(request):
	return render(request,'admin/cards.html')

def carousels(request):
	return render(request,'admin/carousels.html')

def forms(request):
	return render(request,'admin/forms.html')

def people(request):
	return render(request,'admin/people.html')

def pricing(request):
	return render(request,'admin/pricing.html')

def regform(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		password=request.POST['password']
		address=request.POST['address']
		check=admin.objects.filter(email=email)
		if check:
			return render(request,'admin/forms.html',{"error":"email already taken"})
		else:
			user=admin(name=name,email=email,password=password,address=address)
			user.save()
			return render(request,'admin/index.html')
	else:
		return render(request,'admin/forms.html')

def admindisplay(request):
	data=admin.objects.all()
	return render(request,'admin/display.html',{'datas':data})

def admin_login(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		check=admin.objects.filter(email=email,password=password)
		if check:
			for x in check:
				request.session['myid']=x.id
				request.session['myname']=x.name
			return render(request,'admin/index.html',{"success":"logged in"})
		else:
			return render(request,'admin/login.html',{"error":"invalid details"})
	else:
		return render(request,'admin/login.html')
def admin_logout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['myname']
		return HttpResponseRedirect('/adminindex/')
	else:
		return redirect('/adminindex/')

def admin_update(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		password=request.POST['password']
		address=request.POST['address']
		regid=request.GET['regid']
		data=admin.objects.filter(id=regid).update(name=name,email=email,password=password,address=address)
		return redirect('/admindisplay/')

	else:
		regid=request.GET['regid']
		data=admin.objects.filter(id=regid)
		return render(request,'admin/update.html',{'data':data})

def admin_delete(request):
	regid=request.GET['regid']
	data=admin.objects.filter(id=regid).delete()
	return redirect('/admindisplay/') 






