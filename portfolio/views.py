from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Project, ContactMessage
from .forms import ContactForm
from django.views.generic.edit import FormView

class HomePageView(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects']=Project.objects.all()
        return context
class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'

class AboutPageView(TemplateView):
    template_name = 'portfolio/about.html'

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# write class based view for handling succes form 

class ContactFormView(FormView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')
    
    def form_valid(self, form):
        # Save the form data to the database
        form.save()
        
        # Check if the request is an AJAX request
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        
        # For normal form submissions
        return super().form_valid(form)

    def form_invalid(self, form):
        # Check if the request is an AJAX request
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        
        # For normal form submissions
        return super().form_invalid(form)

