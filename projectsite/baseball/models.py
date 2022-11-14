from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Position(BaseModel):
    description = models.CharField(max_length=100)

class Person(BaseModel):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True, max_length=100)
    height = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5, null=True)

class Club(BaseModel):
    name = models.CharField(max_length=100)
    coach = models.ForeignKey(Person, on_delete=models.CASCADE)
    dorm_latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    dorm_longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)

class Play(BaseModel):
    STRING_CHOICES= (
    ('First String', 'First String'),
    ('Second String','Second String'))
    player = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = "Player")
    team = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = "Team")
    string_no = models.CharField(max_length=100, choices = STRING_CHOICES)
    isActive = models.BooleanField(default=False)
    pos = models.ForeignKey(Position, on_delete=models.CASCADE)