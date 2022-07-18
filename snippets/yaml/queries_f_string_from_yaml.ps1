<#
	This PowerShell sample will convert the "sql_queries.yaml" file into an PowerShell Object,
	then parse it to the location:
		sql_connection_test → powershell
	and then inserts the value of the variable $Database_Name into the placeholder "0".

	Resulting in this:
		SELECT TOP (10)
		[IP_Address]
		,[Caption]
		FROM [{0}].[dbo].[NodesData]
		/*
		Arguments:
		0 = Database Name
		*/

	Turning into this:
		SELECT TOP (10)
		[IP_Address]
		,[Caption]
		FROM [SolarWindsOrion].[dbo].[NodesData]
		/*
		Arguments:
		0 = Database Name
		*/
#>

Import-Module powershell-yaml

#	The YAML file in this directory
$YamlFilePath = Join-Path -Path $PSScriptRoot -ChildPath '\sql_queries.yaml'

#	Load the content of the YAML file as a string
$YamlFile = Get-Content -Path $YamlFilePath | Out-String

#	convert the YAML file to a PSObject
$sql_queries_yaml = ConvertFrom-Yaml -Yaml $YamlFile

#	Some variables to inject into the query stored in the YAML file
$Database_Name = "SolarWindsOrion"

#	Do it
$SqlQuery = $sql_queries_yaml.sql_connection_test.powershell -f $Database_Name
Write-Host $SqlQuery -ForegroundColor Yellow