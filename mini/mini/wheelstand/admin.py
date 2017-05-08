from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Models, Trim, ModelsShown, FeaturesAccessory, Exterior, Upholstery, Wheel, Package, Option, \
	Location, TrimEnImage, TrimFrImage, Gallery, Interior, Performance, Colour, TestDrive, KeepingInTouch, \
	StaticModelEN, StaticModelFR, StaticModel, StandAloneOption, OptionalEquipment
from django.forms import TextInput, Textarea
from django.db import models


# class GalleryInline(admin.TabularInline):
#    model = Gallery
#    extra = 3
#    list_display = ('name_en', 'base_price', 'freight_DPI')
#    verbose_name = "Image"
#    verbose_name_plural = "Gallery"
#    readonly_fields = ('image_thumb',)


class GalleryAdmin(admin.ModelAdmin):
	model = Gallery
	list_display = ('name', 'url', 'image_thumb')


# def get_model_perms(self, request):
#        return {}



class ModelsAdmin(admin.ModelAdmin):
	list_display = ('name_en', 'year', 'base_price', 'freight_DPI')
	fieldsets = (
		(_('General'), {
			'fields': (('name_en', 'name_fr'), 'year'),
		}),
		(_('Prices'), {
			'fields': ('base_price', 'colour',
			           'exterior', 'interior', 'trim_price', 'optional_equipement', 'wheels', 'freight_DPI', 'taxes'),
		}),
	)


'''
class StaticModelENAdmin(admin.ModelAdmin):
    list_display = ('url',)
    fieldsets = (
        (_('Image'), {
            'fields': ('url',),
        }),         
    )



class StaticModelFRAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'url_en', 'name_fr', 'url_fr')
    fieldsets = (
        (_('Image'), {
            'fields': ('name_en', 'url_en', 'name_fr', 'url_fr'),
        }),         
    )
'''


class StaticModelAdmin(admin.ModelAdmin):
	list_display = ('name_en', 'url_en', 'name_fr', 'url_fr')
	fieldsets = (
		(_('Image'), {
			'fields': ('name_en', 'url_en', 'name_fr', 'url_fr'),
		}),
	)


class TrimEnImageAdmin(admin.ModelAdmin):
	list_display = ('url', 'link')
	fieldsets = (
		(_('Image'), {
			'fields': ('url', 'link'),
		}),
	)

	def get_model_perms(self, request):
		return {}


class TrimFrImageAdmin(admin.ModelAdmin):
	list_display = ('url', 'link')
	fieldsets = (
		(_('Image'), {
			'fields': ('url', 'link'),
		}),
	)

	def get_model_perms(self, request):
		return {}


class UserProfileInline(admin.TabularInline):
	model = Trim.features_accessories.through
	extra = 1
	verbose_name = 'test'
	verbose_name_plural = 'test'


class FeaturesAccessoryInline(admin.TabularInline):
	model = Trim.features_accessories.through
	extra = 3


class PackagesInline(admin.TabularInline):
	model = Trim.packages.through
	extra = 3


class WheelsInline(admin.TabularInline):
	model = Trim.wheels.through
	extra = 3


class TrimAdmin(admin.ModelAdmin):
	list_display = ('name_en', 'model')
	filter_horizontal = ('upholsteries', 'gallery', 'colours')
	#    inlines = [UserProfileInline,]
	#    inlines = (FeaturesAccessoryInline,)
	fieldsets = (
		(_('General'), {
			'fields': ('model', ('name_en', 'name_fr'), 'MSRP'),
		}),
		(_('Performance'), {
			'fields': (('power_en', 'power_fr'), 'torque', 'fuel_economy', 'acceleration', 'car_range'),
		}),
		(_('Features & Accessories'), {
			'fields': ('features_accessories',),
		}),
		(_('Colours'), {
			'fields': ('colours',),
		}),
		(_('Upholstery'), {
			'fields': ('upholsteries',),
		}),
		(_('Packages'), {
			'fields': ('packages',),
		}),
		(_('Wheels'), {
			'fields': ('wheels',),
		}),
		(_('Options'), {
			'fields': (
			('interior_en', 'interior_fr'), ('performance_en', 'performance_fr'), ('exterior_en', 'exterior_fr'))
		}),

		(_('Image'), {
			'fields': ('gallery',),
		}),
	)


