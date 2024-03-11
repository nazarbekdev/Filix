from django.urls import path

from app.views import ProductMaterialsView

urlpatterns = [
    path('product/', ProductMaterialsView.as_view(), name='product')
]
