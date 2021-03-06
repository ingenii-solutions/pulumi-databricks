# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DatabricksMountArgs', 'DatabricksMount']

@pulumi.input_type
class DatabricksMountArgs:
    def __init__(__self__, *,
                 abfs: Optional[pulumi.Input['DatabricksMountAbfsArgs']] = None,
                 adl: Optional[pulumi.Input['DatabricksMountAdlArgs']] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[str]] = None,
                 extra_configs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 gs: Optional[pulumi.Input['DatabricksMountGsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input['DatabricksMountS3Args']] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 wasb: Optional[pulumi.Input['DatabricksMountWasbArgs']] = None):
        """
        The set of arguments for constructing a DatabricksMount resource.
        """
        if abfs is not None:
            pulumi.set(__self__, "abfs", abfs)
        if adl is not None:
            pulumi.set(__self__, "adl", adl)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if encryption_type is not None:
            pulumi.set(__self__, "encryption_type", encryption_type)
        if extra_configs is not None:
            pulumi.set(__self__, "extra_configs", extra_configs)
        if gs is not None:
            pulumi.set(__self__, "gs", gs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if s3 is not None:
            pulumi.set(__self__, "s3", s3)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)
        if wasb is not None:
            pulumi.set(__self__, "wasb", wasb)

    @property
    @pulumi.getter
    def abfs(self) -> Optional[pulumi.Input['DatabricksMountAbfsArgs']]:
        return pulumi.get(self, "abfs")

    @abfs.setter
    def abfs(self, value: Optional[pulumi.Input['DatabricksMountAbfsArgs']]):
        pulumi.set(self, "abfs", value)

    @property
    @pulumi.getter
    def adl(self) -> Optional[pulumi.Input['DatabricksMountAdlArgs']]:
        return pulumi.get(self, "adl")

    @adl.setter
    def adl(self, value: Optional[pulumi.Input['DatabricksMountAdlArgs']]):
        pulumi.set(self, "adl", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "encryption_type")

    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_type", value)

    @property
    @pulumi.getter(name="extraConfigs")
    def extra_configs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "extra_configs")

    @extra_configs.setter
    def extra_configs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "extra_configs", value)

    @property
    @pulumi.getter
    def gs(self) -> Optional[pulumi.Input['DatabricksMountGsArgs']]:
        return pulumi.get(self, "gs")

    @gs.setter
    def gs(self, value: Optional[pulumi.Input['DatabricksMountGsArgs']]):
        pulumi.set(self, "gs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input['DatabricksMountS3Args']]:
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: Optional[pulumi.Input['DatabricksMountS3Args']]):
        pulumi.set(self, "s3", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter
    def wasb(self) -> Optional[pulumi.Input['DatabricksMountWasbArgs']]:
        return pulumi.get(self, "wasb")

    @wasb.setter
    def wasb(self, value: Optional[pulumi.Input['DatabricksMountWasbArgs']]):
        pulumi.set(self, "wasb", value)


@pulumi.input_type
class _DatabricksMountState:
    def __init__(__self__, *,
                 abfs: Optional[pulumi.Input['DatabricksMountAbfsArgs']] = None,
                 adl: Optional[pulumi.Input['DatabricksMountAdlArgs']] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[str]] = None,
                 extra_configs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 gs: Optional[pulumi.Input['DatabricksMountGsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input['DatabricksMountS3Args']] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 wasb: Optional[pulumi.Input['DatabricksMountWasbArgs']] = None):
        """
        Input properties used for looking up and filtering DatabricksMount resources.
        """
        if abfs is not None:
            pulumi.set(__self__, "abfs", abfs)
        if adl is not None:
            pulumi.set(__self__, "adl", adl)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if encryption_type is not None:
            pulumi.set(__self__, "encryption_type", encryption_type)
        if extra_configs is not None:
            pulumi.set(__self__, "extra_configs", extra_configs)
        if gs is not None:
            pulumi.set(__self__, "gs", gs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if s3 is not None:
            pulumi.set(__self__, "s3", s3)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)
        if wasb is not None:
            pulumi.set(__self__, "wasb", wasb)

    @property
    @pulumi.getter
    def abfs(self) -> Optional[pulumi.Input['DatabricksMountAbfsArgs']]:
        return pulumi.get(self, "abfs")

    @abfs.setter
    def abfs(self, value: Optional[pulumi.Input['DatabricksMountAbfsArgs']]):
        pulumi.set(self, "abfs", value)

    @property
    @pulumi.getter
    def adl(self) -> Optional[pulumi.Input['DatabricksMountAdlArgs']]:
        return pulumi.get(self, "adl")

    @adl.setter
    def adl(self, value: Optional[pulumi.Input['DatabricksMountAdlArgs']]):
        pulumi.set(self, "adl", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "encryption_type")

    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_type", value)

    @property
    @pulumi.getter(name="extraConfigs")
    def extra_configs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "extra_configs")

    @extra_configs.setter
    def extra_configs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "extra_configs", value)

    @property
    @pulumi.getter
    def gs(self) -> Optional[pulumi.Input['DatabricksMountGsArgs']]:
        return pulumi.get(self, "gs")

    @gs.setter
    def gs(self, value: Optional[pulumi.Input['DatabricksMountGsArgs']]):
        pulumi.set(self, "gs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input['DatabricksMountS3Args']]:
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: Optional[pulumi.Input['DatabricksMountS3Args']]):
        pulumi.set(self, "s3", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter
    def wasb(self) -> Optional[pulumi.Input['DatabricksMountWasbArgs']]:
        return pulumi.get(self, "wasb")

    @wasb.setter
    def wasb(self, value: Optional[pulumi.Input['DatabricksMountWasbArgs']]):
        pulumi.set(self, "wasb", value)


class DatabricksMount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 abfs: Optional[pulumi.Input[pulumi.InputType['DatabricksMountAbfsArgs']]] = None,
                 adl: Optional[pulumi.Input[pulumi.InputType['DatabricksMountAdlArgs']]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[str]] = None,
                 extra_configs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 gs: Optional[pulumi.Input[pulumi.InputType['DatabricksMountGsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input[pulumi.InputType['DatabricksMountS3Args']]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 wasb: Optional[pulumi.Input[pulumi.InputType['DatabricksMountWasbArgs']]] = None,
                 __props__=None):
        """
        Create a DatabricksMount resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DatabricksMountArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DatabricksMount resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DatabricksMountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabricksMountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 abfs: Optional[pulumi.Input[pulumi.InputType['DatabricksMountAbfsArgs']]] = None,
                 adl: Optional[pulumi.Input[pulumi.InputType['DatabricksMountAdlArgs']]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[str]] = None,
                 extra_configs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 gs: Optional[pulumi.Input[pulumi.InputType['DatabricksMountGsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input[pulumi.InputType['DatabricksMountS3Args']]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 wasb: Optional[pulumi.Input[pulumi.InputType['DatabricksMountWasbArgs']]] = None,
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
            __props__ = DatabricksMountArgs.__new__(DatabricksMountArgs)

            __props__.__dict__["abfs"] = abfs
            __props__.__dict__["adl"] = adl
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["encryption_type"] = encryption_type
            __props__.__dict__["extra_configs"] = extra_configs
            __props__.__dict__["gs"] = gs
            __props__.__dict__["name"] = name
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["s3"] = s3
            __props__.__dict__["uri"] = uri
            __props__.__dict__["wasb"] = wasb
            __props__.__dict__["source"] = None
        super(DatabricksMount, __self__).__init__(
            'databricks:databricks/databricksMount:DatabricksMount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            abfs: Optional[pulumi.Input[pulumi.InputType['DatabricksMountAbfsArgs']]] = None,
            adl: Optional[pulumi.Input[pulumi.InputType['DatabricksMountAdlArgs']]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            encryption_type: Optional[pulumi.Input[str]] = None,
            extra_configs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            gs: Optional[pulumi.Input[pulumi.InputType['DatabricksMountGsArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_id: Optional[pulumi.Input[str]] = None,
            s3: Optional[pulumi.Input[pulumi.InputType['DatabricksMountS3Args']]] = None,
            source: Optional[pulumi.Input[str]] = None,
            uri: Optional[pulumi.Input[str]] = None,
            wasb: Optional[pulumi.Input[pulumi.InputType['DatabricksMountWasbArgs']]] = None) -> 'DatabricksMount':
        """
        Get an existing DatabricksMount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatabricksMountState.__new__(_DatabricksMountState)

        __props__.__dict__["abfs"] = abfs
        __props__.__dict__["adl"] = adl
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["encryption_type"] = encryption_type
        __props__.__dict__["extra_configs"] = extra_configs
        __props__.__dict__["gs"] = gs
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_id"] = resource_id
        __props__.__dict__["s3"] = s3
        __props__.__dict__["source"] = source
        __props__.__dict__["uri"] = uri
        __props__.__dict__["wasb"] = wasb
        return DatabricksMount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def abfs(self) -> pulumi.Output[Optional['outputs.DatabricksMountAbfs']]:
        return pulumi.get(self, "abfs")

    @property
    @pulumi.getter
    def adl(self) -> pulumi.Output[Optional['outputs.DatabricksMountAdl']]:
        return pulumi.get(self, "adl")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "encryption_type")

    @property
    @pulumi.getter(name="extraConfigs")
    def extra_configs(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "extra_configs")

    @property
    @pulumi.getter
    def gs(self) -> pulumi.Output[Optional['outputs.DatabricksMountGs']]:
        return pulumi.get(self, "gs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def s3(self) -> pulumi.Output[Optional['outputs.DatabricksMountS3']]:
        return pulumi.get(self, "s3")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter
    def wasb(self) -> pulumi.Output[Optional['outputs.DatabricksMountWasb']]:
        return pulumi.get(self, "wasb")

