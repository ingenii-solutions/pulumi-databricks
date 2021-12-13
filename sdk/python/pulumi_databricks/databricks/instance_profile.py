# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['InstanceProfileArgs', 'InstanceProfile']

@pulumi.input_type
class InstanceProfileArgs:
    def __init__(__self__, *,
                 instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 is_meta_instance_profile: Optional[pulumi.Input[bool]] = None,
                 skip_validation: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a InstanceProfile resource.
        """
        if instance_profile_arn is not None:
            pulumi.set(__self__, "instance_profile_arn", instance_profile_arn)
        if is_meta_instance_profile is not None:
            pulumi.set(__self__, "is_meta_instance_profile", is_meta_instance_profile)
        if skip_validation is not None:
            pulumi.set(__self__, "skip_validation", skip_validation)

    @property
    @pulumi.getter(name="instanceProfileArn")
    def instance_profile_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "instance_profile_arn")

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_profile_arn", value)

    @property
    @pulumi.getter(name="isMetaInstanceProfile")
    def is_meta_instance_profile(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_meta_instance_profile")

    @is_meta_instance_profile.setter
    def is_meta_instance_profile(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_meta_instance_profile", value)

    @property
    @pulumi.getter(name="skipValidation")
    def skip_validation(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "skip_validation")

    @skip_validation.setter
    def skip_validation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_validation", value)


@pulumi.input_type
class _InstanceProfileState:
    def __init__(__self__, *,
                 instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 is_meta_instance_profile: Optional[pulumi.Input[bool]] = None,
                 skip_validation: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering InstanceProfile resources.
        """
        if instance_profile_arn is not None:
            pulumi.set(__self__, "instance_profile_arn", instance_profile_arn)
        if is_meta_instance_profile is not None:
            pulumi.set(__self__, "is_meta_instance_profile", is_meta_instance_profile)
        if skip_validation is not None:
            pulumi.set(__self__, "skip_validation", skip_validation)

    @property
    @pulumi.getter(name="instanceProfileArn")
    def instance_profile_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "instance_profile_arn")

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_profile_arn", value)

    @property
    @pulumi.getter(name="isMetaInstanceProfile")
    def is_meta_instance_profile(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_meta_instance_profile")

    @is_meta_instance_profile.setter
    def is_meta_instance_profile(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_meta_instance_profile", value)

    @property
    @pulumi.getter(name="skipValidation")
    def skip_validation(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "skip_validation")

    @skip_validation.setter
    def skip_validation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_validation", value)


class InstanceProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 is_meta_instance_profile: Optional[pulumi.Input[bool]] = None,
                 skip_validation: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a InstanceProfile resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InstanceProfileArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a InstanceProfile resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param InstanceProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 is_meta_instance_profile: Optional[pulumi.Input[bool]] = None,
                 skip_validation: Optional[pulumi.Input[bool]] = None,
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
            __props__ = InstanceProfileArgs.__new__(InstanceProfileArgs)

            __props__.__dict__["instance_profile_arn"] = instance_profile_arn
            __props__.__dict__["is_meta_instance_profile"] = is_meta_instance_profile
            __props__.__dict__["skip_validation"] = skip_validation
        super(InstanceProfile, __self__).__init__(
            'databricks:databricks/instanceProfile:InstanceProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_profile_arn: Optional[pulumi.Input[str]] = None,
            is_meta_instance_profile: Optional[pulumi.Input[bool]] = None,
            skip_validation: Optional[pulumi.Input[bool]] = None) -> 'InstanceProfile':
        """
        Get an existing InstanceProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceProfileState.__new__(_InstanceProfileState)

        __props__.__dict__["instance_profile_arn"] = instance_profile_arn
        __props__.__dict__["is_meta_instance_profile"] = is_meta_instance_profile
        __props__.__dict__["skip_validation"] = skip_validation
        return InstanceProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceProfileArn")
    def instance_profile_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "instance_profile_arn")

    @property
    @pulumi.getter(name="isMetaInstanceProfile")
    def is_meta_instance_profile(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "is_meta_instance_profile")

    @property
    @pulumi.getter(name="skipValidation")
    def skip_validation(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "skip_validation")

