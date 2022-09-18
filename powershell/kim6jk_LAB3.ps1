$IP = (Get-NetIPAddress).IPv4Address | Select-String "192*"
$user = $env:USERNAME
$hostname = $env:COMPUTERNAME
$version = $Host.Version.Major
$date = Get-Date -Format "dddd, MM dd yyyy"

$body = "This machine's IP is {0}. User is {1}. Hostname is {2}. PowerShell Version {3}. Today's Date is {4}." -f $IP, $user, $hostname, $version, $date

$body | Out-File -Append C:\Users\Administrator\Desktop\sysinfo.txt