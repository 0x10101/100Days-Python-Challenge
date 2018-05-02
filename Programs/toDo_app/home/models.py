from django.db import models

# Create your models here.

class Entry(models.Model):
	text = models.TextField()
	date_added = models.DateField(auto_now_add = True)
	class Meta:
		verbose_name_plural = "Entries"
	def __str__(self):
		return self.text