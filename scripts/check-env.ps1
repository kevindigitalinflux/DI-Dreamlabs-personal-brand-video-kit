# Read-only environment check. Prints versions. Installs nothing.
foreach ($c in 'node','git','ffmpeg','ffprobe','python','claude','codex') {
  $cmd = Get-Command $c -ErrorAction SilentlyContinue
  if ($cmd) {
    $v = (& $c --version 2>&1 | Select-Object -First 1)
    Write-Output "OK      $c  $v"
  } else {
    Write-Output "MISSING $c"
  }
}
