from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('organizations/new', views.organizations_new, name='organizations_new'), 
    path('organizations/create', views.organizations_create, name='organizations_create'),
    path('organizations/assoc_employee', views.assoc_org_employee, name='assoc_org_employee'),
    path('departments/index', views.departments_index, name='departments_index'), 
    path('departments/create', views.departments_create, name='departments_create'),
    path('departments/<int:department_id>/', views.departments_detail, name='departments_detail'),
    path('departments/<int:pk>/update/', views.DepartmentUpdate.as_view(), name='departments_update'),
    path('departments/<int:pk>/delete/', views.DepartmentDelete.as_view(), name='departments_delete'), 
    path('departments/<int:department_id>/tasks_create/', views.tasks_create, name='tasks_create'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='tasks_detail'),
    path('departments/<int:department_id>/tasks/<int:pk>/delete', views.TaskDelete.as_view(), name='tasks_delete'),
    path('employees/<int:employee_id>/', views.employees_detail, name='employees_detail'), 
    path('employees/', views.employees_index, name='employees_index'), 
    path('employees/<int:employee_id>/assoc_dept_employee/', views.assoc_dept_employee, name='assoc_dept_employee'),
    path('tasks/<int:task_id>/update/', views.tasks_update, name='tasks_update'),
    path('departments/<int:department_id>/tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
    path('tasks/<int:task_id>/assoc_task_employee/', views.assoc_task_employee, name='assoc_task_employee'), 
    path('tasks/<int:task_id>/remove_task_employee/', views.remove_task_employee, name='remove_task_employee')
]