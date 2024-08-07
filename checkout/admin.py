from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_reference', 'date',
                       'order_total', 'delivery_cost', 'grand_total')

    fields = ('order_reference', 'user_profile', 'date', 'full_name', 'phone_number', 'country', 'postcode', 'town_or_city',
              'street_address1', 'street_address2', 'county', 'order_total', 'delivery_cost', 'grand_total')

    list_display = ('order_reference', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
