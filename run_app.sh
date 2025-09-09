#!/bin/bash

echo "Starting English Alphabet Learning Platform..."
echo "بدء منصة تعلم الأبجدية الإنجليزية..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed"
    echo "Python3 غير مثبت"
    echo "Please install Python3 from your package manager"
    exit 1
fi

# Check if required packages are installed
python3 -c "import pygame, pyttsx3" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing required packages..."
    echo "تثبيت المكتبات المطلوبة..."
    pip3 install pygame pyttsx3
    if [ $? -ne 0 ]; then
        echo "Failed to install packages"
        echo "فشل في تثبيت المكتبات"
        exit 1
    fi
fi

# Run the application
echo "Starting application..."
echo "بدء التطبيق..."
python3 english_alphabet_learning_platform.py
