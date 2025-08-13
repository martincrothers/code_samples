$Username = "domain\user"
$Password_Old = "oldP@ssw0rd" | ConvertTo-SecureString -AsPlainText -Force
$Password_New = "newP@ssw0rd" | ConvertTo-SecureString -AsPlainText -Force

$Cred_Old = [System.Management.Automation.PSCredential]::New($Username,$Password_Old)
$Cred_New = [System.Management.Automation.PSCredential]::New($Username,$Password_New)

Set-ADAccountPassword -Identity ($Cred_Old.GetNetworkCredential().UserName) -OldPassword $Cred_Old.Password -NewPassword $Cred_New.Password
