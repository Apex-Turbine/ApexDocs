param(
    [ValidateSet("all", "site", "DS", "DX", "GageMap", "DX+", "Custom Development", "deployment")]
    [string]$Target = "all",
    [ValidateSet("html", "pdf", "both")]
    [string]$Format = "both",
    [string]$Output = "dist",
    [switch]$Strict,
    [switch]$Clean
)

$ErrorActionPreference = "Stop"

$pyCmd = $null
if (Get-Command "py" -ErrorAction SilentlyContinue) {
    $pyCmd = @("py", "-3.13")
} elseif (Get-Command "python" -ErrorAction SilentlyContinue) {
    $pyCmd = @("python")
} else {
    throw "Python 3.11+ was not found on PATH."
}

$argsList = @("build_docs.py", "--target", $Target, "--format", $Format, "--output", $Output)
if ($Strict) { $argsList += "--strict" }
if ($Clean)  { $argsList += "--clean" }

if ($pyCmd.Length -gt 1) {
    & $pyCmd[0] $pyCmd[1] @argsList
} else {
    & $pyCmd[0] @argsList
}
exit $LASTEXITCODE
