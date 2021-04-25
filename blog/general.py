from .models import *

def global_data(request):
    data = {
        'title':'Welcome',
        'settingData':ProjectConfig.objects.first()

        }

    return data
