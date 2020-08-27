from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as uAdmin
from dateutil.relativedelta import relativedelta
from .models import User as myUser
from django.contrib import messages 
import datetime
from django.utils.translation import gettext_lazy as _

# Register your models here.

class DateJoinedFilter(admin.SimpleListFilter):
	title = _('Date Added')
	parameter_name = 'filterby'

	def lookups(self, request, model_admin):
		return(
			('24hours', _('Added in the past 24 hours')),
			('oneweek', _('Added in the past week')),
			('onemonth', _('Added in the past month')),
		)

	def queryset(self, request, queryset):
		time_24_hours_ago = datetime.datetime.today() - datetime.timedelta(hours=24)
		time_one_week_ago = datetime.datetime.today() - datetime.timedelta(days=7)
		time_one_month_ago = datetime.datetime.today() - relativedelta(months=1)
		

		if self.value() == '24hours':
			return queryset.filter(date_joined__lt=datetime.datetime.today(), date_joined__gt=time_24_hours_ago)
		if self.value() == 'oneweek':
			return queryset.filter(date_joined__lt=datetime.datetime.today(), date_joined__gt=time_one_week_ago)
		if self.value() == 'onemonth':
			return queryset.filter(date_joined__lt=datetime.datetime.today(), date_joined__gt=time_one_month_ago)
				


class UserAdmin(uAdmin):
	list_display = ('username', 'date_joined', 'active')
	list_filter = (DateJoinedFilter,)

	def active(self, obj): 
		return obj.is_active == 1

	active.boolean = True	

	def make_active(modeladmin, request, queryset): 
		queryset.update(is_active = 1) 
		messages.success(request, "Users made active") 

	def make_inactive(modeladmin, request, queryset): 
		queryset.update(is_active = 0)
		messages.success(request, "Users made inactive") 	

	admin.site.add_action(make_active, "Make User Active") 	
	admin.site.add_action(make_inactive, "Make User Inactive")   

admin.site.register(myUser, UserAdmin)