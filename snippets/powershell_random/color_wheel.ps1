function Get-Padding {
	[CmdletBinding()]
	param (
		#   Max length
		[Parameter(Position=0, Mandatory=$true)]
		[int]$MaxLength,

		#   Word to pad
		[Parameter(Position=1, Mandatory=$true)]
		[string]$Word
	)
	
	begin {
		[int]$Gap = $MaxLength - $Word.Length
	}
	
	process {
		[int]$Padding_Left = [Math]::Floor($Gap / 2)
		[int]$Padding_Right = [Math]::Ceiling(($Gap / 2))
	}
	
	end {
		return @{
			PaddingLeft	 = $Padding_Left;
			PaddingRight	= $Padding_Right
		}
	}
}

#region Declarations
	$Padding_Padder = 1
	$Colors_List = New-Object System.Collections.ArrayList
	$Colors_List_With_Padding = New-Object System.Collections.ArrayList
#endregion Declarations

#region GenerateValues
	[System.Enum]::GetValues([System.ConsoleColor]) | ForEach-Object {$Colors_List.Add([string]$_) | Out-Null}
	$Longest_Color_Name = ($Colors_List | Measure-Object -Maximum -Property Length).Maximum
	foreach ($Color in $Colors_List) {
		$Padding = Get-Padding -MaxLength $Longest_Color_Name -Word $Color
		$Obj = New-Object PSObject
		Add-Member -InputObject $Obj -MemberType NoteProperty -Name Color -Value $Color
		Add-Member -InputObject $Obj -MemberType NoteProperty -Name PaddingLeft -Value $Padding.PaddingLeft
		Add-Member -InputObject $Obj -MemberType NoteProperty -Name PaddingRight -Value $Padding.PaddingRight
		$Colors_List_With_Padding.Add($Obj) | Out-Null
	}
	$BlackCell = @{
		Object = (" " * ($Longest_Color_Name + ($Padding_Padder * 2)));
		ForegroundColor = 'Black';
		BackgroundColor = 'Black'
	}
#endregion GenerateValues

#region WriteColorTable
	#region TableHeader
		#region StubHead
			$StubHead_Text_Left = "BG↓"
			$StubHead_Text_Right = "FG→"
			$StubHead_Padding = Get-Padding -MaxLength $Longest_Color_Name -Word ($StubHead_Text_Left + $StubHead_Text_Right)
			$StubHead_Text = "{0}{1}{2}" -f ("BG↓", (" " * ($StubHead_Padding.PaddingLeft + $StubHead_Padding.PaddingRight + ($Padding_Padder * 2))), "FG→")
			$StubHead_Splat = @{
				Object = $StubHead_Text;
				ForegroundColor = 'DarkBlue';
				BackgroundColor = 'DarkGray';
			}
			Write-Host @StubHead_Splat -NoNewline
		#endregion StubHead
		#region ColumnLabel
			$i_header = $Colors_List_With_Padding.Count
			foreach ($Color in $Colors_List_With_Padding) {
				$Header_Text = "{0}{1}{2}" -f (" " * ($Color.PaddingLeft + $Padding_Padder)), $Color.Color, (" " * ($Color.PaddingRight + $Padding_Padder))
				$Header_Splat = @{
					Object = $Header_Text;
					ForegroundColor = 'DarkBlue';
					BackgroundColor = 'DarkGray';
				}
				if($i_header -gt 1) {
					$Header_Splat.Add('NoNewline', $true) | Out-Null
				}
				Write-Host @Header_Splat
				$i_header--
			}
		#endregion ColumnLabel
	#endregion TableHeader
	#region TableBody
		foreach ($Color_Row in $Colors_List_With_Padding) {
			#region RowLabel
				$Row_Stub_Text = "{0}{1}{2}" -f (" " * ($Color_Row.PaddingLeft + $Padding_Padder)), $Color_Row.Color, (" " * ($Color_Row.PaddingRight + $Padding_Padder))
				$Row_Stub_Splat = [ordered]@{
					Object = $Row_Stub_Text;
					ForegroundColor = 'DarkBlue';
					BackgroundColor = 'DarkGray';
					NoNewline = $true
				}
				Write-Host @Row_Stub_Splat
			#endregion RowLabel
			#region Cells
				$i_columns = $Colors_List_With_Padding.Count
				foreach ($Color_Column in $Colors_List_With_Padding) {
					$Column_Text = "{0}{1}{2}" -f (" " * ($Color_Column.PaddingLeft + $Padding_Padder)), $Color_Column.Color, (" " * ($Color_Column.PaddingRight + $Padding_Padder))
					if ($Color_Row.Color -eq $Color_Column.Color) {
						$Splat_Column = $BlackCell.Clone()
					}
					else {
						$Splat_Column = [ordered]@{
							Object = $Column_Text;
							ForegroundColor = $Color_Column.Color;
							BackgroundColor = $Color_Row.Color;
						}
					}
					if ($i_columns -gt 1) {
						$Splat_Column.Add('NoNewline', $true) | Out-Null
					}
					Write-Host @Splat_Column
					$i_columns--
				}
			#endregion Cells
		}
	#endregion TableBody
#endregion WriteColorTable