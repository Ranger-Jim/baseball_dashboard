from django.db import models

# Create your models here.
class Schedule(models.Model):
  date = models.DateField()
  start_time = models.TimeField()
  away_team = models.CharField(max_length=100)
  home_team = models.CharField(max_length=100)
  location = models.CharField(max_length=200)
  broadcast = models.CharField(max_length=200)
  end_time = models.TimeField()

  def __str__(self):
    return f"{self.away_team} at {self.home_team} on {self.date} at {self.start_time}"