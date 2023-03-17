from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.store, name='index'),
    path('book/<book_id>/', views.book_details, name='book_details'),
    path('add/<book_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<book_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('complete_order/', views.complete_order, name='complete_order'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                            document_root=settings.MEDIA_ROOT)
