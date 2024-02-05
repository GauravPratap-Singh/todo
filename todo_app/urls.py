from django.urls import path 
from . import views

urlpatterns = [
    path('addtask/', views.addTask, name='addTask'),
   path('mark_as_done/<int:pk>',views.Mark_as_done,name='mark_as_done'),
   path('mark_as_undone/<int:pk>',views.Mark_as_Undone,name='mark_as_undone'),
   path('edit_task/<int:pk>',views.Edit_Task,name='edit_task'),
   path('delete_task/<int:pk>',views.Delete_Task,name='delete_task'),
]