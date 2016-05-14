from azure import *
from azure.servicemanagement import *

subscription_id = '4c1f7e7c-e47c-4688-8de0-19b1f8b58636'
certificate_path = 'C:\Azure_Cert\zymcert-home.pem'

sms = ServiceManagementService(subscription_id,
                               certificate_path,
                               'management.core.chinacloudapi.cn')

properties = sms.get_hosted_service_properties('zymwats')


print properties.hosted_service_properties.status