from django.urls import path
from.import views
app_name = 'JulaneHotel'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index', views.MyIndexView.as_view(),name="my_index_view"),
    path('reservation', views.MyReservationView.as_view(),name="my_reservation_view"),
    path('gallery', views.MyGalleryView.as_view(),name="my_gallery_view"),
    path('contact', views.MyContactView.as_view(),name="my_contact_view"),
    path('about', views.MyAboutView.as_view(),name="my_about_view"),
    path('LogIn', views.login,name="my_LogIn_view"),
    path('adminLogIn', views.MyadminLogInView,name="my_adminLogIn_view"),
    path('adminDashboard', views.MyadminDashboardView.as_view(),name="my_adminDashboard_view"),
    path('addRoom', views.MyaddRoomView.as_view(),name="my_addRoom_view"),
    path('customerRegistration', views.MyCustomerRegistration,name="my_customerRegistration_view"),
    path('dashboardCustomer', views.MydashboardCustomerView.as_view(),name="my_dashboardCustomer_view"),
    path('dashboardReservation', views.MydashboardReservationView.as_view(),name="my_dashboardReservation_view"),
    path('customerReservation', views.MyCustomerReservationView.as_view(),name="my_customerReservation_view"),
    path('customerDashboard', views.MyCustomerDashboardView.as_view(),name="my_customerDashboard_view"),
    path('customerProfile', views.MyCustomerProfileView.as_view(),name="my_customerProfile_view"),
    path('searchRoom', views.searchRoom,name="my_searchRoom_view"),
]
