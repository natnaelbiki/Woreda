from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import Staff
from bootstrap_datepicker_plus.widgets import DatePickerInput

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'  # Or list specific fields if preferred
        widgets = {
            "hired_year": DatePickerInput(),
            "date_of_birth": DatePickerInput(),
        }
        labels = {
            'full_name_amh': 'ስም ከነአያት በአማርኛ',
            'full_name_eng': 'ስም ከነአያት በእንግሊዘኛ',
            'gender': 'ፆታ',
            'place_of_work': 'የሚሰራበት የከተማ ቀበሌ ስም',
            'pension_id_no': 'የጡረታ መለያ ቁጥር',
            'date_of_birth': 'የትውልድ ዘመን',
            'ethnicity': 'ብሔር',
            'edu_type': 'የትምህርት ዓይነት በአማርኛ',
            'edu_level': 'የትምህርት ደረጃ',
            'hired_year': 'የቅጥር ዘመን',
            'years_of_service': 'አገልግሎት  ዘመን',
            'marital_status': 'የጋብቻ ሁኔታ',
            'position': 'የስራ መደብ መጠሪያ',
            'position_grade': 'የስራ መደብ ደረጃ',
            'salary': 'ደመወዝ',
            'hire_type': 'የቅጥር ሁኔታ',
        }

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('full_name_amh', css_class='form-group col-md-4 mb-0'),
                Column('full_name_eng', css_class='form-group col-md-4 mb-0'),
                Column('gender', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('place_of_work', css_class='form-group col-md-3 mb-0'),
                Column('pension_id_no', css_class='form-group col-md-3 mb-0'),
                Column('date_of_birth', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ethnicity', css_class='form-group col-md-3 mb-0'),
                Column('edu_type', css_class='form-group col-md-3 mb-0'),
                Column('hired_year', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            # Repeat the structure above for the rest of your fields
            Row(
                
                Column('years_of_service', css_class='form-group col-md-3 mb-0'),
                Column('marital_status', css_class='form-group col-md-3 mb-0'),
                Column('edu_level', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('position', css_class='form-group col-md-3 mb-0'),
                Column('position_grade', css_class='form-group col-md-3 mb-0'),
                Column('salary', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('hire_type', css_class='form-group col-md-3 mb-0'),
                Submit('submit', 'Submit'),
                css_class='form-row'
            ),
            
        )
