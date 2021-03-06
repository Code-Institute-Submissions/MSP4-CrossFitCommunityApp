from django import forms
from .models import Log, MemberComment, Workout
from datetime import date, datetime


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = (
            'ft_result',
            'amrap_result',
            'mw_result',
            'rx',
            'date',
            'user_comment'
            )
        # wod_date = DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"])


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'ft_result': 'mm:ss',
            'amrap_result': '0.00 rounds',
            'mw_result': 'weight in kg',
            'user_comment': 'notes?',
        }

        labels = {
            'ft_result': 'For Time Result:',
            'amrap_result': 'AMRAP Result:',
            'mw_result': 'Weight in kilograms:',
            'user_comment': 'Comment:',
        }

        for field in self.fields:
            if not (field == 'rx' or field == 'date'):
                placeholder = placeholders[field]
                label = labels[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                if field != 'rx':
                    self.fields[field].label = False
                else:
                    self.fields[field].label = label
            if field == "ft_result" or field == "amrap_result" or field =="mw_result":
                self.fields[field].widget.attrs['class'] = 'border-black rounded-1 profile-form-input score-result'
            else:
                self.fields[field].widget.attrs['class'] = 'border-black rounded-1 profile-form-input'


class MemberCommentForm(forms.ModelForm):
    class Meta:
        model = MemberComment
        fields = (
            'member',
            'message',
            'log_id',
            )


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = (
            'workout_name',
            'workout_type',
            'workout_category',
            'description',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].widget.attrs['rows'] = '3'
