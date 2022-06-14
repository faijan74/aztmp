from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.trafficmanager import TrafficManagerManagementClient
from azure.mgmt.trafficmanager.models import EndpointStatus, Endpoint
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import SubscriptionClient

credential = DefaultAzureCredential()
subscription_client = SubscriptionClient(credential)


client_id = "9e618b20-fb12-4bd5-ac9a-8f31b48c76af"
secret = "4470e53c-deb5-45bb-a7e8-a89828c79e91"
tenant = "5473e86b-917b-4f8b-b651-58c6856515da"
subscription_ID = "985d107b-f410-4595-8500-e1991ed9fe4a"

tm_client = TrafficManagerManagementClient(credential, subscription_ID)
param = Endpoint(
    target_resource_id='/subscriptions/985d107b-f410-4595-8500-e1991ed9fe4a/resourceGroups/test/providers/Microsoft.Web/sites/azure-cli-2022-06-12-14-35-20',
    endpoint_status=EndpointStatus.enabled,
    priority=1
)
result = tm_client.endpoints.create_or_update(
    resource_group_name='test',
    profile_name='test05',
    endpoint_type='AzureEndpoints',
    endpoint_name='mypoint',
    parameters=param)

print(result.id)


