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