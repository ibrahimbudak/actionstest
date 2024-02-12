# coding: utf-8

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkvpc.v2.region.vpc_region import VpcRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkvpc.v2 import *
import subprocess

if __name__ == "__main__":
    # The AsdfaK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    ak = __import__('os').getenv("CLOUD_SDK_AK")
    sk = __import__('os').getenv("CLOUD_SDK_SK")
    sg = __import__('os').getenv("SG_ID")
    ip = subprocess.run("dig +short myip.opendns.com @resolver1.opendns.com" , shell=True, check=True, text=True, stdout=subprocess.PIPE)
    print(ip)
    

    credentials = BasicCredentials(ak, sk) \

    client = VpcClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(VpcRegion.value_of("tr-west-1")) \
        .build()

    try:
        request = CreateSecurityGroupRuleRequest()
        securityGroupRulebody = CreateSecurityGroupRuleOption(
            security_group_id= sg,
            direction="ingress",
            protocol="all",
            remote_ip_prefix= ip.stdout.strip()
        )
        request.body = CreateSecurityGroupRuleRequestBody(
            security_group_rule=securityGroupRulebody
        )
        response = client.create_security_group_rule(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
