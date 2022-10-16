Write-Host "This is a default toast notification (bottom right of screen). Hit enter after it disappears, or you dismiss it."
New-BurntToastNotification
pause
Write-Host "This is a notification with custom texts. Hit enter again to go on."
New-BurntToastNotification -Text "This is the title", "This is the description"
pause
Write-Host "This notification functions as an alarm. Hit enter to end the script."
New-BurntToastNotification -Text 'Alarm' -Sound 'Alarm2' -SnoozeAndDismiss
pause