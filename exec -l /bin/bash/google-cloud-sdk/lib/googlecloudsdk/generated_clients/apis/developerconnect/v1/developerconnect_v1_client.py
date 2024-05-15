"""Generated client library for developerconnect version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.developerconnect.v1 import developerconnect_v1_messages as messages


class DeveloperconnectV1(base_api.BaseApiClient):
  """Generated client library for service developerconnect version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://developerconnect.googleapis.com/'
  MTLS_BASE_URL = 'https://developerconnect.mtls.googleapis.com/'

  _PACKAGE = 'developerconnect'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'DeveloperconnectV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new developerconnect handle."""
    url = url or self.BASE_URL
    super(DeveloperconnectV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_connections_gitRepositoryLinks = self.ProjectsLocationsConnectionsGitRepositoryLinksService(self)
    self.projects_locations_connections = self.ProjectsLocationsConnectionsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsConnectionsGitRepositoryLinksService(base_api.BaseApiService):
    """Service class for the projects_locations_connections_gitRepositoryLinks resource."""

    _NAME = 'projects_locations_connections_gitRepositoryLinks'

    def __init__(self, client):
      super(DeveloperconnectV1.ProjectsLocationsConnectionsGitRepositoryLinksService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a GitRepositoryLink. Upon linking a Git Repository, Developer Connect will configure the Git Repository to send webhook events to Developer Connect. Connections that use Firebase GitHub Application will have events forwarded to the Firebase service. All other Connections will have events forwarded to Cloud Build.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}/gitRepositoryLinks',
        http_method='POST',
        method_id='developerconnect.projects.locations.connections.gitRepositoryLinks.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['gitRepositoryLinkId', 'requestId', 'validateOnly'],
        relative_path='v1/{+parent}/gitRepositoryLinks',
        request_field='gitRepositoryLink',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single GitRepositoryLink.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}/gitRepositoryLinks/{gitRepositoryLinksId}',
        http_method='DELETE',
        method_id='developerconnect.projects.locations.connections.gitRepositoryLinks.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['etag', 'requestId', 'validateOnly'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def FetchGitRefs(self, request, global_params=None):
      r"""Fetch the list of branches or tags for a given repository.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksFetchGitRefsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (FetchGitRefsResponse) The response message.
      """
      config = self.GetMethodConfig('FetchGitRefs')
      return self._RunMethod(
          config, request, global_params=global_params)

    FetchGitRefs.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}/gitRepositoryLinks/{gitRepositoryLinksId}:fetchGitRefs',
        http_method='GET',
        method_id='developerconnect.projects.locations.connections.gitRepositoryLinks.fetchGitRefs',
        ordered_params=['gitRepositoryLink'],
        path_params=['gitRepositoryLink'],
        query_params=['pageSize', 'pageToken', 'refType'],
        relative_path='v1/{+gitRepositoryLink}:fetchGitRefs',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksFetchGitRefsRequest',
        response_type_name='FetchGitRefsResponse',
        supports_download=False,
    )

    def FetchReadToken(self, request, global_params=None):
      r"""Fetches read token of a given gitRepositoryLink.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksFetchReadTokenRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (FetchReadTokenResponse) The response message.
      """
      config = self.GetMethodConfig('FetchReadToken')
      return self._RunMethod(
          config, request, global_params=global_params)

    FetchReadToken.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}/gitRepositoryLinks/{gitRepositoryLinksId}:fetchReadToken',
        http_method='POST',
        method_id='developerconnect.projects.locations.connections.gitRepositoryLinks.fetchReadToken',
        ordered_params=['gitRepositoryLink'],
        path_params=['gitRepositoryLink'],
        query_params=[],
        relative_path='v1/{+gitRepositoryLink}:fetchReadToken',
        request_field='fetchReadTokenRequest',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksFetchReadTokenRequest',
        response_type_name='FetchReadTokenResponse',
        supports_download=False,
    )

    def FetchReadWriteToken(self, request, global_params=None):
      r"""Fetches read/write token of a given gitRepositoryLink.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksFetchReadWriteTokenRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (FetchReadWriteTokenResponse) The response message.
      """
      config = self.GetMethodConfig('FetchReadWriteToken')
      return self._RunMethod(
          config, request, global_params=global_params)

    FetchReadWriteToken.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}/gitRepositoryLinks/{gitRepositoryLinksId}:fetchReadWriteToken',
        http_method='POST',
        method_id='developerconnect.projects.locations.connections.gitRepositoryLinks.fetchReadWriteToken',
        ordered_params=['gitRepositoryLink'],
        path_params=['gitRepositoryLink'],
        query_params=[],
        relative_path='v1/{+gitRepositoryLink}:fetchReadWriteToken',
        request_field='fetchReadWriteTokenRequest',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksFetchReadWriteTokenRequest',
        response_type_name='FetchReadWriteTokenResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single GitRepositoryLink.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GitRepositoryLink) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}/gitRepositoryLinks/{gitRepositoryLinksId}',
        http_method='GET',
        method_id='developerconnect.projects.locations.connections.gitRepositoryLinks.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksGetRequest',
        response_type_name='GitRepositoryLink',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists GitRepositoryLinks in a given project, location, and connection.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListGitRepositoryLinksResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}/gitRepositoryLinks',
        http_method='GET',
        method_id='developerconnect.projects.locations.connections.gitRepositoryLinks.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/gitRepositoryLinks',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsGitRepositoryLinksListRequest',
        response_type_name='ListGitRepositoryLinksResponse',
        supports_download=False,
    )

  class ProjectsLocationsConnectionsService(base_api.BaseApiService):
    """Service class for the projects_locations_connections resource."""

    _NAME = 'projects_locations_connections'

    def __init__(self, client):
      super(DeveloperconnectV1.ProjectsLocationsConnectionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Connection in a given project and location.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections',
        http_method='POST',
        method_id='developerconnect.projects.locations.connections.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['connectionId', 'requestId', 'validateOnly'],
        relative_path='v1/{+parent}/connections',
        request_field='connection',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Connection.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}',
        http_method='DELETE',
        method_id='developerconnect.projects.locations.connections.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['etag', 'requestId', 'validateOnly'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def FetchGitHubInstallations(self, request, global_params=None):
      r"""FetchGitHubInstallations returns the list of GitHub Installations that are available to be added to a Connection. For github.com, only installations accessible to the authorizer token are returned. For GitHub Enterprise, all installations are returned.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsFetchGitHubInstallationsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (FetchGitHubInstallationsResponse) The response message.
      """
      config = self.GetMethodConfig('FetchGitHubInstallations')
      return self._RunMethod(
          config, request, global_params=global_params)

    FetchGitHubInstallations.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}:fetchGitHubInstallations',
        http_method='GET',
        method_id='developerconnect.projects.locations.connections.fetchGitHubInstallations',
        ordered_params=['connection'],
        path_params=['connection'],
        query_params=[],
        relative_path='v1/{+connection}:fetchGitHubInstallations',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsFetchGitHubInstallationsRequest',
        response_type_name='FetchGitHubInstallationsResponse',
        supports_download=False,
    )

    def FetchLinkableGitRepositories(self, request, global_params=None):
      r"""FetchLinkableGitRepositories returns a list of git repositories from an SCM that are available to be added to a Connection.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsFetchLinkableGitRepositoriesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (FetchLinkableGitRepositoriesResponse) The response message.
      """
      config = self.GetMethodConfig('FetchLinkableGitRepositories')
      return self._RunMethod(
          config, request, global_params=global_params)

    FetchLinkableGitRepositories.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}:fetchLinkableGitRepositories',
        http_method='GET',
        method_id='developerconnect.projects.locations.connections.fetchLinkableGitRepositories',
        ordered_params=['connection'],
        path_params=['connection'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+connection}:fetchLinkableGitRepositories',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsFetchLinkableGitRepositoriesRequest',
        response_type_name='FetchLinkableGitRepositoriesResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Connection.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Connection) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}',
        http_method='GET',
        method_id='developerconnect.projects.locations.connections.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsGetRequest',
        response_type_name='Connection',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Connections in a given project and location.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListConnectionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections',
        http_method='GET',
        method_id='developerconnect.projects.locations.connections.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/connections',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsListRequest',
        response_type_name='ListConnectionsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single Connection.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections/{connectionsId}',
        http_method='PATCH',
        method_id='developerconnect.projects.locations.connections.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['allowMissing', 'requestId', 'updateMask', 'validateOnly'],
        relative_path='v1/{+name}',
        request_field='connection',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def ProcessGitHubEnterpriseWebhook(self, request, global_params=None):
      r"""ProcessGitHubEnterpriseWebhook is called by the external GitHub Enterprise instances for notifying events.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsProcessGitHubEnterpriseWebhookRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('ProcessGitHubEnterpriseWebhook')
      return self._RunMethod(
          config, request, global_params=global_params)

    ProcessGitHubEnterpriseWebhook.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections:processGitHubEnterpriseWebhook',
        http_method='POST',
        method_id='developerconnect.projects.locations.connections.processGitHubEnterpriseWebhook',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/connections:processGitHubEnterpriseWebhook',
        request_field='processGitHubEnterpriseWebhookRequest',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsProcessGitHubEnterpriseWebhookRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def ProcessGitLabEnterpriseWebhook(self, request, global_params=None):
      r"""ProcessGitLabEnterpriseWebhook is called by the external GitLab Enterprise instances for notifying events.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsProcessGitLabEnterpriseWebhookRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('ProcessGitLabEnterpriseWebhook')
      return self._RunMethod(
          config, request, global_params=global_params)

    ProcessGitLabEnterpriseWebhook.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections:processGitLabEnterpriseWebhook',
        http_method='POST',
        method_id='developerconnect.projects.locations.connections.processGitLabEnterpriseWebhook',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/connections:processGitLabEnterpriseWebhook',
        request_field='processGitLabEnterpriseWebhookRequest',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsProcessGitLabEnterpriseWebhookRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def ProcessGitLabWebhook(self, request, global_params=None):
      r"""ProcessGitLabWebhook is called by the GitLab.com for notifying events.

      Args:
        request: (DeveloperconnectProjectsLocationsConnectionsProcessGitLabWebhookRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('ProcessGitLabWebhook')
      return self._RunMethod(
          config, request, global_params=global_params)

    ProcessGitLabWebhook.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connections:processGitLabWebhook',
        http_method='POST',
        method_id='developerconnect.projects.locations.connections.processGitLabWebhook',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/connections:processGitLabWebhook',
        request_field='processGitLabWebhookRequest',
        request_type_name='DeveloperconnectProjectsLocationsConnectionsProcessGitLabWebhookRequest',
        response_type_name='Empty',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(DeveloperconnectV1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (DeveloperconnectProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='developerconnect.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='DeveloperconnectProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (DeveloperconnectProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='developerconnect.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (DeveloperconnectProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='developerconnect.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (DeveloperconnectProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='developerconnect.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/operations',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(DeveloperconnectV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (DeveloperconnectProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='developerconnect.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (DeveloperconnectProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='developerconnect.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/locations',
        request_field='',
        request_type_name='DeveloperconnectProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(DeveloperconnectV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
