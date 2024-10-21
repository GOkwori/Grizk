from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import custom error handlers
from home.views import custom_403, custom_404, custom_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add custom error handlers
handler404 = 'home.views.custom_404'
handler500 = 'home.views.custom_500'
handler403 = 'home.views.custom_403'
