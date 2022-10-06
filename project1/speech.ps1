Add-Type -AssemblyName System.speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer

Write-Host "Welcome to my Speech Synthesizer script!"
pause
clear-host

write-host "1. Microsoft David"
write-host "2. Microsoft Zira"
$voiceNumber = read-host -prompt 'Enter 1 or 2 depending on which voice you would like to use'
clear-host

$record = Read-Host -prompt 'Would you like to record the message and create a .wav file on your desktop? (y/n)'
clear-host

if($voiceNumber -eq 2){	$synth.SelectVoice('Microsoft Zira Desktop') }
if($record -eq "y") {$synth.SetOutputToWaveFile("$env:UserProfile\Desktop\speak.wav")}

$message = Read-Host -prompt 'What would you like to say?'
$synth.Speak($message)
$synth.Dispose()





