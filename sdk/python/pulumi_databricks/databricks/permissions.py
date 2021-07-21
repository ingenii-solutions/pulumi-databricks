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

__all__ = ['PermissionsArgs', 'Permissions']

@pulumi.input_type
class PermissionsArgs:
    def __init__(__self__, *,
                 access_controls: pulumi.Input[Sequence[pulumi.Input['PermissionsAccessControlArgs']]],
                 authorization: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cluster_policy_id: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 directory_path: Optional[pulumi.Input[str]] = None,
                 instance_pool_id: Optional[pulumi.Input[str]] = None,
                 job_id: Optional[pulumi.Input[str]] = None,
                 notebook_id: Optional[pulumi.Input[str]] = None,
                 notebook_path: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 sql_alert_id: Optional[pulumi.Input[str]] = None,
                 sql_dashboard_id: Optional[pulumi.Input[str]] = None,
                 sql_endpoint_id: Optional[pulumi.Input[str]] = None,
                 sql_query_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Permissions resource.
        """
        pulumi.set(__self__, "access_controls", access_controls)
        if authorization is not None:
            pulumi.set(__self__, "authorization", authorization)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if cluster_policy_id is not None:
            pulumi.set(__self__, "cluster_policy_id", cluster_policy_id)
        if directory_id is not None:
            pulumi.set(__self__, "directory_id", directory_id)
        if directory_path is not None:
            pulumi.set(__self__, "directory_path", directory_path)
        if instance_pool_id is not None:
            pulumi.set(__self__, "instance_pool_id", instance_pool_id)
        if job_id is not None:
            pulumi.set(__self__, "job_id", job_id)
        if notebook_id is not None:
            pulumi.set(__self__, "notebook_id", notebook_id)
        if notebook_path is not None:
            pulumi.set(__self__, "notebook_path", notebook_path)
        if object_type is not None:
            pulumi.set(__self__, "object_type", object_type)
        if sql_alert_id is not None:
            pulumi.set(__self__, "sql_alert_id", sql_alert_id)
        if sql_dashboard_id is not None:
            pulumi.set(__self__, "sql_dashboard_id", sql_dashboard_id)
        if sql_endpoint_id is not None:
            pulumi.set(__self__, "sql_endpoint_id", sql_endpoint_id)
        if sql_query_id is not None:
            pulumi.set(__self__, "sql_query_id", sql_query_id)

    @property
    @pulumi.getter(name="accessControls")
    def access_controls(self) -> pulumi.Input[Sequence[pulumi.Input['PermissionsAccessControlArgs']]]:
        return pulumi.get(self, "access_controls")

    @access_controls.setter
    def access_controls(self, value: pulumi.Input[Sequence[pulumi.Input['PermissionsAccessControlArgs']]]):
        pulumi.set(self, "access_controls", value)

    @property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authorization")

    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="clusterPolicyId")
    def cluster_policy_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_policy_id")

    @cluster_policy_id.setter
    def cluster_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_policy_id", value)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "directory_id")

    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_id", value)

    @property
    @pulumi.getter(name="directoryPath")
    def directory_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "directory_path")

    @directory_path.setter
    def directory_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_path", value)

    @property
    @pulumi.getter(name="instancePoolId")
    def instance_pool_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "instance_pool_id")

    @instance_pool_id.setter
    def instance_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_pool_id", value)

    @property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "job_id")

    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_id", value)

    @property
    @pulumi.getter(name="notebookId")
    def notebook_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "notebook_id")

    @notebook_id.setter
    def notebook_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notebook_id", value)

    @property
    @pulumi.getter(name="notebookPath")
    def notebook_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "notebook_path")

    @notebook_path.setter
    def notebook_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notebook_path", value)

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "object_type")

    @object_type.setter
    def object_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_type", value)

    @property
    @pulumi.getter(name="sqlAlertId")
    def sql_alert_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sql_alert_id")

    @sql_alert_id.setter
    def sql_alert_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_alert_id", value)

    @property
    @pulumi.getter(name="sqlDashboardId")
    def sql_dashboard_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sql_dashboard_id")

    @sql_dashboard_id.setter
    def sql_dashboard_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_dashboard_id", value)

    @property
    @pulumi.getter(name="sqlEndpointId")
    def sql_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sql_endpoint_id")

    @sql_endpoint_id.setter
    def sql_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_endpoint_id", value)

    @property
    @pulumi.getter(name="sqlQueryId")
    def sql_query_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sql_query_id")

    @sql_query_id.setter
    def sql_query_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_query_id", value)


@pulumi.input_type
class _PermissionsState:
    def __init__(__self__, *,
                 access_controls: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionsAccessControlArgs']]]] = None,
                 authorization: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cluster_policy_id: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 directory_path: Optional[pulumi.Input[str]] = None,
                 instance_pool_id: Optional[pulumi.Input[str]] = None,
                 job_id: Optional[pulumi.Input[str]] = None,
                 notebook_id: Optional[pulumi.Input[str]] = None,
                 notebook_path: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 sql_alert_id: Optional[pulumi.Input[str]] = None,
                 sql_dashboard_id: Optional[pulumi.Input[str]] = None,
                 sql_endpoint_id: Optional[pulumi.Input[str]] = None,
                 sql_query_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Permissions resources.
        """
        if access_controls is not None:
            pulumi.set(__self__, "access_controls", access_controls)
        if authorization is not None:
            pulumi.set(__self__, "authorization", authorization)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if cluster_policy_id is not None:
            pulumi.set(__self__, "cluster_policy_id", cluster_policy_id)
        if directory_id is not None:
            pulumi.set(__self__, "directory_id", directory_id)
        if directory_path is not None:
            pulumi.set(__self__, "directory_path", directory_path)
        if instance_pool_id is not None:
            pulumi.set(__self__, "instance_pool_id", instance_pool_id)
        if job_id is not None:
            pulumi.set(__self__, "job_id", job_id)
        if notebook_id is not None:
            pulumi.set(__self__, "notebook_id", notebook_id)
        if notebook_path is not None:
            pulumi.set(__self__, "notebook_path", notebook_path)
        if object_type is not None:
            pulumi.set(__self__, "object_type", object_type)
        if sql_alert_id is not None:
            pulumi.set(__self__, "sql_alert_id", sql_alert_id)
        if sql_dashboard_id is not None:
            pulumi.set(__self__, "sql_dashboard_id", sql_dashboard_id)
        if sql_endpoint_id is not None:
            pulumi.set(__self__, "sql_endpoint_id", sql_endpoint_id)
        if sql_query_id is not None:
            pulumi.set(__self__, "sql_query_id", sql_query_id)

    @property
    @pulumi.getter(name="accessControls")
    def access_controls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PermissionsAccessControlArgs']]]]:
        return pulumi.get(self, "access_controls")

    @access_controls.setter
    def access_controls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionsAccessControlArgs']]]]):
        pulumi.set(self, "access_controls", value)

    @property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authorization")

    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="clusterPolicyId")
    def cluster_policy_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_policy_id")

    @cluster_policy_id.setter
    def cluster_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_policy_id", value)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "directory_id")

    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_id", value)

    @property
    @pulumi.getter(name="directoryPath")
    def directory_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "directory_path")

    @directory_path.setter
    def directory_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_path", value)

    @property
    @pulumi.getter(name="instancePoolId")
    def instance_pool_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "instance_pool_id")

    @instance_pool_id.setter
    def instance_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_pool_id", value)

    @property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "job_id")

    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_id", value)

    @property
    @pulumi.getter(name="notebookId")
    def notebook_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "notebook_id")

    @notebook_id.setter
    def notebook_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notebook_id", value)

    @property
    @pulumi.getter(name="notebookPath")
    def notebook_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "notebook_path")

    @notebook_path.setter
    def notebook_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notebook_path", value)

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "object_type")

    @object_type.setter
    def object_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_type", value)

    @property
    @pulumi.getter(name="sqlAlertId")
    def sql_alert_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sql_alert_id")

    @sql_alert_id.setter
    def sql_alert_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_alert_id", value)

    @property
    @pulumi.getter(name="sqlDashboardId")
    def sql_dashboard_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sql_dashboard_id")

    @sql_dashboard_id.setter
    def sql_dashboard_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_dashboard_id", value)

    @property
    @pulumi.getter(name="sqlEndpointId")
    def sql_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sql_endpoint_id")

    @sql_endpoint_id.setter
    def sql_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_endpoint_id", value)

    @property
    @pulumi.getter(name="sqlQueryId")
    def sql_query_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sql_query_id")

    @sql_query_id.setter
    def sql_query_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_query_id", value)


