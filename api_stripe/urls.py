from django.urls import path
from .views import ProductLandingPageView, CreateCheckoutSessionView, CancelView, \
    SuccessesView, DisplayItemsView

urlpatterns = [
    path('item/<str:pk>/', ProductLandingPageView.as_view(), name="item"),
    path('buy/<str:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('', DisplayItemsView.as_view(), name='list_items'),
    path('cancel/', CancelView.as_view()),
    path('success/', SuccessesView.as_view()),

]
