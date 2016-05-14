from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ticket(models.Model) :

	ticket_id = models.IntegerField(primary_key=True) 
	application_id = models.CharField(max_length=255)
	created_time =  models.DateTimeField()
	last_update_time = models.DateTimeField()
	assigne_id = models.IntegerField()
	STATUS_OPTIONS = (
        (1, 'pending'),
        (2, 'online_pending'),
        (3, 'offline_pending'),
        (4, 'lender_pending'),
        (5, 'resolved')
    )

 	status = models.IntegerField(choices=STATUS_OPTIONS,default=1)
