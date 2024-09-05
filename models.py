from django.db import models

# User Model
class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_logged_in_at = models.DateTimeField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    citizenship = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Rolls Model
class Roll(models.Model):
    roll_id = models.AutoField(primary_key=True)
    roll_name = models.CharField(max_length=45)

    def __str__(self):
        return self.roll_name

# Event Model
class Event(models.Model):
    event_id = models.CharField(max_length=255, primary_key=True)
    event_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_summary = models.TextField()

    def __str__(self):
        return self.event_name

# Event Participants Model
class EventParticipants(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_participations')
    role = models.CharField(max_length=50, choices=[('Coordinator', 'Coordinator'), ('Host', 'Host'), ('Guests/Participants', 'Guests/Participants')])

    def __str__(self):
        return f"{self.user.name} - {self.event.event_name} - {self.role}"

# Funding Model
class Funding(models.Model):
    funding_id = models.CharField(max_length=255, primary_key=True)
    startup = models.ForeignKey('Startup', on_delete=models.CASCADE, null=True, blank=True, related_name='funding')
    investor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='investments')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    round = models.CharField(max_length=20, choices=[('Seed', 'Seed'), ('Series A', 'Series A'), ('Series B', 'Series B'), ('Series C', 'Series C'), ('IPO', 'IPO')])
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.startup.name if self.startup else 'N/A'} - {self.amount} - {self.date}"

# Innovation Model
class Innovation(models.Model):
    innovation_id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    related_research = models.ForeignKey('Research', on_delete=models.SET_NULL, null=True, blank=True, related_name='innovations')
    related_ipr = models.ForeignKey('IPR', on_delete=models.SET_NULL, null=True, blank=True, related_name='innovations')
    associated_startup = models.ForeignKey('Startup', on_delete=models.SET_NULL, null=True, blank=True, related_name='innovations')
    status = models.CharField(max_length=50, choices=[('Concept', 'Concept'), ('Prototype', 'Prototype'), ('Development', 'Development'), ('Deployed', 'Deployed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Investment Model
class Investment(models.Model):
    investment_id = models.CharField(max_length=255, primary_key=True)
    investment_type = models.CharField(max_length=20, choices=[('Startup', 'Startup'), ('Research', 'Research')])
    entity = models.ForeignKey('Research', on_delete=models.SET_NULL, null=True, blank=True, related_name='investments')
    investor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investment_records')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.investment_type} - {self.amount} - {self.date}"

# IPR Model
class IPR(models.Model):
    ipr_id = models.CharField(max_length=255, primary_key=True)
    ipr_type = models.CharField(max_length=20, choices=[('Patent', 'Patent'), ('Trademark', 'Trademark'), ('Copyright', 'Copyright')])
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    application_number = models.CharField(max_length=255, null=True, blank=True)
    registration_number = models.CharField(max_length=255, null=True, blank=True)
    file_date = models.DateField(null=True, blank=True)
    granted_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('Filed', 'Filed'), ('Granted', 'Granted'), ('In-process', 'In-process'), ('Rejected', 'Rejected')])
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_ipr')
    document_link = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Mentorship Model
class Mentorship(models.Model):
    mentorship_id = models.CharField(max_length=255, primary_key=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentored_projects')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorships')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Completed', 'Completed'), ('Terminated', 'Terminated')])

    def __str__(self):
        return f"{self.mentor.name} - {self.mentee.name} - {self.status}"

# Research Model
class Research(models.Model):
    research_id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    abstract = models.TextField(null=True, blank=True)
    lead_researcher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='led_research')
    status = models.CharField(max_length=20, choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')])
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    related_patent = models.ForeignKey('IPR', on_delete=models.SET_NULL, null=True, blank=True, related_name='related_research')
    related_publication = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

# Startup Model
class Startup(models.Model):
    startup_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    logo = models.TextField()
    incorporation_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('Ideation', 'Ideation'), ('Seed Stage', 'Seed Stage'), ('Growth', 'Growth'), ('Established', 'Established')])
    related_innovation = models.ForeignKey(Innovation, on_delete=models.SET_NULL, null=True, blank=True, related_name='startups')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Startup Role Model
class StartupRole(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='roles')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='startup_roles')
    startup_role = models.CharField(max_length=50, choices=[('Founder', 'Founder'), ('Co-Founder', 'Co-Founder'), ('CEO', 'CEO'), ('CTO', 'CTO'), ('CFO', 'CFO'), ('COO', 'COO'), ('CMO', 'CMO'), ('Other', 'Other')])

    def __str__(self):
        return f"{self.user.name} - {self.startup.name} - {self.startup_role}"

# UserRoll Model
class UserRoll(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roll = models.ForeignKey(Roll, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_roll'
        unique_together = ('user', 'roll')

    def __str__(self):
        return f"{self.user.name} - {self.roll.roll_name}"
