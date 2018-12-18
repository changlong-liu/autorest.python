# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models
from .date_model_operations import DateModelOperations as _DateModelOperations


class DateModelOperations(_DateModelOperations):
    """DateModelOperations operations."""

    async def get_null_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get null date value.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_null_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_null_async.metadata = {'url': '/date/null'}

    async def get_invalid_date_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get invalid date value.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_invalid_date_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_invalid_date_async.metadata = {'url': '/date/invaliddate'}

    async def get_overflow_date_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get overflow date value.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_overflow_date_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_overflow_date_async.metadata = {'url': '/date/overflowdate'}

    async def get_underflow_date_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get underflow date value.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_underflow_date_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_underflow_date_async.metadata = {'url': '/date/underflowdate'}

    async def put_max_date_async(
            self, date_body, *, custom_headers=None, raw=False, **operation_config):
        """Put max date value 9999-12-31.

        :param date_body:
        :type date_body: date
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.put_max_date_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(date_body, 'date')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_max_date_async.metadata = {'url': '/date/max'}

    async def get_max_date_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get max date value 9999-12-31.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_max_date_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_max_date_async.metadata = {'url': '/date/max'}

    async def put_min_date_async(
            self, date_body, *, custom_headers=None, raw=False, **operation_config):
        """Put min date value 0000-01-01.

        :param date_body:
        :type date_body: date
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.put_min_date_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(date_body, 'date')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_min_date_async.metadata = {'url': '/date/min'}

    async def get_min_date_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get min date value 0000-01-01.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_min_date_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_min_date_async.metadata = {'url': '/date/min'}
