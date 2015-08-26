from azure import *
from azure.servicemanagement import *


subscription_id = '4c1f7e7c-e47c-4688-8de0-19b1f8b58636'
certificate_path = 'C:\cer\zymcert.pem'

sms = ServiceManagementService(subscription_id,
                               certificate_path,
                               'management.core.chinacloudapi.cn')


name = 'zymDS11'

#Set the location
sms.create_hosted_service(service_name=name,
    label=name,
    location='China East')

# Name of an os image as returned by list_os_images
image_name = '55bc2b193643443bb879a78bda516fc8__Windows-Server-2012-R2-20150726-zh.cn-127GB.vhd'

# Destination storage account container/blob where the VM disk
# will be created
media_link = 'https://zymnorth.blob.core.chinacloudapi.cn/vhds/test.vhd'

# Linux VM configuration, you can use WindowsConfigurationSet
# for a Windows VM instead
windows_config = WindowsConfigurationSet(name,admin_password='!QAZ1qaz',admin_username='zhang.yiming')

os_hd = OSVirtualHardDisk(image_name, media_link)

sms.create_virtual_machine_deployment(service_name=name,
    deployment_name=name,
    deployment_slot='production',
    label=name,
    role_name=name,
    system_config=windows_config,
    os_virtual_hard_disk=os_hd,
    role_size='Small')