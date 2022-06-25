Import-Module SqlServer

<#
	This function needs to be executed in a terminal session running from an account with permissions to
	the SQL server/database. As structured is using Windows authentication. If you need to run this as a
	different user, you will need to have the ability to use "CredSSP".
#>


$SqlServerInstance = 'oriondb\orionprod'
$Database = 'SolarWindsOrion'

$Query = @"
	SELECT TOP 4
		[NodeID]
	,	[Caption]
	,	[IP_Address]
	FROM [$Database].[dbo].[NodesData] 
"@

$QueryResult = Invoke-Sqlcmd -ServerInstance $SqlServerInstance -Database $Database -Query $Query -ErrorAction Stop

$QueryResult