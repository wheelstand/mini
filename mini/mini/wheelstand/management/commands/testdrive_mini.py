from django.core.management import BaseCommand
from wheelstand.models import TestDrive
import requests
from requests.auth import HTTPBasicAuth
from django.core import serializers
import json


class Command(BaseCommand):

	def handle(self, *args, **options):
		url = 'https://form-staging.richmondday.com/MINIWheelstand'
		headers = {'content-type': 'application/x-www-form-urlencoded'}
		auth = HTTPBasicAuth('user', 'pass')

		newdata = TestDrive.objects.filter(status=False)

		for i in newdata:
			payload = {
				'RetailerNumber' : i.retailer_number, 
				'Vehicle' : i.vehicle, 
				'Lang' : i.language, 
				'Salutation' : i.salutation, 
				'FirstName' : i.firstName, 
				'LastName' : i.last_name, 
				'PreferredContactMethod' : i.contact_method, 
				'PreferredContactTime' : i.contact_time, 
				'PhoneNumber' : i.phone, 
				'PhoneType' : i.phone_type, 
				'Email' : i.email,
				'Source' : i.source,				
				'Comments' : 'Brochure=' + str(i.brochure) + 'RetailerProvince' + i.retailer_province + 'RetailerCity' + i.retailer_location + 'CommercialEmailOptIn' + str(i.consent)
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

