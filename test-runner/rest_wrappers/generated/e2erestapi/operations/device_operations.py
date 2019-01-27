# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class DeviceOperations(object):
    """DeviceOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def connect(
            self, transport_type, connection_string, ca_certificate=None, custom_headers=None, raw=False, **operation_config):
        """Connect to the azure IoT Hub as a device.

        :param transport_type: Transport to use. Possible values include:
         'amqp', 'amqpws', 'mqtt', 'mqttws', 'http'
        :type transport_type: str
        :param connection_string: connection string
        :type connection_string: str
        :param ca_certificate:
        :type ca_certificate: ~e2erestapi.models.Certificate
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ConnectResponse or ClientRawResponse if raw=true
        :rtype: ~e2erestapi.models.ConnectResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.connect.metadata['url']
        path_format_arguments = {
            'transportType': self._serialize.url("transport_type", transport_type, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['connectionString'] = self._serialize.query("connection_string", connection_string, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if ca_certificate is not None:
            body_content = self._serialize.body(ca_certificate, 'Certificate')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ConnectResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    connect.metadata = {'url': '/device/connect/{transportType}'}

    def disconnect(
            self, connection_id, custom_headers=None, raw=False, **operation_config):
        """Disconnect the device.

        Disconnects from Azure IoTHub service.  More specifically, closes all
        connections and cleans up all resources for the active connection.

        :param connection_id: Id for the connection
        :type connection_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.disconnect.metadata['url']
        path_format_arguments = {
            'connectionId': self._serialize.url("connection_id", connection_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    disconnect.metadata = {'url': '/device/{connectionId}/disconnect'}

    def enable_methods(
            self, connection_id, custom_headers=None, raw=False, **operation_config):
        """Enable methods.

        :param connection_id: Id for the connection
        :type connection_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.enable_methods.metadata['url']
        path_format_arguments = {
            'connectionId': self._serialize.url("connection_id", connection_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    enable_methods.metadata = {'url': '/device/{connectionId}/enableMethods'}

    def roundtrip_method_call(
            self, connection_id, method_name, request_and_response, custom_headers=None, raw=False, **operation_config):
        """Wait for a method call, verify the request, and return the response.

        This is a workaround to deal with SDKs that only have method call
        operations that are sync.  This function responds to the method with
        the payload of this function, and then returns the method parameters.
        Real-world implemenatations would never do this, but this is the only
        same way to write our test code right now (because the method handlers
        for C, Java, and probably Python all return the method response instead
        of supporting an async method call).

        :param connection_id: Id for the connection
        :type connection_id: str
        :param method_name: name of the method to handle
        :type method_name: str
        :param request_and_response:
        :type request_and_response: ~e2erestapi.models.RoundtripMethodCallBody
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.roundtrip_method_call.metadata['url']
        path_format_arguments = {
            'connectionId': self._serialize.url("connection_id", connection_id, 'str'),
            'methodName': self._serialize.url("method_name", method_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(request_and_response, 'RoundtripMethodCallBody')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    roundtrip_method_call.metadata = {'url': '/device/{connectionId}/roundtripMethodCall/{methodName}'}