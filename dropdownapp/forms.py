from django import forms
from .models import Travel,City,Country

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(TravelForm,self).__init__(*args,**kwargs)
        self.fields['city'].queryset = City.objects.none()
        self.fields['country'].widget.attrs.update({'id': 'country'})
        self.fields['city'].widget.attrs.update({'id': 'city'})

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country__id=country_id)
            except:
                pass
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set