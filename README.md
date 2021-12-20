# IMPORTANT

This is a pre-release. Please do not use it in production.

We have requested permission from the Pulumi team to start working on porting (or bridging) the Terraform Databricks provider to Pulumi.

This release matches version 0.4.0 of the Terraform Databricks provider.

## Notes

* Install [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
* Install [PulumiCTL](https://github.com/pulumi/pulumictl)
* Install Go 1.16
* Install Python 3.x

Run the following commands:

`cd provider && go mod tidy`
`make tfgen`  
`make build_provider`  
`make build_sdks`  

If additional mapping is required, open the `/provider/resources.go` file and perform the mapping by using the [provider.go](https://github.com/databrickslabs/terraform-provider-databricks/blob/master/provider/provider.go) file as reference.

Run `pip install` when the Python SDK is built. If duplicate attribuets are detected, fix them by going to the files specified in the pip output.

Once the duplicates are resolved, proceed by using `twine` to upload the latest version of the Python SDK to pypi.

Also, we need to create another release of this repository and upload all provider binaries. Linux, Windows, Darwin.

> This repository is in a shabby state, but we cannot allocate enough time to fully automate the Pulumi <> Terraform bridging. If anyone is happy to spend the time, please reach out.

We have only generated the Python SDKs.

* Previous working version: `0.0.6` (mapped to Terraform Databricks provider version `0.4.0`)  
* Latest working version: `0.0.7` (mapped to Terraform Databricks provider version `0.4.1`)

## Usage

### Python

```shell
pip install pulumi-databricks
```