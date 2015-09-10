import sys
from azure import *
from azure.servicemanagement import *

if __name__ == '__main__':

    subscription_id = raw_input("Please input Subscription ID:")
    certificate_path = raw_input("Please input your certification location:")
    start_time = raw_input("Please input the start time [eg:2015-09-01T16:30:00Z]:")
    end_time = raw_input("Please input the start time [eg:2015-09-01T16:30:00Z]:")
    filter = raw_input("Please input the operation status[Succeeded, Failed, or InProgress enter = all]:")


#subscription_id = '4c1f7e7c-e47c-4688-8de0-19b1f8b58636'
#certificate_path = 'C:\Azure_Cert\zymcert-home.pem'

    sms = ServiceManagementService(subscription_id,
                                   certificate_path,
                                   'management.core.chinacloudapi.cn')



    try:
        operations = sms.list_subscription_operations(start_time,end_time,operation_result_filter = filter)
    except Exception as e :
        print "error：" + str(e)


    for i in range(0,len(operations.subscription_operations)):

        print('NO:' + str(i) )
        print('operation_id: ' + operations.subscription_operations[i].operation_id)
        print('operation_name: ' + operations.subscription_operations[i].operation_name)
        print('operation_started_time: ' + operations.subscription_operations[i].operation_started_time)
        print('operation_status: ' + operations.subscription_operations[i].operation_status.status)
        print('==========================================')