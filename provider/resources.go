// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package databricks

import (
	"fmt"
	"path/filepath"
	"unicode"

	"github.com/ingenii-solutions/pulumi-databricks/provider/pkg/version"

	"github.com/databrickslabs/terraform-provider-databricks/provider"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
)

// all of the token components used below.
const (
	// packages:
	mainPkg = "databricks"
	// modules:
	mainMod = "databricks" // the y module
)

// makeMember manufactures a type token for the package and the given module and type.
func makeMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(mainPkg + ":" + mod + ":" + mem)
}

// makeType manufactures a type token for the package and the given module and type.
func makeType(mod string, typ string) tokens.Type {
	return tokens.Type(makeMember(mod, typ))
}

// makeDataSource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the data source's
// first character.
func makeDataSource(mod string, res string) tokens.ModuleMember {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeMember(mod+"/"+fn, res)
}

// makeResource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the resource's
// first character.
func makeResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeType(mod+"/"+fn, res)
}

// boolRef returns a reference to the bool argument.
func boolRef(b bool) *bool {
	return &b
}

// stringValue gets a string value from a property map if present, else ""
func stringValue(vars resource.PropertyMap, prop resource.PropertyKey) string {
	val, ok := vars[prop]
	if ok && val.IsString() {
		return val.StringValue()
	}
	return ""
}

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

