from django.urls import path
from .views      import (
                    AllItems, 
                    WhichCategory, 
                    WhichBrand, 
                    WhichColor, 
                    WhichSize,
                    CustomFoundation,
                    ProductDetailView,
                    SizeDetailView)

urlpatterns = [
    path('', AllItems.as_view()),
    path('/category', WhichCategory.as_view()),
    path('/brand', WhichBrand.as_view()),
    path('/size', WhichSize.as_view()),
    path('/color', WhichColor.as_view()),
#    path('<int:category_id>', ItemsForCategory.as_view()),
    path('/sideimage/<int:product_id>', CustomFoundation.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/sizedetail/<int:product_id>', SizeDetailView.as_view())
    ]

