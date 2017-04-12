from django import forms
from owaspcalc.models import *

class RiskAuditCreateForm(forms.ModelForm):
    class Meta:
        model = RiskAudit
        exclude = ['created_time_stamp','slug']
    
class RiskAuditEditForm(forms.ModelForm):
    class Meta:
        model = RiskAudit
        exclude = ['created_time_stamp']

