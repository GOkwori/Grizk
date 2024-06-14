from django.contrib import admin
from .models import order, order_line_item


class orderLineAdminInline(admin.TabularInline):
    model = order_line_item
    readonly_fields = ('lineitem_total',)


class orderAdmin(admin.ModelAdmin):
    inlines = (orderLineAdminInline,)

    readonly_fields = ('order_reference', 'date',
                       'order_total', 'delivery_cost', 'grand_total')

    fields = ('order_reference', 'full_name', 'phone_number',
              'country', 'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'date', 'order_total',
              'delivery_cost', 'grand_total')

    list_display = ('order_reference', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total')

    ordering = ('-date',)


admin.site.register(order, orderAdmin)
