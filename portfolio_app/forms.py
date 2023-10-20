from django.forms import ModelForm
from .models import Project, Portfolio


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = ['title', 'description', 'portfolio']
        fields = ('title', 'description')

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'contact_email', 'is_active', 'about']