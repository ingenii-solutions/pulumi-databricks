module github.com/ingenii-solutions/pulumi-databricks/provider

go 1.16

replace (
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20210402103405-f5979773e8ba
)

require (
	github.com/databrickslabs/terraform-provider-databricks v0.5.3
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.4.1-0.20210714215802-5020116ac4e6
	github.com/pulumi/pulumi/pkg/v3 v3.7.1-0.20210714212650-083fc64ff547 // indirect
	github.com/pulumi/pulumi/sdk/v3 v3.7.1-0.20210714111852-eb8e1585c3b7
)
