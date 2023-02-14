from django.urls import path
from . import views

urlpatterns=[
	# path('',views.index),
	# path('abcd/',views.abcd)
	path('about/',views.about),
	path('contact/',views.contact),
	path('',views.index),
	path('services/',views.services),
	path('reg/',views.reg),
	path('login/',views.login),
	path('logout/',views.logout),
	path('display/',views.display),
	path('update/',views.update),
	path('delete/',views.delete),



##############################################################################################################
################################################## ADMIN ########################################################


	path('adminindex/',views.admin_index),
	path('adminblocks/',views.blocks),
	path('admincards/',views.cards),
	path('admincarousels/',views.carousels),
	path('adminforms/',views.forms),
	path('adminpeople/',views.people),
	path('adminpricing/',views.pricing),
	path('regform/',views.regform),
	path('admindisplay/',views.admindisplay),
	path('adminlogin/',views.admin_login),
	path('adminlogout/',views.admin_logout),
	path('adminupdate/',views.admin_update),
	path('admindelete/',views.admin_delete),












]