from django.core.management import BaseCommand
from wheelstand.models import KeepingInTouch
import requests
from requests.auth import HTTPBasicAuth
from django.core import serializers


class Command(BaseCommand):

	def handle(self, *args, **options):
		url = 'https://form-staging.richmondday.com/MINIHandRaiser'
		headers = {'content-type': 'application/x-www-form-urlencoded'}
		auth = HTTPBasicAuth('user', 'pass')

		newdata = KeepingInTouch.objects.filter(status=False)

		for i in newdata:
			payload = {
				'Source' : i.source,			
				'FirstName' : i.first_name, 
				'LastName' : i.last_name, 
				'Email' : i.email,
				'Comments' : i.language, 
			}
			j = payload
			print j
			r = requests.post(url, data=j, headers=headers, auth=auth)
			print r.status_code
			print r.text
			print i.status
			if r.status_code == 200:
				i.status = True
				i.save()
			print i.status	
