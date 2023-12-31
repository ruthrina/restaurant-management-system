from . import views
from django.urls import path

urlpatterns = [
    path('order_items/', views.order_items, name='order_items'),
    path('make_order/<int:item_id>/',views.add_order_item,name='add_order_item'),
    path('<int:item_id>/',views.order_item_detail,name='order_detail'),
    path('new_order/',views.create_new_order,name='create_new_order'),
    path('delete_item/<int:item_id>/<int:order_id>/',views.delete_item_from_order,name='delete_order_item'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('update_order_item/<pk>/',views.OrderItemUpdateView.as_view(), name='update_order_item'),
    path('order_checkout/<int:order_id>/',views.order_checkout, name='order_checkout'),
    path('delete_order/<int:order_id>/',views.delete_order,name='delete_order')
]