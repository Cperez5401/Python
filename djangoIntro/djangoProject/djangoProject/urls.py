from django.urls import path, include

urlpatterns = [
    path('', include('application.urls')),
    path('blogs/', include('application.urls')),
    path('blogs/new/', include('application.urls')),
    path('blogs/create/', include('application.urls')),
    path('blogs/<int:number>/', include('application.urls')),
    path('blogs/<int:number>/edit', include('application.urls')),
    path('blogs/<int:number>/delete', include('application.urls'))
]