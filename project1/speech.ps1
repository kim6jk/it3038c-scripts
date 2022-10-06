Add-Type -AssemblyName System.speech
$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer

Write-Host "Welcome to my Speech Synthesizer script!"
pause
clear-host

write-host "1. Microsoft David"
write-host "2. Microsoft Zira"
$voiceNumber = read-host -prompt 'Enter 1 or 2 depending on which voice you would like to use'
clear-host

$record = Read-Host -prompt 'Would you like to record the message and create a .wav file on your desktop? (y/n)'
clear-host

if($voiceNumber -eq 2){	$speak.SelectVoice('Microsoft Zira Desktop') }
if($voiceNumber -eq "y") {$speak.SetOutputToWaveFile("$env:UserProfile\Desktop\speak.wav")}

$message = Read-Host -prompt 'What would you like to say?'
$speak.Speak($message)
$speak.Dispose()





