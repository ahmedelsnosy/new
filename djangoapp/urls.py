# Uncomment the imports before you add the code
# from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# from . import views
from django.urls import path
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
    # path(route='login', view=views.login_user, name='login'),

    # path for dealer reviews view

    # path for add a review view
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.registration, name='register'),

    # Dealership and Review Views
    path('dealerships/', views.get_dealerships, name='dealerships'),
    path('car_records/', views.get_car, name='car_records'),
    path('dealerships/<int:dealer_id>/reviews/', views.get_dealer_reviews, name='dealer_reviews'),
    path('dealerships/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('addreview/', views.add_review, name='addreview'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
