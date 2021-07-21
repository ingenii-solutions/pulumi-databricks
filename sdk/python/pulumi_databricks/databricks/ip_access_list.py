# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IPAccessListArgs', 'IPAccessList']

@pulumi.input_type
class IPAccessListArgs:
    def __init__(__self__, *,
                 ip_addresses: pulumi.Input[Sequence[pulumi.Input[str]]],
                 label: pulumi.Input[str],
                 list_type: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a IPAccessList resource.
        """
        pulumi.set(__self__, "ip_addresses", ip_addresses)
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "list_type", list_type)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "ip_addresses")

    @ip_addresses.setter
    def ip_addresses(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "ip_addresses", value)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Input[str]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: pulumi.Input[str]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="listType")
    def list_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "list_type")

    @list_type.setter
    def list_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "list_type", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class _IPAccessListState:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 list_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IPAccessList resources.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if ip_addresses is not None:
            pulumi.set(__self__, "ip_addresses", ip_addresses)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if list_type is not None:
            pulumi.set(__self__, "list_type", list_type)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "ip_addresses")

    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_addresses", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="listType")
    def list_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "list_type")

    @list_type.setter
    def list_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "list_type", value)


class IPAccessList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 list_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a IPAccessList resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IPAccessListArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a IPAccessList resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param IPAccessListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IPAccessListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 list_type: Optional[pulumi.Input[str]] = None,
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
            __props__ = IPAccessListArgs.__new__(IPAccessListArgs)

            __props__.__dict__["enabled"] = enabled
            if ip_addresses is None and not opts.urn:
                raise TypeError("Missing required property 'ip_addresses'")
            __props__.__dict__["ip_addresses"] = ip_addresses
            if label is None and not opts.urn:
                raise TypeError("Missing required property 'label'")
            __props__.__dict__["label"] = label
            if list_type is None and not opts.urn:
                raise TypeError("Missing required property 'list_type'")
            __props__.__dict__["list_type"] = list_type
        super(IPAccessList, __self__).__init__(
            'databricks:databricks/iPAccessList:IPAccessList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            label: Optional[pulumi.Input[str]] = None,
            list_type: Optional[pulumi.Input[str]] = None) -> 'IPAccessList':
        """
        Get an existing IPAccessList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IPAccessListState.__new__(_IPAccessListState)

        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["ip_addresses"] = ip_addresses
        __props__.__dict__["label"] = label
        __props__.__dict__["list_type"] = list_type
        return IPAccessList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="listType")
    def list_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "list_type")
