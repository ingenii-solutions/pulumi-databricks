# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MwsPrivateAccessSettingsArgs', 'MwsPrivateAccessSettings']

@pulumi.input_type
class MwsPrivateAccessSettingsArgs:
    def __init__(__self__, *,
                 private_access_settings_name: pulumi.Input[str],
                 region: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 allowed_vpc_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_access_level: Optional[pulumi.Input[str]] = None,
                 private_access_settings_id: Optional[pulumi.Input[str]] = None,
                 public_access_enabled: Optional[pulumi.Input[bool]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MwsPrivateAccessSettings resource.
        """
        pulumi.set(__self__, "private_access_settings_name", private_access_settings_name)
        pulumi.set(__self__, "region", region)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if allowed_vpc_endpoint_ids is not None:
            pulumi.set(__self__, "allowed_vpc_endpoint_ids", allowed_vpc_endpoint_ids)
        if private_access_level is not None:
            pulumi.set(__self__, "private_access_level", private_access_level)
        if private_access_settings_id is not None:
            pulumi.set(__self__, "private_access_settings_id", private_access_settings_id)
        if public_access_enabled is not None:
            pulumi.set(__self__, "public_access_enabled", public_access_enabled)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="privateAccessSettingsName")
    def private_access_settings_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "private_access_settings_name")

    @private_access_settings_name.setter
    def private_access_settings_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_access_settings_name", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="allowedVpcEndpointIds")
    def allowed_vpc_endpoint_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "allowed_vpc_endpoint_ids")

    @allowed_vpc_endpoint_ids.setter
    def allowed_vpc_endpoint_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_vpc_endpoint_ids", value)

    @property
    @pulumi.getter(name="privateAccessLevel")
    def private_access_level(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_access_level")

    @private_access_level.setter
    def private_access_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_access_level", value)

    @property
    @pulumi.getter(name="privateAccessSettingsId")
    def private_access_settings_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_access_settings_id")

    @private_access_settings_id.setter
    def private_access_settings_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_access_settings_id", value)

    @property
    @pulumi.getter(name="publicAccessEnabled")
    def public_access_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "public_access_enabled")

    @public_access_enabled.setter
    def public_access_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_access_enabled", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _MwsPrivateAccessSettingsState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 allowed_vpc_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_access_level: Optional[pulumi.Input[str]] = None,
                 private_access_settings_id: Optional[pulumi.Input[str]] = None,
                 private_access_settings_name: Optional[pulumi.Input[str]] = None,
                 public_access_enabled: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MwsPrivateAccessSettings resources.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if allowed_vpc_endpoint_ids is not None:
            pulumi.set(__self__, "allowed_vpc_endpoint_ids", allowed_vpc_endpoint_ids)
        if private_access_level is not None:
            pulumi.set(__self__, "private_access_level", private_access_level)
        if private_access_settings_id is not None:
            pulumi.set(__self__, "private_access_settings_id", private_access_settings_id)
        if private_access_settings_name is not None:
            pulumi.set(__self__, "private_access_settings_name", private_access_settings_name)
        if public_access_enabled is not None:
            pulumi.set(__self__, "public_access_enabled", public_access_enabled)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="allowedVpcEndpointIds")
    def allowed_vpc_endpoint_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "allowed_vpc_endpoint_ids")

    @allowed_vpc_endpoint_ids.setter
    def allowed_vpc_endpoint_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_vpc_endpoint_ids", value)

    @property
    @pulumi.getter(name="privateAccessLevel")
    def private_access_level(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_access_level")

    @private_access_level.setter
    def private_access_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_access_level", value)

    @property
    @pulumi.getter(name="privateAccessSettingsId")
    def private_access_settings_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_access_settings_id")

    @private_access_settings_id.setter
    def private_access_settings_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_access_settings_id", value)

    @property
    @pulumi.getter(name="privateAccessSettingsName")
    def private_access_settings_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_access_settings_name")

    @private_access_settings_name.setter
    def private_access_settings_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_access_settings_name", value)

    @property
    @pulumi.getter(name="publicAccessEnabled")
    def public_access_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "public_access_enabled")

    @public_access_enabled.setter
    def public_access_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_access_enabled", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class MwsPrivateAccessSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 allowed_vpc_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_access_level: Optional[pulumi.Input[str]] = None,
                 private_access_settings_id: Optional[pulumi.Input[str]] = None,
                 private_access_settings_name: Optional[pulumi.Input[str]] = None,
                 public_access_enabled: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a MwsPrivateAccessSettings resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MwsPrivateAccessSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a MwsPrivateAccessSettings resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MwsPrivateAccessSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MwsPrivateAccessSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 allowed_vpc_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_access_level: Optional[pulumi.Input[str]] = None,
                 private_access_settings_id: Optional[pulumi.Input[str]] = None,
                 private_access_settings_name: Optional[pulumi.Input[str]] = None,
                 public_access_enabled: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MwsPrivateAccessSettingsArgs.__new__(MwsPrivateAccessSettingsArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["allowed_vpc_endpoint_ids"] = allowed_vpc_endpoint_ids
            __props__.__dict__["private_access_level"] = private_access_level
            __props__.__dict__["private_access_settings_id"] = private_access_settings_id
            if private_access_settings_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_access_settings_name'")
            __props__.__dict__["private_access_settings_name"] = private_access_settings_name
            __props__.__dict__["public_access_enabled"] = public_access_enabled
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["status"] = status
        super(MwsPrivateAccessSettings, __self__).__init__(
            'databricks:databricks/mwsPrivateAccessSettings:MwsPrivateAccessSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            allowed_vpc_endpoint_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            private_access_level: Optional[pulumi.Input[str]] = None,
            private_access_settings_id: Optional[pulumi.Input[str]] = None,
            private_access_settings_name: Optional[pulumi.Input[str]] = None,
            public_access_enabled: Optional[pulumi.Input[bool]] = None,
            region: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'MwsPrivateAccessSettings':
        """
        Get an existing MwsPrivateAccessSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MwsPrivateAccessSettingsState.__new__(_MwsPrivateAccessSettingsState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["allowed_vpc_endpoint_ids"] = allowed_vpc_endpoint_ids
        __props__.__dict__["private_access_level"] = private_access_level
        __props__.__dict__["private_access_settings_id"] = private_access_settings_id
        __props__.__dict__["private_access_settings_name"] = private_access_settings_name
        __props__.__dict__["public_access_enabled"] = public_access_enabled
        __props__.__dict__["region"] = region
        __props__.__dict__["status"] = status
        return MwsPrivateAccessSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="allowedVpcEndpointIds")
    def allowed_vpc_endpoint_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "allowed_vpc_endpoint_ids")

    @property
    @pulumi.getter(name="privateAccessLevel")
    def private_access_level(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "private_access_level")

    @property
    @pulumi.getter(name="privateAccessSettingsId")
    def private_access_settings_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "private_access_settings_id")

    @property
    @pulumi.getter(name="privateAccessSettingsName")
    def private_access_settings_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "private_access_settings_name")

    @property
    @pulumi.getter(name="publicAccessEnabled")
    def public_access_enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "public_access_enabled")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "status")

