from django import forms

class CustomerForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

    TERM_CHOICES = [
        ('Short Term', 'Short Term'),
        ('Long Term', 'Long Term')
    ]

    YOJ_CHOICES = [
        ('< 1 year', '< 1 year'),
        ('1 year', '1 year'),
        ('2 years', '2 years'),
        ('3 years', '3 years'),
        ('4 years', '4 years'),
        ('5 years', '5 years'),
        ('6 years', '6 years'),
        ('7 years', '7 years'),
        ('8 years', '8 years'),
        ('9 years', '9 years'),
        ('10+ years', '10+ years')
    ]

    HO_CHOICES = [
        ('Home Mortgage', 'Home Mortgage'),
        ('Own Home', 'Own Home'),
        ('Rent', 'Rent'),
        ('HaveMortgage', 'HaveMortgage')
    ]

    PURPOSE_CHOICES = [
        ('Home Improvements', 'Home Improvements'),
        ('Debt Consolidation', 'Debt Consolidation'),
        ('Buy House', 'Buy House'),
        ('Business Loan', 'Business Loan'),
        ('Buy a Car', 'Buy a Car'),
        ('Other', 'Other'),
        ('Take a Trip', 'Take a Trip'),
        ('Medical Bills', 'Medical Bills'),
        ('Educational Expenses', 'Educational Expenses'),
    ]

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    gender = forms.ChoiceField(max_length=10, choices=GENDER_CHOICES)
    term  = forms.ChoiceField(max_length=15, choices=TERM_CHOICES)
    credit_score = forms.FloatField()
    year_in_current_job = forms.ChoiceField(max_length=15, choices=YOJ_CHOICES)
    home_ownership = forms.ChoiceField(max_length=30, choices=HO_CHOICES)
    purpose = forms.ChoiceField(max_length=30, choices=PURPOSE_CHOICES)
    years_credit_history = forms.FloatField()
    num_open_acc = forms.IntegerField()