// managedByPulumi is a default used for some managed resources, in the absence of something more meaningful.
var managedByPulumi = &tfbridge.DefaultInfo{Value: "Managed by Pulumi"}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(provider.DatabricksProvider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "databricks",
		Description: "A Pulumi package for creating and managing Databricks cloud resources.",
		Keywords:    []string{"pulumi", "dataricks"},
		License:     "Apache-2.0",
		Homepage:    "https://ingenii.dev",
		Repository:  "https://github.com/ingenii-solutions/pulumi-databricks",
		Config:      map[string]*tfbridge.SchemaInfo{
			// Add any required configuration here, or remove the example below if
			// no additional points are required.
			// "region": {
			// 	Type: makeType("region", "Region"),
			// 	Default: &tfbridge.DefaultInfo{
			// 		EnvVars: []string{"AWS_REGION", "AWS_DEFAULT_REGION"},
			// 	},
			// },
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"databricks_aws_s3_mount":                {Tok: makeResource(mainMod, "AwsS3Mount")},
			"databricks_azure_adls_gen1_mount":       {Tok: makeResource(mainMod, "AzureAdlsGen1Mount")},
			"databricks_azure_adls_gen2_mount":       {Tok: makeResource(mainMod, "AzureAdlsGen2Mount")},
			"databricks_azure_blob_mount":            {Tok: makeResource(mainMod, "AzureBlobMount")},
			"databricks_catalog":                     {Tok: makeResource(mainMod, "Catalog")},
			"databricks_cluster":                     {Tok: makeResource(mainMod, "Cluster")},
			"databricks_cluster_policy":              {Tok: makeResource(mainMod, "ClusterPolicy")},
			"databricks_dbfs_file":                   {Tok: makeResource(mainMod, "AzureDbfsFile")},
			"databricks_directory":                   {Tok: makeResource(mainMod, "Directory")},
			"databricks_global_init_script":          {Tok: makeResource(mainMod, "GlobalInitScript")},
			"databricks_group":                       {Tok: makeResource(mainMod, "Group")},
			"databricks_group_instance_profile":      {Tok: makeResource(mainMod, "GroupInstanceProfile")},
			"databricks_group_member":                {Tok: makeResource(mainMod, "GroupMember")},
			"databricks_instance_pool":               {Tok: makeResource(mainMod, "InstancePool")},
			"databricks_instance_profile":            {Tok: makeResource(mainMod, "InstanceProfile")},
			"databricks_ip_access_list":              {Tok: makeResource(mainMod, "IPAccessList")},
			"databricks_job":                         {Tok: makeResource(mainMod, "Job")},
			"databricks_metastore":                   {Tok: makeResource(mainMod, "Metastore")},
			"databricks_metastore_assignment":        {Tok: makeResource(mainMod, "MetastoreAssignment")},
			"databricks_metastore_data_access":       {Tok: makeResource(mainMod, "MetastoreDataAccess")},
			"databricks_mlflow_experiment":           {Tok: makeResource(mainMod, "MLFlowExperiment")},
			"databricks_mlflow_model":                {Tok: makeResource(mainMod, "MLFlowModel")},
			"databricks_mount":                       {Tok: makeResource(mainMod, "DatabricksMount")},
			"databricks_mws_credentials":             {Tok: makeResource(mainMod, "MwsCredentials")},
			"databricks_mws_customer_managed_keys":   {Tok: makeResource(mainMod, "MwsCustomerManagedKeys")},
			"databricks_mws_log_delivery":            {Tok: makeResource(mainMod, "MwsLogDelivery")},
			"databricks_mws_networks":                {Tok: makeResource(mainMod, "MwsNetworks")},
			"databricks_mws_private_access_settings": {Tok: makeResource(mainMod, "MwsPrivateAccessSettings")},
			"databricks_mws_storage_configurations":  {Tok: makeResource(mainMod, "MwsStorageConfigurations")},
			"databricks_mws_vpc_endpoint":            {Tok: makeResource(mainMod, "MwsVpcEndpoint")},
			"databricks_mws_workspaces":              {Tok: makeResource(mainMod, "MwsWorkspaces")},
			"databricks_notebook":                    {Tok: makeResource(mainMod, "Notebook")},
			"databricks_obo_token":                   {Tok: makeResource(mainMod, "OboToken")},
			"databricks_permissions":                 {Tok: makeResource(mainMod, "Permissions")},
			"databricks_pipeline":                    {Tok: makeResource(mainMod, "Pipeline")},
			"databricks_repo":                        {Tok: makeResource(mainMod, "Repo")},
			"databricks_schema":                      {Tok: makeResource(mainMod, "Schema")},
			"databricks_secret":                      {Tok: makeResource(mainMod, "Secret")},
			"databricks_secret_acl":                  {Tok: makeResource(mainMod, "SecretAcl")},
			"databricks_secret_scope":                {Tok: makeResource(mainMod, "SecretScope")},
			"databricks_service_principal":           {Tok: makeResource(mainMod, "ServicePrincipal")},
			"databricks_sql_dashboard":               {Tok: makeResource(mainMod, "SqlDashboard")},
			"databricks_sql_endpoint":                {Tok: makeResource(mainMod, "SqlEndpoint")},
			"databricks_sql_global_config":           {Tok: makeResource(mainMod, "SqlGlobalConfig")},
			"databricks_sql_permissions":             {Tok: makeResource(mainMod, "SqlPermissions")},
			"databricks_sql_query":                   {Tok: makeResource(mainMod, "SqlQuery")},
			"databricks_sql_visualization":           {Tok: makeResource(mainMod, "SqlVisualization")},
			"databricks_sql_widget":                  {Tok: makeResource(mainMod, "SqlWidget")},
			"databricks_token":                       {Tok: makeResource(mainMod, "Token")},
			"databricks_user":                        {Tok: makeResource(mainMod, "User")},
			"databricks_user_instance_profile":       {Tok: makeResource(mainMod, "UserInstanceProfile")},
			"databricks_workspace_conf":              {Tok: makeResource(mainMod, "WorkspaceConf")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			"databricks_aws_crossaccount_policy": {Tok: makeDataSource(mainMod, "getAwsCrossAccountPolicy")},
			"databricks_aws_assume_role_policy":  {Tok: makeDataSource(mainMod, "getAwsAssumeRolePolicy")},
			"databricks_aws_bucket_policy":       {Tok: makeDataSource(mainMod, "getAwsBucketPolicy")},
			"databricks_current_user":            {Tok: makeDataSource(mainMod, "getCurrentUser")},
			"databricks_dbfs_file":               {Tok: makeDataSource(mainMod, "getDbfsFile")},
			"databricks_dbfs_file_paths":         {Tok: makeDataSource(mainMod, "getDbfsFilePaths")},
			"databricks_group":                   {Tok: makeDataSource(mainMod, "getGroup")},
			"databricks_node_type":               {Tok: makeDataSource(mainMod, "getNodeType")},
			"databricks_notebook":                {Tok: makeDataSource(mainMod, "getNotebook")},
			"databricks_notebook_paths":          {Tok: makeDataSource(mainMod, "getNotebookPaths")},
			"databricks_spark_version":           {Tok: makeDataSource(mainMod, "getSparkVersion")},
			"databricks_user":                    {Tok: makeDataSource(mainMod, "getUser")},
			"databricks_zones":                   {Tok: makeDataSource(mainMod, "getZones")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi":                       "3.*",
				"System.Collections.Immutable": "1.6.0",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
