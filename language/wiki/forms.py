from django import forms
from wiki.models import Category, Page
from django.forms.widgets import Widget


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label='類別名稱', help_text='請輸入類別名稱')
 
    class Meta:
        model = Category
        fields = ('name', )



class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label='頁面標題', help_text='請輸入頁面標題')
    #url = forms.URLField(max_length=128, label='頁面網址', help_text='請輸入頁面網址')
    content = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = Page
        exclude = ('category', 'views',)
                   
        
    def clean(self):
        cleanedData = self.cleaned_data
        #url = cleanedData.get('url')
        #if url and not url.startswith('http://'):
        #    url = 'http://' + url
        #    cleanedData['url'] = url
        #return cleanedData