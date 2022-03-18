# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetJobsResult',
    'AwaitableGetJobsResult',
    'get_jobs',
]

@pulumi.output_type
class GetJobsResult:
    """
    A collection of values returned by getJobs.
    """
    def __init__(__self__, id=None, ids=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, dict):
            raise TypeError("Expected argument 'ids' to be a dict")
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Mapping[str, Any]:
        return pulumi.get(self, "ids")


class AwaitableGetJobsResult(GetJobsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJobsResult(
            id=self.id,
            ids=self.ids)


def get_jobs(ids: Optional[Mapping[str, Any]] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJobsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['ids'] = ids
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('databricks:databricks/getJobs:getJobs', __args__, opts=opts, typ=GetJobsResult).value

    return AwaitableGetJobsResult(
        id=__ret__.id,
        ids=__ret__.ids)