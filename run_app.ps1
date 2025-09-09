# English Alphabet Learning Platform - PowerShell Launcher
# منصة تعلم الأبجدية الإنجليزية - مشغل PowerShell

Write-Host "Starting English Alphabet Learning Platform..." -ForegroundColor Green
Write-Host "بدء منصة تعلم الأبجدية الإنجليزية..." -ForegroundColor Green

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found Python: $pythonVersion" -ForegroundColor Yellow
} catch {
    Write-Host "Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Python غير مثبت أو غير موجود في PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if required packages are installed
try {
    python -c "import pygame, pyttsx3" 2>$null
    Write-Host "Required packages are installed" -ForegroundColor Green
} catch {
    Write-Host "Installing required packages..." -ForegroundColor Yellow
    Write-Host "تثبيت المكتبات المطلوبة..." -ForegroundColor Yellow
    
    try {
        pip install pygame pyttsx3
        Write-Host "Packages installed successfully" -ForegroundColor Green
    } catch {
        Write-Host "Failed to install packages" -ForegroundColor Red
        Write-Host "فشل في تثبيت المكتبات" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# Run the application
Write-Host "Starting application..." -ForegroundColor Green
Write-Host "بدء التطبيق..." -ForegroundColor Green

try {
    python english_alphabet_learning_platform.py
} catch {
    Write-Host "Error running application: $_" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
