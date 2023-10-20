from django.urls import path
from . import views

urlpatterns = [

    ## Path to home/index page
    path('', views.index, name='index'),

    ## Configure Student views
    path(
        'students/', 
        views.StudentListView.as_view(), 
        name= 'students'
    ),
    path(
        'student/<int:pk>', 
        views.StudentDetailView.as_view(), 
        name='student-detail'
    ),

    ## Configure Portfolio views
    path(
        'portfolios/', 
        views.PortfolioListView.as_view(), 
        name= 'portfolios'
    ),
    path(
        'portfolio/<int:pk>', 
        views.PortfolioDetailView.as_view(), 
        name='portfolio-detail'
    ),
    path(
        'portfolio/<int:portfolio_id>/create_project', 
        views.create_project, 
        name='create-project'
    ),
    path(
        'portfolio/update_portfolio/<int:portfolio_id>',
        views.update_portfolio,
        name='update-portfolio'
    ),

    ## Configure Project views
    path(
        'projects/', 
        views.ProjectListView.as_view(), 
        name= 'projects'
    ),
    path(
        'project/<int:pk>', 
        views.ProjectDetailView.as_view(), 
        name='project-detail'
    ),
    path(
        'project/<int:project_id>/update_project',
        views.update_project,
        name='update-project'
    ),
    path(
        'portfolio/<int:portfolio_id>/delete_project/<int:project_id>',
        views.delete_project,
        name='delete-project'
    ),

]
