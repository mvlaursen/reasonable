Write-Output "Removing previous .csv file..."
Remove-Item -path c:\Users\money\Downloads\reason-latest.csv
Write-Output "Launching Firefox..."
Start-Process -FilePath "C:\Program Files\Mozilla Firefox\firefox.exe" -ArgumentList "-devtools -new-window https://reason.com/latest/"
Read-Host "When screen scraping is done, press ENTER to continue..."
Write-Output "Launching reasonable.py..."
Python reasonable.py c:\Users\money\Downloads\reason-latest.csv c:\Users\money\AppData\Local\Temp\reason-latest.html
Write-Ouptut "Done"