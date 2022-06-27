from django.contrib import admin
from django import forms
from .models import typeTask, Task, subType, Decision, Profile
from ckeditor_uploader.widgets import CKEditorUploadingWidget



@admin.register(subType)
class SubtypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'type')
    list_display_links = (None)
    prepopulated_fields = {"slug": ("title",)}

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    solution = forms.CharField(widget=CKEditorUploadingWidget(), empty_value=True)
    class Meta:
        model = Task
        fields = '__all__'
class DecisionAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Decision
        fields = '__all__'
class ProfileAdminForm(forms.ModelForm):
    tasks = forms.ModelMultipleChoiceField(queryset=Task.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Profile
        fields = '__all__'
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(typeTask)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm



@admin.register(Decision)
class DecisionAdmin(admin.ModelAdmin):
    form = DecisionAdminForm
