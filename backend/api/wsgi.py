import os

from django.core.wsgi import get_wsgi_application

# Required to make a seeminglessly switch between deployment_settings and the original settings.
settiings_module = 'api.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'api.settings'

application = get_wsgi_application()
