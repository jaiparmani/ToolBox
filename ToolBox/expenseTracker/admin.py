from django.contrib import admin
from django.apps import apps

# Register your models here.
# Get all models from the current app
app_models = apps.get_app_config('expenseTracker').get_models()

# Register all models dynamically
for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass  # Skip models that are already registered