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

__all__ = ['MLFlowWebhookArgs', 'MLFlowWebhook']

@pulumi.input_type
class MLFlowWebhookArgs:
    def __init__(__self__, *,
                 events: pulumi.Input[Sequence[pulumi.Input[str]]],
                 description: Optional[pulumi.Input[str]] = None,
                 http_url_spec: Optional[pulumi.Input['MLFlowWebhookHttpUrlSpecArgs']] = None,
                 job_spec: Optional[pulumi.Input['MLFlowWebhookJobSpecArgs']] = None,
                 model_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MLFlowWebhook resource.
        """
        pulumi.set(__self__, "events", events)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if http_url_spec is not None:
            pulumi.set(__self__, "http_url_spec", http_url_spec)
        if job_spec is not None:
            pulumi.set(__self__, "job_spec", job_spec)
        if model_name is not None:
            pulumi.set(__self__, "model_name", model_name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def events(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="httpUrlSpec")
    def http_url_spec(self) -> Optional[pulumi.Input['MLFlowWebhookHttpUrlSpecArgs']]:
        return pulumi.get(self, "http_url_spec")

    @http_url_spec.setter
    def http_url_spec(self, value: Optional[pulumi.Input['MLFlowWebhookHttpUrlSpecArgs']]):
        pulumi.set(self, "http_url_spec", value)

    @property
    @pulumi.getter(name="jobSpec")
    def job_spec(self) -> Optional[pulumi.Input['MLFlowWebhookJobSpecArgs']]:
        return pulumi.get(self, "job_spec")

    @job_spec.setter
    def job_spec(self, value: Optional[pulumi.Input['MLFlowWebhookJobSpecArgs']]):
        pulumi.set(self, "job_spec", value)

    @property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "model_name")

    @model_name.setter
    def model_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _MLFlowWebhookState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 http_url_spec: Optional[pulumi.Input['MLFlowWebhookHttpUrlSpecArgs']] = None,
                 job_spec: Optional[pulumi.Input['MLFlowWebhookJobSpecArgs']] = None,
                 model_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MLFlowWebhook resources.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if events is not None:
            pulumi.set(__self__, "events", events)
        if http_url_spec is not None:
            pulumi.set(__self__, "http_url_spec", http_url_spec)
        if job_spec is not None:
            pulumi.set(__self__, "job_spec", job_spec)
        if model_name is not None:
            pulumi.set(__self__, "model_name", model_name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter(name="httpUrlSpec")
    def http_url_spec(self) -> Optional[pulumi.Input['MLFlowWebhookHttpUrlSpecArgs']]:
        return pulumi.get(self, "http_url_spec")

    @http_url_spec.setter
    def http_url_spec(self, value: Optional[pulumi.Input['MLFlowWebhookHttpUrlSpecArgs']]):
        pulumi.set(self, "http_url_spec", value)

    @property
    @pulumi.getter(name="jobSpec")
    def job_spec(self) -> Optional[pulumi.Input['MLFlowWebhookJobSpecArgs']]:
        return pulumi.get(self, "job_spec")

    @job_spec.setter
    def job_spec(self, value: Optional[pulumi.Input['MLFlowWebhookJobSpecArgs']]):
        pulumi.set(self, "job_spec", value)

    @property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "model_name")

    @model_name.setter
    def model_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class MLFlowWebhook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 http_url_spec: Optional[pulumi.Input[pulumi.InputType['MLFlowWebhookHttpUrlSpecArgs']]] = None,
                 job_spec: Optional[pulumi.Input[pulumi.InputType['MLFlowWebhookJobSpecArgs']]] = None,
                 model_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a MLFlowWebhook resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MLFlowWebhookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a MLFlowWebhook resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MLFlowWebhookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MLFlowWebhookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 http_url_spec: Optional[pulumi.Input[pulumi.InputType['MLFlowWebhookHttpUrlSpecArgs']]] = None,
                 job_spec: Optional[pulumi.Input[pulumi.InputType['MLFlowWebhookJobSpecArgs']]] = None,
                 model_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = MLFlowWebhookArgs.__new__(MLFlowWebhookArgs)

            __props__.__dict__["description"] = description
            if events is None and not opts.urn:
                raise TypeError("Missing required property 'events'")
            __props__.__dict__["events"] = events
            __props__.__dict__["http_url_spec"] = http_url_spec
            __props__.__dict__["job_spec"] = job_spec
            __props__.__dict__["model_name"] = model_name
            __props__.__dict__["status"] = status
        super(MLFlowWebhook, __self__).__init__(
            'databricks:databricks/mLFlowWebhook:MLFlowWebhook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            http_url_spec: Optional[pulumi.Input[pulumi.InputType['MLFlowWebhookHttpUrlSpecArgs']]] = None,
            job_spec: Optional[pulumi.Input[pulumi.InputType['MLFlowWebhookJobSpecArgs']]] = None,
            model_name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'MLFlowWebhook':
        """
        Get an existing MLFlowWebhook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MLFlowWebhookState.__new__(_MLFlowWebhookState)

        __props__.__dict__["description"] = description
        __props__.__dict__["events"] = events
        __props__.__dict__["http_url_spec"] = http_url_spec
        __props__.__dict__["job_spec"] = job_spec
        __props__.__dict__["model_name"] = model_name
        __props__.__dict__["status"] = status
        return MLFlowWebhook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def events(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "events")

    @property
    @pulumi.getter(name="httpUrlSpec")
    def http_url_spec(self) -> pulumi.Output[Optional['outputs.MLFlowWebhookHttpUrlSpec']]:
        return pulumi.get(self, "http_url_spec")

    @property
    @pulumi.getter(name="jobSpec")
    def job_spec(self) -> pulumi.Output[Optional['outputs.MLFlowWebhookJobSpec']]:
        return pulumi.get(self, "job_spec")

    @property
    @pulumi.getter(name="modelName")
    def model_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "model_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "status")

