from django.urls import path
from .views import RoomListView, RoomDetailView

urlpatterns=[
    path('room/<int:id>/', RoomDetailView.as_view, name='room_detail'),
    # path('signup/', SignUpView.as_view(), name='signUp'),
    # path('login/', LoginView.as_view, name='login'),
    path('', RoomListView.as_view(), name='home'),
]