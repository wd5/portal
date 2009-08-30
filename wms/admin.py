from portal.wms.models import Provider, Manufacturer, Project, ItemType, Item, Import, Export, LibraryType, User, Qaer, Library

from django.contrib import admin
from django import forms

class ProviderAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc','contact', 'tel1', 'tel2','mail')
	search_fields = ('name', 'desc')

class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc')
	search_fields = ('name', 'desc')

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc', 'owner', 'customer')
	search_fields = ('name', 'desc', 'owner', 'customer')

class ItemTypeAdmin(admin.ModelAdmin):
	list_display = ('name','desc')

class ItemAdmin(admin.ModelAdmin):
	list_display = ('pn', 'opn', 'type', 'manufacturer', 'value', 'package', 'desc', 'num')
	list_filter = ('type','manufacturer','package','value',)
	search_fields = ('pn', 'opn', 'type__name','manufacturer__name','value', 'desc')

class ImportAdmin(admin.ModelAdmin):
	list_display = ('item','provider','project','num', 'price', 'sum', 'ver','cycle','min_num', 'min_price','pay_date', 'arrive_date', 'arrived_date', 'enter_date')
	list_display_links = ('item', 'provider', 'project')
	list_filter = ('item', 'provider', 'project',)
	ordering = ('-enter_date',)
	search_fields = ('item__pn', 'provider__name', 'project__name',)

class ExportAdminForm(forms.ModelForm):
	class Meta:
		model = Export
	def clean_num(self):
		selected_item = Item.objects.get(pk=self.cleaned_data["item"].pk)
		if self.cleaned_data["num"] > selected_item.num:
			raise forms.ValidationError('There are only %d in the warehouse' % selected_item.num)
		else:
			return self.cleaned_data["num"]

class ExportAdmin(admin.ModelAdmin):
	form = ExportAdminForm

	list_display = ('item', 'project', 'num', 'issue_date')
	list_display_links = ('item', 'project')
	list_filter = ('item', 'project',)
	ordering = ('-issue_date',)
	search_fields = ('item__pn', 'project__name')

class LibraryTypeAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc')
	search_fields = ('name', 'desc')

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc')
	search_fields = ('name', 'desc')

class QaerAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc')
	search_fields = ('name', 'desc')

class LibraryAdmin(admin.ModelAdmin):
	list_display = ('name', 'pad', 'type', 'project', 'desc', 'qa', 'creator')
	search_fields = ('name', 'pad', 'project__name', 'type__name', 'desc', 'up_desc')

admin.site.register(Provider, ProviderAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Import, ImportAdmin)
admin.site.register(Export, ExportAdmin)
admin.site.register(LibraryType, LibraryTypeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Qaer, QaerAdmin)
admin.site.register(Library, LibraryAdmin)

