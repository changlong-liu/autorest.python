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

from azure.core.configuration import Configuration, ConnectionConfiguration
from azure.core.pipeline import policies

from .version import VERSION


class AutoRestParameterizedCustomHostTestClientConfiguration(Configuration):
    """Configuration for AutoRestParameterizedCustomHostTestClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: The subscription id with value 'test12'.
    :type subscription_id: str
    :param dns_suffix: A string value that is used as a global part of the
     parameterized host. Default value 'host'.
    :type dns_suffix: str
    """

    def __init__(self, subscription_id, dns_suffix, **kwargs):

        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if dns_suffix is None:
            raise ValueError("Parameter 'dns_suffix' must not be None.")

        super(AutoRestParameterizedCustomHostTestClientConfiguration, self).__init__(**kwargs)
        self._configure(**kwargs)

        self.user_agent_policy.add_user_agent('autorestparameterizedcustomhosttestclient/{}'.format(VERSION))
        self.generate_client_request_id = True
        self.accept_language = None

        self.subscription_id = subscription_id
        self.dns_suffix = dns_suffix

    def _configure(self, **kwargs):
        self.connection = ConnectionConfiguration(**kwargs)
        self.user_agent_policy = policies.UserAgentPolicy(**kwargs)
        self.headers_policy = policies.HeadersPolicy(**kwargs)
        self.proxy_policy = policies.ProxyPolicy(**kwargs)
        self.logging_policy = policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = policies.RedirectPolicy(**kwargs)
