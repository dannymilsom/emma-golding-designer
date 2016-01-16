from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    """Render a simple template for the homepage."""

    template_name = "public/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['emma_email'] = settings.EMMA_EMAIL_ADDRESS
        return context
