from azure import *
from azure.servicemanagement import *

subscription_id = '4c1f7e7c-e47c-4688-8de0-19b1f8b58636'
certificate_path = 'C:\Azure_Cert\zymcert-home.pem'

sms = ServiceManagementService(subscription_id,
                               certificate_path,
                               'management.core.chinacloudapi.cn')


operations = sms.list_subscription_operations('2015-09-01T16:30:00Z','2015-09-09T16:30:00Z',operation_result_filter = 'Failed')


for i in range(0,len(operations.subscription_operations)):

    print('NO:' + str(i) )
    print('operation_id: ' + operations.subscription_operations[i].operation_id)
    print('operation_name: ' + operations.subscription_operations[i].operation_name)
    print('operation_started_time: ' + operations.subscription_operations[i].operation_started_time)
    print('operation_status: ' + operations.subscription_operations[i].operation_status.status)
    print('==========================================')