# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetGroupResult',
    'AwaitableGetGroupResult',
    'get_group',
]

@pulumi.output_type
class GetGroupResult:
    """
    A collection of values returned by getGroup.
    """
    def __init__(__self__, allow_cluster_create=None, allow_instance_pool_create=None, allow_sql_analytics_access=None, display_name=None, groups=None, id=None, instance_profiles=None, members=None, recursive=None, workspace_access=None):
        if allow_cluster_create and not isinstance(allow_cluster_create, bool):
            raise TypeError("Expected argument 'allow_cluster_create' to be a bool")
        pulumi.set(__self__, "allow_cluster_create", allow_cluster_create)
        if allow_instance_pool_create and not isinstance(allow_instance_pool_create, bool):
            raise TypeError("Expected argument 'allow_instance_pool_create' to be a bool")
        pulumi.set(__self__, "allow_instance_pool_create", allow_instance_pool_create)
        if allow_sql_analytics_access and not isinstance(allow_sql_analytics_access, bool):
            raise TypeError("Expected argument 'allow_sql_analytics_access' to be a bool")
        pulumi.set(__self__, "allow_sql_analytics_access", allow_sql_analytics_access)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_profiles and not isinstance(instance_profiles, list):
            raise TypeError("Expected argument 'instance_profiles' to be a list")
        pulumi.set(__self__, "instance_profiles", instance_profiles)
        if members and not isinstance(members, list):
            raise TypeError("Expected argument 'members' to be a list")
        pulumi.set(__self__, "members", members)
        if recursive and not isinstance(recursive, bool):
            raise TypeError("Expected argument 'recursive' to be a bool")
        pulumi.set(__self__, "recursive", recursive)
        if workspace_access and not isinstance(workspace_access, bool):
            raise TypeError("Expected argument 'workspace_access' to be a bool")
        pulumi.set(__self__, "workspace_access", workspace_access)

    @property
    @pulumi.getter(name="allowClusterCreate")
    def allow_cluster_create(self) -> Optional[bool]:
        return pulumi.get(self, "allow_cluster_create")

    @property
    @pulumi.getter(name="allowInstancePoolCreate")
    def allow_instance_pool_create(self) -> Optional[bool]:
        return pulumi.get(self, "allow_instance_pool_create")

    @property
    @pulumi.getter(name="allowSqlAnalyticsAccess")
    def allow_sql_analytics_access(self) -> Optional[bool]:
        return pulumi.get(self, "allow_sql_analytics_access")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def groups(self) -> Sequence[str]:
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceProfiles")
    def instance_profiles(self) -> Sequence[str]:
        return pulumi.get(self, "instance_profiles")

    @property
    @pulumi.getter
    def members(self) -> Sequence[str]:
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def recursive(self) -> Optional[bool]:
        return pulumi.get(self, "recursive")

    @property
    @pulumi.getter(name="workspaceAccess")
    def workspace_access(self) -> Optional[bool]:
        return pulumi.get(self, "workspace_access")


class AwaitableGetGroupResult(GetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupResult(
            allow_cluster_create=self.allow_cluster_create,
            allow_instance_pool_create=self.allow_instance_pool_create,
            allow_sql_analytics_access=self.allow_sql_analytics_access,
            display_name=self.display_name,
            groups=self.groups,
            id=self.id,
            instance_profiles=self.instance_profiles,
            members=self.members,
            recursive=self.recursive,
            workspace_access=self.workspace_access)


def get_group(allow_cluster_create: Optional[bool] = None,
              allow_instance_pool_create: Optional[bool] = None,
              allow_sql_analytics_access: Optional[bool] = None,
              display_name: Optional[str] = None,
              groups: Optional[Sequence[str]] = None,
              instance_profiles: Optional[Sequence[str]] = None,
              members: Optional[Sequence[str]] = None,
              recursive: Optional[bool] = None,
              workspace_access: Optional[bool] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['allowClusterCreate'] = allow_cluster_create
    __args__['allowInstancePoolCreate'] = allow_instance_pool_create
    __args__['allowSqlAnalyticsAccess'] = allow_sql_analytics_access
    __args__['displayName'] = display_name
    __args__['groups'] = groups
    __args__['instanceProfiles'] = instance_profiles
    __args__['members'] = members
    __args__['recursive'] = recursive
    __args__['workspaceAccess'] = workspace_access
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('databricks:databricks/getGroup:getGroup', __args__, opts=opts, typ=GetGroupResult).value

    return AwaitableGetGroupResult(
        allow_cluster_create=__ret__.allow_cluster_create,
        allow_instance_pool_create=__ret__.allow_instance_pool_create,
        allow_sql_analytics_access=__ret__.allow_sql_analytics_access,
        display_name=__ret__.display_name,
        groups=__ret__.groups,
        id=__ret__.id,
        instance_profiles=__ret__.instance_profiles,
        members=__ret__.members,
        recursive=__ret__.recursive,
        workspace_access=__ret__.workspace_access)
