Import-Module PSWriteColor


$Server_Names = @(
	'nausabh1sopp101',
	'server-win-orion-mpe-01',
	'srv001'
)
$Longest_ServerName = ($ServerNames | Measure-Object -Maximum -Property Length).Maximum


$Banner_Border_Padding_LeftRight = 4
$Banner_Total_Width = ($LongestServerName + ($Banner_Border_Padding_LeftRight * 2))
$Banner_Empty_Line_Fill = $Banner_Total_Width -2
$Banner_Empty_Line_String = "#" + (" " * $Banner_Empty_Line_Fill) + "#"
$Banner_Text_Line_Max_Length = $Banner_Total_Width - 6


$Banner_TopBottom_Border = "#" * $Banner_Total_Width

Write-Host $Banner_TopBottom_Border -ForegroundColor Cyan
Write-Host $Banner_Empty_Line_String -ForegroundColor Cyan



$Long_String = "You are about to shut-down the Orion services on the servers listed below."


[System.Collections.ArrayList]$Long_String_Word_Array = $Long_String -split "\s"




$Long_String_Line_Breaks_Complete = New-Object System.Collections.ArrayList




$Long_String_Line_Breaks_Iterator = 0
$Long_String_Word_Array_Iterator = 0


do {
	


	
	$Long_String_Line_Breaks_Current_Line = New-Object System.Collections.ArrayList
	do {
		$Next_Word_Length = $Long_String_Word_Array[$Long_String_Word_Array_Iterator]
		Write-Color "Length of next word: ", $Next_Word_Length -Color Cyan, Green



	} while (
		$Long_String_Line_Breaks_Current_Line -lt $Banner_Text_Line_Max_Length
	)




	$Long_String_Line_Breaks_Iterator++
	$Long_String_Word_Array_Iterator++
} while (
	
)




$Array_Test = @("The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog.")
Write-Color "The total count of words in Array_Test is: ", $Array_Test.Count -Color Cyan, Green

$Array_Test_Iterator = 0
do {
	Write-Color "Current iterator: ", $Array_Test_Iterator -Color Cyan, Yellow
	Write-Color "Associated word: ", $Array_Test[$Array_Test_Iterator] -Color Cyan, Gray
	$Array_Test_Iterator++
} while (
	$Array_Test_Iterator -lt $Array_Test.Count
)