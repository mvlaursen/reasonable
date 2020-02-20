Start-Process -FilePath "C:\Program Files\Mozilla Firefox\firefox.exe" -ArgumentList "-devtools -new-window https://reason.com/latest/"
read-host "When screen scraping is done, press ENTER to continue..."
Python reasonable.py c:\Users\money\Downloads\reason-latest.csv c:\Users\money\AppData\Local\Temp\reason-latest.html