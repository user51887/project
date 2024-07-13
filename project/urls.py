from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[

    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('blog/' , include('blog.urls' , namespace='blog')),
    
 
   
    path('equipes/' , include('equipes.urls' , namespace='equipes')),
    path('' , include('accueil.urls' , namespace='accueil')),
    path('login/' , include('customadmin.urls' , namespace='customadmin')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "Cabinet_Dentaire AdminPanel"
admin.site.site_title = "Cabinet_Dentaire App Admin"
admin.site.site_index_title = "Bienvenue !!t"