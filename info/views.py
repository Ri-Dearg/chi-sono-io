from django.views.generic import CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Email, About


class AboutTemplate(TemplateView):
    template_name = "info/about.html"

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context.
        Mainly just highlights the "Contact" in the navbar."""
        context = super().get_context_data(**kwargs)
        about_active = True

        about = About.objects.get(pk=1)

        context['about'] = about
        context['about_active'] = about_active
        return context


# Create your views here.
class CreateEmailView(SuccessMessageMixin, CreateView):
    """The page used for contact to send an email."""
    model = Email
    context_object_name = 'email'
    fields = ['email', 'name', 'subject', 'message']
    success_message = 'Grazie, il messagio è stato spedito.'

    def get_form(self, form_class=None):
        """Adds custom placeholders and widgets to form"""
        form = super().get_form(form_class)
        form.fields['email'].widget.attrs = {'placeholder': 'Email*',
                                             'class': 'form-control'}
        form.fields['name'].widget.attrs = {'placeholder': 'Nome*', 'class':
                                            'form-control'}
        form.fields['subject'].widget.attrs = {'placeholder': 'Argomento*',
                                               'class': 'form-control'}
        form.fields['message'].widget.attrs = {
            'placeholder': 'Cosa pensi?*', 'class': 'form-control message-box'}
        form.fields['message'].label = ''
        return form

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context.
        Mainly just highlights the "Contact" in the navbar."""
        context = super().get_context_data(**kwargs)
        contact_active = True

        context['contact_active'] = contact_active
        return context
