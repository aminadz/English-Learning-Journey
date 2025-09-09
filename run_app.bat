@echo off
echo Starting English Alphabet Learning Platform...
echo بدء منصة تعلم الأبجدية الإنجليزية...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH
    echo Python غير مثبت أو غير موجود في PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if required packages are installed
python -c "import pygame, pyttsx3" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing required packages...
    echo تثبيت المكتبات المطلوبة...
    pip install pygame pyttsx3
    if %errorlevel% neq 0 (
        echo Failed to install packages
        echo فشل في تثبيت المكتبات
        pause
        exit /b 1
    )
)

REM Run the application
echo Starting application...
echo بدء التطبيق...
python english_alphabet_learning_platform.py

pause