class ModelsShownAdmin(admin.ModelAdmin):
	list_display = ('vehicle', 'price_override')
	readonly_fields = ('image_thumb', 'image_thumb_fr')
	filter_horizontal = ('optional_equipment', 'stand_alone_option', 'package')
	fieldsets = (
		(_('General'), {
			'fields': ('vehicle',),
		}),
		(_('Image English'), {
			'fields': ('url_en', 'link', 'image_thumb'),
		}),
		(_('Image French'), {
			'fields': ('url_fr', 'link_fr', 'image_thumb'),
		}),
		(('Prices'), {
			'fields': ('price_override', ('disclaimer_override_en', 'disclaimer_override_fr'), 'colour_en', 'colour_fr',
			           'exterior', 'interior', 'trim_price', 'wheels', 'taxes'),
		}),
		(('Locations'), {
			'fields': ('location', 'optional_equipment', 'stand_alone_option', 'package'),
		}),
		(('Static Model'), {
			'fields': ('static_model',),
		}),
	)


class FeaturesAccessoryAdmin(admin.ModelAdmin):
	readonly_fields = ('image_thumb',)
	list_display = ('name_en', 'image_thumb', 'trims')
	fieldsets = (
		(_('General'), {
			'fields': (('name_en', 'name_fr',), ('description_en', 'description_fr',)),
		}),
		(_('Image'), {
			'fields': ('url', 'link', 'image_thumb'),
		}),
	)


class ExteriorAdmin(admin.ModelAdmin):
	list_display = ('name_en', 'trims')
	fieldsets = (
		(_('General'), {
			'fields': (('name_en', 'name_fr',),),
		}),
	)


class UpholsteryAdmin(admin.ModelAdmin):
	readonly_fields = ('image_thumb',)
	list_display = ('name_en', 'trims')
	fieldsets = (
		(_('General'), {
			'fields': (('name_en', 'name_fr',)),
		}),
		(_('Image'), {
			'fields': ('url', 'link', 'image_thumb'),
		}),
	)


class WheelAdmin(admin.ModelAdmin):
	readonly_fields = ('image_thumb',)
	list_display = ('name_en', 'trims')
	fieldsets = (
		(_('General'), {
			'fields': (('name_en', 'name_fr',)),
		}),
		(_('Image'), {
			'fields': ('url', 'link', 'image_thumb'),
		}),
	)


class ModelInline(admin.TabularInline):
	model = Package.package_model.through
	extra = 1
	verbose_name = "Model"
	verbose_name_plural = 'Optional Equipment - Model'


class PackageAdmin(admin.ModelAdmin):
	list_display = ('name_en', 'price_override', 'trims')
	readonly_fields = ('image_thumb', 'trims')
	inlines = (
		ModelInline,
	)
	fieldsets = (
		(_('General'), {
			'fields': (('name_en', 'name_fr',), ('description_en', 'description_fr',), 'price_override'),
		}),
		(_('Image'), {
			'fields': ('url', 'link', 'image_thumb'),
		}),
		(_('Details'), {
			'fields': ('code', 'field_type'),
		}),
	)


class OptionAdmin(admin.ModelAdmin):
	list_display = ('name_en', 'description_en', 'trims')
	fieldsets = (
		(_('General'), {
			'fields': (('name_en', 'name_fr',), ('description_en', 'description_fr')),
		}),
	)


class LocationAdmin(admin.ModelAdmin):
	list_display = ('name', 'language')
	fieldsets = (
		(_('General'), {
			'fields': ('name', 'language', 'disclaimer_en', 'disclaimer_fr'),
		}),
	)


