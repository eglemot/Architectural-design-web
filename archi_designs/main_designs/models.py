from django.db import models

class Plan(models.Model):

    FLOOR_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )

    STYLE_CHOICES = (
        ('barndominium', 'Barndominium'),
    )

    name = models.CharField(max_length=255)
    min_bedrooms = models.PositiveSmallIntegerField()
    max_bedrooms = models.PositiveSmallIntegerField()
    floors = models.CharField(max_length=10, choices=FLOOR_CHOICES)
    min_bathrooms = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    max_bathrooms = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    heated_sq_feet = models.DecimalField(max_digits=20, decimal_places=3, null=True, blank=True)
    basement = models.BooleanField(default=False)
    loft = models.BooleanField(default=False)
    walk_in_pantry = models.BooleanField(default=False)
    home_office = models.BooleanField(default=False)
    mudroom = models.BooleanField(default=False)
    bonus_room = models.BooleanField(default=False)
    wrap_around_porch = models.BooleanField(default=False)
    affiliate_link = models.URLField()
    style = models.CharField(max_length=20, choices=STYLE_CHOICES, default='barndominium')
    description = models.TextField(blank=True, default='')

    def __str__(self) -> str:
        return self.name

class FloorPicture(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='floor_pictures')
    floor_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='pictures/floor_pictures')

class PlanPicture(models.Model):
    image = models.ImageField(upload_to='pictures/plan_pictures')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plan_pictures')
