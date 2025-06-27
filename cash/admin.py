from django.contrib import admin
from .models import Item  
from .forms import ItemForm

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemForm 

    list_display = ('name', 'quantity', 'created_at', 'updated_at') 
    search_fields = ('name', 'description')  
    list_filter = ('created_at',)  
    ordering = ('name',) 
    readonly_fields = ('created_at', 'updated_at')  

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description', 'quantity', 'price'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  
        }),
    )