class Permissions(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_controls: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionsAccessControlArgs']]]]] = None,
                 authorization: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cluster_policy_id: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 directory_path: Optional[pulumi.Input[str]] = None,
                 instance_pool_id: Optional[pulumi.Input[str]] = None,
                 job_id: Optional[pulumi.Input[str]] = None,
                 notebook_id: Optional[pulumi.Input[str]] = None,
                 notebook_path: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 sql_alert_id: Optional[pulumi.Input[str]] = None,
                 sql_dashboard_id: Optional[pulumi.Input[str]] = None,
                 sql_endpoint_id: Optional[pulumi.Input[str]] = None,
                 sql_query_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Permissions resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PermissionsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Permissions resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PermissionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PermissionsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_controls: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionsAccessControlArgs']]]]] = None,
                 authorization: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cluster_policy_id: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 directory_path: Optional[pulumi.Input[str]] = None,
                 instance_pool_id: Optional[pulumi.Input[str]] = None,
                 job_id: Optional[pulumi.Input[str]] = None,
                 notebook_id: Optional[pulumi.Input[str]] = None,
                 notebook_path: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 sql_alert_id: Optional[pulumi.Input[str]] = None,
                 sql_dashboard_id: Optional[pulumi.Input[str]] = None,
                 sql_endpoint_id: Optional[pulumi.Input[str]] = None,
                 sql_query_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = PermissionsArgs.__new__(PermissionsArgs)

            if access_controls is None and not opts.urn:
                raise TypeError("Missing required property 'access_controls'")
            __props__.__dict__["access_controls"] = access_controls
            __props__.__dict__["authorization"] = authorization
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["cluster_policy_id"] = cluster_policy_id
            __props__.__dict__["directory_id"] = directory_id
            __props__.__dict__["directory_path"] = directory_path
            __props__.__dict__["instance_pool_id"] = instance_pool_id
            __props__.__dict__["job_id"] = job_id
            __props__.__dict__["notebook_id"] = notebook_id
            __props__.__dict__["notebook_path"] = notebook_path
            __props__.__dict__["object_type"] = object_type
            __props__.__dict__["sql_alert_id"] = sql_alert_id
            __props__.__dict__["sql_dashboard_id"] = sql_dashboard_id
            __props__.__dict__["sql_endpoint_id"] = sql_endpoint_id
            __props__.__dict__["sql_query_id"] = sql_query_id
        super(Permissions, __self__).__init__(
            'databricks:databricks/permissions:Permissions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_controls: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionsAccessControlArgs']]]]] = None,
            authorization: Optional[pulumi.Input[str]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            cluster_policy_id: Optional[pulumi.Input[str]] = None,
            directory_id: Optional[pulumi.Input[str]] = None,
            directory_path: Optional[pulumi.Input[str]] = None,
            instance_pool_id: Optional[pulumi.Input[str]] = None,
            job_id: Optional[pulumi.Input[str]] = None,
            notebook_id: Optional[pulumi.Input[str]] = None,
            notebook_path: Optional[pulumi.Input[str]] = None,
            object_type: Optional[pulumi.Input[str]] = None,
            sql_alert_id: Optional[pulumi.Input[str]] = None,
            sql_dashboard_id: Optional[pulumi.Input[str]] = None,
            sql_endpoint_id: Optional[pulumi.Input[str]] = None,
            sql_query_id: Optional[pulumi.Input[str]] = None) -> 'Permissions':
        """
        Get an existing Permissions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PermissionsState.__new__(_PermissionsState)

        __props__.__dict__["access_controls"] = access_controls
        __props__.__dict__["authorization"] = authorization
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["cluster_policy_id"] = cluster_policy_id
        __props__.__dict__["directory_id"] = directory_id
        __props__.__dict__["directory_path"] = directory_path
        __props__.__dict__["instance_pool_id"] = instance_pool_id
        __props__.__dict__["job_id"] = job_id
        __props__.__dict__["notebook_id"] = notebook_id
        __props__.__dict__["notebook_path"] = notebook_path
        __props__.__dict__["object_type"] = object_type
        __props__.__dict__["sql_alert_id"] = sql_alert_id
        __props__.__dict__["sql_dashboard_id"] = sql_dashboard_id
        __props__.__dict__["sql_endpoint_id"] = sql_endpoint_id
        __props__.__dict__["sql_query_id"] = sql_query_id
        return Permissions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessControls")
    def access_controls(self) -> pulumi.Output[Sequence['outputs.PermissionsAccessControl']]:
        return pulumi.get(self, "access_controls")

    @property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="clusterPolicyId")
    def cluster_policy_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cluster_policy_id")

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "directory_id")

    @property
    @pulumi.getter(name="directoryPath")
    def directory_path(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "directory_path")

    @property
    @pulumi.getter(name="instancePoolId")
    def instance_pool_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "instance_pool_id")

    @property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "job_id")

    @property
    @pulumi.getter(name="notebookId")
    def notebook_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "notebook_id")

    @property
    @pulumi.getter(name="notebookPath")
    def notebook_path(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "notebook_path")

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "object_type")

    @property
    @pulumi.getter(name="sqlAlertId")
    def sql_alert_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sql_alert_id")

    @property
    @pulumi.getter(name="sqlDashboardId")
    def sql_dashboard_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sql_dashboard_id")

    @property
    @pulumi.getter(name="sqlEndpointId")
    def sql_endpoint_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sql_endpoint_id")

    @property
    @pulumi.getter(name="sqlQueryId")
    def sql_query_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sql_query_id")

