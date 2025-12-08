from django import forms
from tasks.models import Task,TaskDetail

class StyledFormMixin:
    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder':  f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 p-1 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                
                field.widget.attrs.update({
                    'class': "space-y-2 space-x-2"
                })
            else:
               
                field.widget.attrs.update({
                    'class': self.default_classes
                })
    


    
    

class TaskModelForm(StyledFormMixin,forms.ModelForm):    
    class Meta:
        model = Task
        fields = ["title","description","due_date","assigned_to"]
        widgets = {
            'due_date': forms.SelectDateWidget,
            'assigned_to': forms.CheckboxSelectMultiple
        }
        
    def __init__(self, *arg, **kwarg):
        
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()




class TaskDetailModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['priority', 'notes']

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()    