class InteriorAdmin(admin.ModelAdmin):
	list_display = ('name_en', 'trims')
	fieldsets = (
		(_('General'), {
			'fields': (('name_en', 'name_fr',),),
		}),
	)


class PerformanceAdmin(admin.ModelAdmin):
	list_display = ('name_en', 'trims')
	fieldsets = (
		(_('General'), {
			'fields': (('name_en', 'name_fr',),),
		}),
	)


class ColourAdmin(admin.ModelAdmin):
	list_display = ('name_en', 'hexcode', 'trims')
	fieldsets = (
		(_('General'), {
			'fields': (('name_en', 'name_fr',), 'hexcode'),
		}),
	)


class ModelsInline(admin.TabularInline):
	model = StandAloneOption.stand_alone_model.through
	extra = 1
	verbose_name = "Model"
	verbose_name_plural = 'Stand Alone Option - Model'


class StandAloneOptionAdmin(admin.ModelAdmin):
	list_display = ('code', 'title_en', 'title_fr')
	readonly_fields = ('stand_alone_model',)
	inlines = (
		ModelsInline,
	)
	fieldsets = (
		(_('General'), {
			'fields': ('code', 'title_en', 'title_fr', 'price'),
		}),
	)


class OptionalEquipmentInline(admin.TabularInline):
	model = OptionalEquipment.optional_equipment_model.through
	extra = 1
	verbose_name = "Model"
	verbose_name_plural = 'Optional Equipment - Model'


class OptionalEquipmentAdmin(admin.ModelAdmin):
	list_display = ('code', 'title_en', 'title_fr')
	readonly_fields = ('optional_equipment_model',)
	inlines = (
		OptionalEquipmentInline,
	)
	fieldsets = (
		(_('General'), {
			'fields': ('code', 'title_en', 'title_fr', 'price', 'field_type'),
		}),
	)


class TestDriveAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'contact_method', 'email', 'phone', 'status')
	fieldsets = (
		(_('Customer'), {
			'fields': (
			'salutation', 'first_name', 'last_name', 'contact_method', 'email', 'phone', 'phone_type', 'contact_time',
			'language'),

		}),
		(_('Dealer'), {
			'fields': (
			'brochure', 'retailer_province', 'retailer_location', 'retailer_number', 'consent', 'vehicle', 'source',
			'city', 'status'),
		}),

	)


class KeepingInTouchAdmin(admin.ModelAdmin):
	list_display = ('source', 'first_name', 'last_name', 'email', 'language', 'status')
	fieldsets = (
		(_('Customer'), {
			'fields': (
			'source', 'first_name', 'last_name', 'email', 'language', 'vehicle', 'city', 'status', 'consent'),
		}),
	)


admin.site.register(Models, ModelsAdmin)
admin.site.register(TrimEnImage, TrimEnImageAdmin)
admin.site.register(TrimFrImage, TrimFrImageAdmin)
# admin.site.register(StaticModelEN, StaticModelENAdmin)
# admin.site.register(StaticModelFR, StaticModelENAdmin)
admin.site.register(StaticModel, StaticModelAdmin)
admin.site.register(Trim, TrimAdmin)
admin.site.register(ModelsShown, ModelsShownAdmin)
admin.site.register(FeaturesAccessory, FeaturesAccessoryAdmin)
# admin.site.register(Exterior, ExteriorAdmin)
admin.site.register(Upholstery, UpholsteryAdmin)
admin.site.register(Wheel, WheelAdmin)
admin.site.register(Package, PackageAdmin)
# admin.site.register(Option, OptionAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Gallery, GalleryAdmin)
# admin.site.register(Interior, InteriorAdmin)
# admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(TestDrive, TestDriveAdmin)
admin.site.register(KeepingInTouch, KeepingInTouchAdmin)
admin.site.register(StandAloneOption, StandAloneOptionAdmin)
admin.site.register(OptionalEquipment, OptionalEquipmentAdmin)
