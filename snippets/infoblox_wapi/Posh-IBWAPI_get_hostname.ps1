<#
	This sample shows how to get the data related to a IPAM record
#>
Import-Module Posh-IBWAPI
Get-IBObject -ObjectType "record:host" -Filters "name=server1.lab.martincrothers.com" -ReturnAllFields