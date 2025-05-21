from django.urls import path
from .views import note_list, note_create, note_update, note_delete, signup

urlpatterns = [
    path('signup/', signup, name='signup'),  # Маршрут регистрации
    path('', note_list, name='note_list'),   # Список заметок
    path('create/', note_create, name='note_create'),  # Создание заметки
    path('<int:pk>/update/', note_update, name='note_update'),  # Обновление заметки
    path('<int:pk>/delete/', note_delete, name='note_delete'),  # Удаление заметки
]