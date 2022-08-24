from django import forms

from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)
    publish_date = forms.CharField( max_length=100, required=False)


class BlogPostModelForm(forms.ModelForm): 
    title = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = BlogPost
        fields = ('title','slug','content', 'publish_date')

    def clean_title(self, *args , **kwargs):
        title = self.cleaned_data.get('title')
        qs = BlogPost.object.filter(title__iexact = title)
        if qs.exists():
            raise forms.ValidationError("The title already exists")
        return title
