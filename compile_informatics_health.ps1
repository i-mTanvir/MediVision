param(
    [string]$TexFile = "informatics_health_template.tex"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $TexFile)) {
    throw "TeX file not found: $TexFile"
}

$texName = [System.IO.Path]::GetFileNameWithoutExtension($TexFile)
$texDir = Split-Path -Parent (Resolve-Path -LiteralPath $TexFile)
Push-Location $texDir
try {
    $pdflatex = (Get-Command pdflatex -ErrorAction Stop).Source
    $bibtex = (Get-Command bibtex -ErrorAction Stop).Source

    & $pdflatex -interaction=nonstopmode -halt-on-error $TexFile
    if ($LASTEXITCODE -ne 0) { throw "First pdflatex pass failed." }

    & $bibtex $texName
    if ($LASTEXITCODE -ne 0) { throw "BibTeX pass failed." }

    & $pdflatex -interaction=nonstopmode -halt-on-error $TexFile
    if ($LASTEXITCODE -ne 0) { throw "Second pdflatex pass failed." }

    & $pdflatex -interaction=nonstopmode -halt-on-error $TexFile
    if ($LASTEXITCODE -ne 0) { throw "Final pdflatex pass failed." }

    Write-Host "Compiled successfully: $texName.pdf" -ForegroundColor Green
}
finally {
    Pop-Location
}
