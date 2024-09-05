from django.db import models
import random

class User(models.Model):
    ROLE_CHOICES = [
        (0, 'Researcher'),
        (1, 'Entrepreneur'),
        (2, 'Company'),
        (3, 'Accelerator'),
    ]

    id = models.CharField(primary_key=True, max_length=12, editable=False, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.IntegerField(choices=ROLE_CHOICES)
    phone_no = models.CharField(max_length=15)
    updated_at = models.DateTimeField(auto_now=True)
    last_logged_in_at = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)  # Add this field
    address = models.TextField()
    citizenship = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.id:
            role_prefix = str(self.role) + "_"
            random_number = str(random.randint(1000000, 99999999))
            self.id = role_prefix + random_number

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Event(models.Model):
    event_id = models.CharField(max_length=12, primary_key=True)
    event_name = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=45, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_summary = models.TextField()

    def __str__(self):
        return self.event_name

class EventParticipants(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[
        ('Coordinator', 'Coordinator'),
        ('Host', 'Host'),
        ('Guests/Participants', 'Guests/Participants')
    ])

    def __str__(self):
        return f"{self.user.name} - {self.role}"
class Innovation(models.Model):
    innovation_id = models.CharField(max_length=12, primary_key=True)
    title = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    related_research = models.ForeignKey('Research', on_delete=models.SET_NULL, null=True, blank=True)
    related_ipr = models.ForeignKey('IPR', on_delete=models.SET_NULL, null=True, blank=True)
    associated_startup = models.ForeignKey('Startup', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('Concept', 'Concept'),
        ('Prototype', 'Prototype'),
        ('Development', 'Development'),
        ('Deployed', 'Deployed')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Investment(models.Model):
    investment_id = models.CharField(max_length=12, primary_key=True)
    investment_type = models.CharField(max_length=20, choices=[('Startup', 'Startup'), ('Innovation', 'Innovation')])
    round = models.CharField(max_length=20, choices=[
        ('Seed', 'Seed'),
        ('Series 1', 'Series 1'),
        ('Series 2', 'Series 2'),
        ('Series 3', 'Series 3'),
        ('IPO', 'IPO')
    ])
    entity = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="investments")
    investor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="investor")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(null=True, blank=True)
    innovation = models.ForeignKey(Innovation, on_delete=models.CASCADE)
    startup = models.ForeignKey('Startup', on_delete=models.CASCADE)

    def __str__(self):
        return f"Investment {self.investment_id}"
class IPR(models.Model):
    ipr_id = models.CharField(max_length=12, primary_key=True)
    ipr_type = models.CharField(max_length=20, choices=[('Patent', 'Patent'), ('Trademark', 'Trademark'), ('Copyright', 'Copyright')])
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    application_number = models.CharField(max_length=20, null=True, blank=True)
    registration_number = models.CharField(max_length=20, null=True, blank=True)
    file_date = models.DateField(null=True, blank=True)
    granted_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Filed', 'Filed'), ('Granted', 'Granted'), ('In-process', 'In-process'), ('Rejected', 'Rejected')])
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    document_link = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Research(models.Model):
    research_id = models.CharField(max_length=12, primary_key=True)
    title = models.CharField(max_length=100)
    abstract = models.TextField(null=True, blank=True)
    lead_researcher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')])
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    related_patent = models.ForeignKey(IPR, on_delete=models.SET_NULL, null=True, blank=True)
    related_publication = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
class Startup(models.Model):
    startup_id = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    logo = models.TextField()
    incorporation_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('Ideation', 'Ideation'),
        ('Seed Stage', 'Seed Stage'),
        ('Growth', 'Growth'),
        ('Established', 'Established')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Mentorship(models.Model):
    mentorship_id = models.CharField(max_length=12, primary_key=True)
    mentor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='mentors')
    mentee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='mentees')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Completed', 'Completed'), ('Terminated', 'Terminated')])

    def __str__(self):
        return f"Mentorship {self.mentorship_id}"
class Request(models.Model):
    request_id = models.CharField(max_length=12, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_title = models.CharField(max_length=100)
    request_type = models.CharField(max_length=20, choices=[
        ('Funding', 'Funding'),
        ('Mentorship', 'Mentorship'),
        ('Collaboration', 'Collaboration'),
        ('Consultation', 'Consultation'),
        ('Investment', 'Investment'),
        ('Advisor', 'Advisor'),
        ('Other', 'Other')
    ])
    startup = models.ForeignKey(Startup, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Innovation, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('In Process', 'In Process'),
        ('Completed', 'Completed'),
        ('Requested', 'Requested'),
        ('Accepted', 'Accepted')
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.request_title
