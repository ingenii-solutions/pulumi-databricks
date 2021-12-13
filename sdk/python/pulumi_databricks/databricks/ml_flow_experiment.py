# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MLFlowExperimentArgs', 'MLFlowExperiment']

@pulumi.input_type
class MLFlowExperimentArgs:
    def __init__(__self__, *,
                 artifact_location: Optional[pulumi.Input[str]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 experiment_id: Optional[pulumi.Input[str]] = None,
                 last_update_time: Optional[pulumi.Input[int]] = None,
                 lifecycle_stage: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MLFlowExperiment resource.
        """
        if artifact_location is not None:
            pulumi.set(__self__, "artifact_location", artifact_location)
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if experiment_id is not None:
            pulumi.set(__self__, "experiment_id", experiment_id)
        if last_update_time is not None:
            pulumi.set(__self__, "last_update_time", last_update_time)
        if lifecycle_stage is not None:
            pulumi.set(__self__, "lifecycle_stage", lifecycle_stage)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="artifactLocation")
    def artifact_location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "artifact_location")

    @artifact_location.setter
    def artifact_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "artifact_location", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="experimentId")
    def experiment_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "experiment_id")

    @experiment_id.setter
    def experiment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "experiment_id", value)

    @property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "last_update_time")

    @last_update_time.setter
    def last_update_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "last_update_time", value)

    @property
    @pulumi.getter(name="lifecycleStage")
    def lifecycle_stage(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "lifecycle_stage")

    @lifecycle_stage.setter
    def lifecycle_stage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_stage", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _MLFlowExperimentState:
    def __init__(__self__, *,
                 artifact_location: Optional[pulumi.Input[str]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 experiment_id: Optional[pulumi.Input[str]] = None,
                 last_update_time: Optional[pulumi.Input[int]] = None,
                 lifecycle_stage: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MLFlowExperiment resources.
        """
        if artifact_location is not None:
            pulumi.set(__self__, "artifact_location", artifact_location)
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if experiment_id is not None:
            pulumi.set(__self__, "experiment_id", experiment_id)
        if last_update_time is not None:
            pulumi.set(__self__, "last_update_time", last_update_time)
        if lifecycle_stage is not None:
            pulumi.set(__self__, "lifecycle_stage", lifecycle_stage)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="artifactLocation")
    def artifact_location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "artifact_location")

    @artifact_location.setter
    def artifact_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "artifact_location", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="experimentId")
    def experiment_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "experiment_id")

    @experiment_id.setter
    def experiment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "experiment_id", value)

    @property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "last_update_time")

    @last_update_time.setter
    def last_update_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "last_update_time", value)

    @property
    @pulumi.getter(name="lifecycleStage")
    def lifecycle_stage(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "lifecycle_stage")

    @lifecycle_stage.setter
    def lifecycle_stage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_stage", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class MLFlowExperiment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_location: Optional[pulumi.Input[str]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 experiment_id: Optional[pulumi.Input[str]] = None,
                 last_update_time: Optional[pulumi.Input[int]] = None,
                 lifecycle_stage: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a MLFlowExperiment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[MLFlowExperimentArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a MLFlowExperiment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MLFlowExperimentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MLFlowExperimentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_location: Optional[pulumi.Input[str]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 experiment_id: Optional[pulumi.Input[str]] = None,
                 last_update_time: Optional[pulumi.Input[int]] = None,
                 lifecycle_stage: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = MLFlowExperimentArgs.__new__(MLFlowExperimentArgs)

            __props__.__dict__["artifact_location"] = artifact_location
            __props__.__dict__["creation_time"] = creation_time
            __props__.__dict__["description"] = description
            __props__.__dict__["experiment_id"] = experiment_id
            __props__.__dict__["last_update_time"] = last_update_time
            __props__.__dict__["lifecycle_stage"] = lifecycle_stage
            __props__.__dict__["name"] = name
        super(MLFlowExperiment, __self__).__init__(
            'databricks:databricks/mLFlowExperiment:MLFlowExperiment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            artifact_location: Optional[pulumi.Input[str]] = None,
            creation_time: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            experiment_id: Optional[pulumi.Input[str]] = None,
            last_update_time: Optional[pulumi.Input[int]] = None,
            lifecycle_stage: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'MLFlowExperiment':
        """
        Get an existing MLFlowExperiment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MLFlowExperimentState.__new__(_MLFlowExperimentState)

        __props__.__dict__["artifact_location"] = artifact_location
        __props__.__dict__["creation_time"] = creation_time
        __props__.__dict__["description"] = description
        __props__.__dict__["experiment_id"] = experiment_id
        __props__.__dict__["last_update_time"] = last_update_time
        __props__.__dict__["lifecycle_stage"] = lifecycle_stage
        __props__.__dict__["name"] = name
        return MLFlowExperiment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="artifactLocation")
    def artifact_location(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "artifact_location")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="experimentId")
    def experiment_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "experiment_id")

    @property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> pulumi.Output[int]:
        return pulumi.get(self, "last_update_time")

    @property
    @pulumi.getter(name="lifecycleStage")
    def lifecycle_stage(self) -> pulumi.Output[str]:
        return pulumi.get(self, "lifecycle_stage")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")
