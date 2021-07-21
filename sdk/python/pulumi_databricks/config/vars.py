# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('databricks')


class _ExportableConfig(types.ModuleType):
    @property
    def azure_client_id(self) -> Optional[str]:
        return __config__.get('azureClientId')

    @property
    def azure_client_secret(self) -> Optional[str]:
        return __config__.get('azureClientSecret')

    @property
    def azure_environment(self) -> Optional[str]:
        return __config__.get('azureEnvironment')

    @property
    def azure_pat_token_duration_seconds(self) -> Optional[str]:
        """
        Currently secret scopes are not accessible via AAD tokens so we will need to create a PAT token
        """
        return __config__.get('azurePatTokenDurationSeconds')

    @property
    def azure_resource_group(self) -> Optional[str]:
        return __config__.get('azureResourceGroup')

    @property
    def azure_subscription_id(self) -> Optional[str]:
        return __config__.get('azureSubscriptionId')

    @property
    def azure_tenant_id(self) -> Optional[str]:
        return __config__.get('azureTenantId')

    @property
    def azure_use_pat_for_cli(self) -> Optional[str]:
        """
        Create ephemeral PAT tokens also for AZ CLI authenticated requests
        """
        return __config__.get('azureUsePatForCli')

    @property
    def azure_use_pat_for_spn(self) -> Optional[str]:
        """
        Create ephemeral PAT tokens instead of AAD tokens for SPN
        """
        return __config__.get('azureUsePatForSpn')

    @property
    def azure_workspace_name(self) -> Optional[str]:
        return __config__.get('azureWorkspaceName')

    @property
    def azure_workspace_resource_id(self) -> Optional[str]:
        return __config__.get('azureWorkspaceResourceId')

    @property
    def config_file(self) -> Optional[str]:
        """
        Location of the Databricks CLI credentials file, that is created by `databricks configure --token` command. By default,
        it is located in ~/.databrickscfg. Check https://docs.databricks.com/dev-tools/cli/index.html#set-up-authentication for
        docs. Config file credentials will only be used when host/token are not provided.
        """
        return __config__.get('configFile')

    @property
    def debug_headers(self) -> Optional[str]:
        """
        Debug HTTP headers of requests made by the provider. Default is false. Visible only when TF_LOG=DEBUG is set
        """
        return __config__.get('debugHeaders')

    @property
    def debug_truncate_bytes(self) -> Optional[str]:
        """
        Truncate JSON fields in JSON above this limit. Default is 96. Visible only when TF_LOG=DEBUG is set
        """
        return __config__.get('debugTruncateBytes')

    @property
    def host(self) -> Optional[str]:
        return __config__.get('host')

    @property
    def password(self) -> Optional[str]:
        return __config__.get('password')

    @property
    def profile(self) -> Optional[str]:
        """
        Connection profile specified within ~/.databrickscfg. Please check
        https://docs.databricks.com/dev-tools/cli/index.html#connection-profiles for documentation.
        """
        return __config__.get('profile')

    @property
    def rate_limit(self) -> Optional[str]:
        """
        Maximum number of requests per second made to Databricks REST API by Terraform.
        """
        return __config__.get('rateLimit')

    @property
    def skip_verify(self) -> Optional[str]:
        """
        Skip SSL certificate verification for HTTP calls. Use at your own risk.
        """
        return __config__.get('skipVerify')

    @property
    def token(self) -> Optional[str]:
        return __config__.get('token')

    @property
    def username(self) -> Optional[str]:
        return __config__.get('username')

