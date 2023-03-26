from django.contrib import admin
from .models import Plan, FloorPicture, PlanPicture

class FloorPictureInline(admin.TabularInline):
    model = FloorPicture

class PlanPictureInline(admin.TabularInline):
    model = PlanPicture

class FloorPictureAdmin(admin.ModelAdmin):
    list_display = ('plan', 'floor_number')
    list_filter = ('plan',)
    search_fields = ('plan__name',)
    
class PlanPictureAdmin(admin.ModelAdmin):
    list_display = ('plan',)
    list_filter = ('plan',)
    search_fields = ('plan__name',)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'heated_sq_feet', 'floors', 'min_bedrooms', 'max_bedrooms', 'min_bathrooms', 'max_bathrooms', 'basement', 'loft', 'walk_in_pantry', 'home_office', 'mudroom', 'bonus_room', 'wrap_around_porch', 'style')
    search_fields = ('name',)
    inlines = [
        PlanPictureInline,
        FloorPictureInline,
    ]
    fieldsets = (
        ('Add plan', {
            'fields': ('name', 'heated_sq_feet', 'affiliate_link')
        }),
        ('Details', {
            'fields': ('floors', 'min_bedrooms', 'max_bedrooms', 'min_bathrooms', 'max_bathrooms', 'description')
        }),
        ('Options', {
            'fields': ('basement', 'loft', 'walk_in_pantry', 'home_office', 'mudroom', 'bonus_room', 'wrap_around_porch', 'style')
        }),
    )

admin.site.register(Plan, PlanAdmin)
admin.site.register(FloorPicture, FloorPictureAdmin)
admin.site.register(PlanPicture, PlanPictureAdmin)


