from typing import Any
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic
from .models import Student,\
                    Portfolio,\
                    Project
from .forms import ProjectForm, PortfolioForm

class StudentListView(generic.ListView):
    model = Student
    
class StudentDetailView(generic.DetailView):
    model = Student
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super(StudentDetailView, self)\
            .get_context_data(**kwargs)
        
        context['portfolio_list'] = Portfolio.objects.all()\
            .filter(id=self.kwargs['pk'])
        
        # ## DEBUGGING:
        # print(f"Portfolio Detail View: {context['project_list']}")
        # print(f"Full context: {context}")

        return context
    
class PortfolioListView(generic.ListView):
    model = Portfolio

    
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super(PortfolioDetailView, self)\
            .get_context_data(**kwargs)
        
        context['project_list'] = Project.objects.all()\
            .filter(portfolio_id=self.kwargs['pk'])
        
        ## DEBUGGING:
        print(f"Portfolio Detail View: {context['project_list']}")
        print(f"Full context: {context}")

        return context

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project


# Create your views here.
def index(request: object) -> HttpResponse:
    student_active_portfolios = Student.objects\
        .select_related('portfolio')\
        .all()\
        .filter(portfolio__is_active=True)

    context = {
        'student_active_portfolios': student_active_portfolios,
    }
    for entry in context['student_active_portfolios']:
        print(f'Active portfolio query set: {entry}')
    print("active portfolio query set ", student_active_portfolios)
    return render(request, 'portfolio_app/index.html', context=context)

def update_portfolio(request: object, portfolio_id: int) -> HttpResponse:
    portfolio_query = Portfolio.objects.get(pk=portfolio_id)
    web_form = PortfolioForm(instance=portfolio_query)
    
    if request.method == 'POST':
        portfolio_data = request.POST.copy()
        
        web_form = PortfolioForm(portfolio_data, instance=portfolio_query)
        
        if web_form.is_valid():
            web_form.save()
            
            return redirect('portfolio-detail', pk=portfolio_id)
        
    context = {'form': web_form}
    return render(request, 'portfolio_app/portfolio_form.html', context=context)

def create_project(request: object, portfolio_id: int) -> HttpResponse:
    web_form = ProjectForm()
    portfolio_query = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        
        web_form = ProjectForm(project_data)
        
        if web_form.is_valid():
            project = web_form.save(commit=False)
            
            project.portfolio = portfolio_query
            project.save()
            
            return redirect('portfolio-detail', pk=portfolio_id)
        
    context = {'form': web_form}
    return render(request, 'portfolio_app/project_form.html', context=context)

def update_project(request: object, project_id: int) -> HttpResponse:
    project_query = Project.objects.get(pk=project_id)
    web_form = ProjectForm(instance=project_query)
    
    if request.method == 'POST':
        project_data = request.POST.copy()
        project_data['portfolio_id'] = project_query.portfolio.id
        
        web_form = ProjectForm(project_data, instance=project_query)
        
        if web_form.is_valid():
            web_form.save()
            
            return redirect('portfolio-detail', pk=project_query.portfolio.id)
        
    context = {'form': web_form}
    return render(request, 'portfolio_app/project_form.html', context=context)

def delete_project(request: object, portfolio_id: int, project_id: int) -> HttpResponse:
    project_query = Project.objects.get(pk=project_id)
    context = {'project': project_query, 'portfolio_id': portfolio_id}

    if request.method == 'POST':
        project_query.delete()
        return redirect('portfolio-detail', pk=portfolio_id)

    return render(request, 'portfolio_app/project_delete.html', context=context)
