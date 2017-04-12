OwaspCalc
-----------

A Django application to calculate an overall risk score for a web application vulnerability using the OWASP Risk Rating methodolgy.

Quick start
-----------
1.  Install widget_tweaks in your venv.   
    pip install django-widget-tweaks
    Then add ‘widget_tweaks’ to INSTALLED_APPS.

1. Add "owaspcalc" to your INSTALLED_APPS setting like this

    INSTALLED_APPS = [
        
        'owaspcalc.apps.OwaspcalcConfig',
        'widget_tweaks',
    ]

2. Include the polls URLconf in your project urls.py like this

    url(r'^owaspcalc/', include('owaspcalc.urls')),

3. Run `python manage.py migrate` to create the owaspcalc models.


4. Visit http://127.0.0.1:8000/owaspcalc/ to get started.
