from django.template.response import TemplateResponse
from finalassignmentapp.models import Reading

def home(request):
    data = Reading.objects.last() # .last() so that you get the most current results

    return TemplateResponse(request, 'index.html', {'data': data})

