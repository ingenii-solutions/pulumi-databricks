# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SchemaArgs', 'Schema']

@pulumi.input_type
class SchemaArgs:
    def __init__(__self__, *,
                 catalog_name: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Schema resource.
        """
        pulumi.set(__self__, "catalog_name", catalog_name)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if metastore_id is not None:
            pulumi.set(__self__, "metastore_id", metastore_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "catalog_name")

    @catalog_name.setter
    def catalog_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "catalog_name", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metastore_id")

    @metastore_id.setter
    def metastore_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metastore_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "properties", value)


@pulumi.input_type
class _SchemaState:
    def __init__(__self__, *,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering Schema resources.
        """
        if catalog_name is not None:
            pulumi.set(__self__, "catalog_name", catalog_name)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if metastore_id is not None:
            pulumi.set(__self__, "metastore_id", metastore_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "catalog_name")

    @catalog_name.setter
    def catalog_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_name", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metastore_id")

    @metastore_id.setter
    def metastore_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metastore_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "properties", value)


class Schema(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        Create a Schema resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SchemaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Schema resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SchemaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SchemaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
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
            __props__ = SchemaArgs.__new__(SchemaArgs)

            if catalog_name is None and not opts.urn:
                raise TypeError("Missing required property 'catalog_name'")
            __props__.__dict__["catalog_name"] = catalog_name
            __props__.__dict__["comment"] = comment
            __props__.__dict__["metastore_id"] = metastore_id
            __props__.__dict__["name"] = name
            __props__.__dict__["owner"] = owner
            __props__.__dict__["properties"] = properties
        super(Schema, __self__).__init__(
            'databricks:databricks/schema:Schema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            catalog_name: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            metastore_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            properties: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'Schema':
        """
        Get an existing Schema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SchemaState.__new__(_SchemaState)

        __props__.__dict__["catalog_name"] = catalog_name
        __props__.__dict__["comment"] = comment
        __props__.__dict__["metastore_id"] = metastore_id
        __props__.__dict__["name"] = name
        __props__.__dict__["owner"] = owner
        __props__.__dict__["properties"] = properties
        return Schema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "catalog_name")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "metastore_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "properties")

