
@echo off
set BAT_DIR=%~dp0
set EXE_PATH=%BAT_DIR%output\dist\desktop_icon_backup.exe
set SHORTCUT_NAME="Desktop Icon Backup"
set DESKTOP_PATH=%USERPROFILE%\Desktop
set SHORTCUT_PATH=%DESKTOP_PATH%\\%SHORTCUT_NAME%.lnk

:: Step 1: Run PyInstaller to generate the executable
echo Running PyInstaller...
pyinstaller --onefile --windowed --icon=monitor.ico --distpath=output\dist --workpath=output\build desktop_icon_backup.py

:: Check if PyInstaller succeeded (check if .exe exists)
if exist "%EXE_PATH%" (
    echo PyInstaller completed successfully.
    
    :: Step 2: Create the shortcut using PowerShell
    echo Creating shortcut...
    powershell "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT_PATH%'); $Shortcut.TargetPath = '%EXE_PATH%'; $Shortcut.WorkingDirectory = [System.IO.Path]::GetDirectoryName('%EXE_PATH%'); $Shortcut.Save()"
    echo Shortcut created at: %SHORTCUT_PATH%
) else (
    echo Error: PyInstaller failed to create the executable.
)
pause



pyinstaller --onefile --windowed --icon=monitor.ico --distpath=output/dist --workpath=output/build desktop_icon_backup.py


