$breakchar = ","#[char]9
$bounds = 100000
$counter = 1
$counterb = 1
$createHeader = $true
$removeOld = $true
$path = "$PSScriptRoot\data.csv"

$osTypes = @("Linux","MacOS","Windows")
$zoneTypes = @("Entwicklung", "Test", "Produktion")
$programs = @("MongoDB", "OracleDB", "PostgreSQL", "Cassandra", "Jira", "Confluence", "Notes", "GitLab", "WebSphere", "Wekan", "NodeJS", "Apache", "TFS", "Proxy", "Loadbalancer", "MSSQL", "SharePoint", "Exchange")

if([System.IO.File]::Exists($path) -and $removeOld){
    Remove-Item -Path $path -Force
}

if($createHeader) {
    $firstline = ("UUID"+$breakchar+"Servername"+$breakchar+"OS"+$breakchar+"Zone"+$breakchar+"Anwendung")

    Add-Content -path $path -value $firstline
}

1..$bounds | % {
    $lines = @()

    1..2000 | % {
    $status = "Gen Line {0} of {1}" -f $counter,(2000)
    Write-Progress -Activity "Generating Testdata for Block $counterb of $bounds" $status -PercentComplete (($counterb / $bounds)*100)

    $uuid = [Guid]::newGuid()
    $zone = Get-Random -Maximum 3
    $os = Get-Random -Maximum 3
    $app = Get-Random -Maximum 18
    $name = "m999" + -join ((97..122) | Get-Random -Count 5 | %{[char]$_}) + (Get-Random -Maximum 999 -Minimum 1).ToString("000")
    switch ($zone) {
     0 { $name += "d" }
     1 { $name += "t" }
     2 { $name += "p" }
    }

    $line = ($uuid.ToString()+$breakchar+$name+$breakchar+$osTypes[$os]+$breakchar+$zoneTypes[$zone]+$breakchar+$programs[$app])

    $lines += $line
    $counter++
    }

    Add-Content -path $path -value $lines
    $counterb++
    $counter = 1
}

Write-Progress -Activity "Generating Testdata for Block $counterb of $bounds" -Status "Completed" -Completed
Write-Host "Press any key to exit..."
$Host.UI.ReadLine()
exit