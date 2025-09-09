#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
English Alphabet Learning Platform - Python Version
منصة تعلم الأبجدية الإنجليزية - إصدار Python

A comprehensive learning platform for teaching English alphabet to children (11 stages)
منصة تعليمية شاملة لتعليم الأبجدية الإنجليزية للأطفال (11 مرحلة)
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
import random
import time
from datetime import datetime
import threading
import pygame
from typing import Dict, List, Optional, Tuple

# Initialize pygame for sound
pygame.mixer.init()

class EnglishAlphabetPlatform:
    """Main class for the English Alphabet Learning Platform"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("English Alphabet Learning Platform - منصة تعلم الأبجدية الإنجليزية")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f8ff')
        
        # Data structures
        self.letters = {
            'A': {'word': 'Apple', 'phonetic': '/ˈæpəl/', 'arabic': 'تفاحة', 'emoji': '🍎'},
            'B': {'word': 'Ball', 'phonetic': '/bɔːl/', 'arabic': 'كرة', 'emoji': '⚽'},
            'C': {'word': 'Cat', 'phonetic': '/kæt/', 'arabic': 'قطة', 'emoji': '🐱'},
            'D': {'word': 'Dog', 'phonetic': '/dɔːɡ/', 'arabic': 'كلب', 'emoji': '🐶'},
            'E': {'word': 'Elephant', 'phonetic': '/ˈeləfənt/', 'arabic': 'فيل', 'emoji': '🐘'},
            'F': {'word': 'Fish', 'phonetic': '/fɪʃ/', 'arabic': 'سمكة', 'emoji': '🐟'},
            'G': {'word': 'Guitar', 'phonetic': '/ɡɪˈtɑːr/', 'arabic': 'جيتار', 'emoji': '🎸'},
            'H': {'word': 'House', 'phonetic': '/haʊs/', 'arabic': 'منزل', 'emoji': '🏠'},
            'I': {'word': 'Ice', 'phonetic': '/aɪs/', 'arabic': 'ثلج', 'emoji': '🧊'},
            'J': {'word': 'Juice', 'phonetic': '/dʒuːs/', 'arabic': 'عصير', 'emoji': '🧃'},
            'K': {'word': 'Kite', 'phonetic': '/kaɪt/', 'arabic': 'طائرة ورقية', 'emoji': '🪁'},
            'L': {'word': 'Lion', 'phonetic': '/ˈlaɪən/', 'arabic': 'أسد', 'emoji': '🦁'},
            'M': {'word': 'Moon', 'phonetic': '/muːn/', 'arabic': 'قمر', 'emoji': '🌙'},
            'N': {'word': 'Nose', 'phonetic': '/noʊz/', 'arabic': 'أنف', 'emoji': '👃'},
            'O': {'word': 'Orange', 'phonetic': '/ˈɔːrɪndʒ/', 'arabic': 'برتقال', 'emoji': '🍊'},
            'P': {'word': 'Pizza', 'phonetic': '/ˈpiːtsə/', 'arabic': 'بيتزا', 'emoji': '🍕'},
            'Q': {'word': 'Queen', 'phonetic': '/kwiːn/', 'arabic': 'ملكة', 'emoji': '👑'},
            'R': {'word': 'Rainbow', 'phonetic': '/ˈreɪnboʊ/', 'arabic': 'قوس قزح', 'emoji': '🌈'},
            'S': {'word': 'Sun', 'phonetic': '/sʌn/', 'arabic': 'شمس', 'emoji': '☀️'},
            'T': {'word': 'Tree', 'phonetic': '/triː/', 'arabic': 'شجرة', 'emoji': '🌳'},
            'U': {'word': 'Umbrella', 'phonetic': '/ʌmˈbrelə/', 'arabic': 'مظلة', 'emoji': '☂️'},
            'V': {'word': 'Violin', 'phonetic': '/ˌvaɪəˈlɪn/', 'arabic': 'كمان', 'emoji': '🎻'},
            'W': {'word': 'Water', 'phonetic': '/ˈwɔːtər/', 'arabic': 'ماء', 'emoji': '💧'},
            'X': {'word': 'Xylophone', 'phonetic': '/ˈzaɪləfoʊn/', 'arabic': 'إكسيليفون', 'emoji': '🎵'},
            'Y': {'word': 'Yellow', 'phonetic': '/ˈjeloʊ/', 'arabic': 'أصفر', 'emoji': '🟡'},
            'Z': {'word': 'Zebra', 'phonetic': '/ˈziːbrə/', 'arabic': 'حمار وحشي', 'emoji': '🦓'}
        }
        
        # Learning stages
        self.stages = [
            {"id": 1, "name": "Letter Recognition", "description": "Learn to recognize letters", "emoji": "🔤"},
            {"id": 2, "name": "Phonics", "description": "Learn letter sounds", "emoji": "🔊"},
            {"id": 3, "name": "Words", "description": "Learn words starting with each letter", "emoji": "📝"},
            {"id": 4, "name": "Colors", "description": "Learn colors and shapes", "emoji": "🎨"},
            {"id": 5, "name": "Sentences", "description": "Form simple sentences", "emoji": "📄"},
            {"id": 6, "name": "Stories", "description": "Read short stories", "emoji": "📚"},
            {"id": 7, "name": "Listening", "description": "Improve listening skills", "emoji": "👂"},
            {"id": 8, "name": "Grammar", "description": "Learn basic grammar", "emoji": "📖"},
            {"id": 9, "name": "Reading", "description": "Practice reading", "emoji": "👁️"},
            {"id": 10, "name": "Writing", "description": "Practice writing letters", "emoji": "✍️"},
            {"id": 11, "name": "Conversation", "description": "Practice speaking", "emoji": "💬"},
            {"id": 12, "name": "Assessment", "description": "Test your knowledge", "emoji": "📊"}
        ]
        
        # Colors data
        self.colors = {
            "Primary Colors": [
                {"english": "Red", "arabic": "أحمر", "emoji": "🔴", "hex": "#FF0000"},
                {"english": "Blue", "arabic": "أزرق", "emoji": "🔵", "hex": "#0000FF"},
                {"english": "Yellow", "arabic": "أصفر", "emoji": "🟡", "hex": "#FFFF00"},
                {"english": "Green", "arabic": "أخضر", "emoji": "🟢", "hex": "#008000"}
            ],
            "Secondary Colors": [
                {"english": "Orange", "arabic": "برتقالي", "emoji": "🟠", "hex": "#FFA500"},
                {"english": "Purple", "arabic": "بنفسجي", "emoji": "🟣", "hex": "#800080"},
                {"english": "Pink", "arabic": "وردي", "emoji": "🩷", "hex": "#FFC0CB"},
                {"english": "Cyan", "arabic": "سماوي", "emoji": "🔵", "hex": "#00FFFF"}
            ],
            "Neutral Colors": [
                {"english": "Black", "arabic": "أسود", "emoji": "⚫", "hex": "#000000"},
                {"english": "White", "arabic": "أبيض", "emoji": "⚪", "hex": "#FFFFFF"},
                {"english": "Gray", "arabic": "رمادي", "emoji": "⚫", "hex": "#808080"},
                {"english": "Brown", "arabic": "بني", "emoji": "🟤", "hex": "#8B4513"}
            ]
        }
        
        # User progress
        self.progress = {
            'current_stage': 1,
            'unlocked_stages': [1],
            'points': 0,
            'badges': [],
            'letters_learned': [],
            'words_learned': [],
            'games_played': 0,
            'total_time': 0,
            'preferences': {
                'sound_enabled': True,
                'arabic_transliteration': True,
                'high_contrast': False
            }
        }
        
        # Current state
        self.current_letter_index = 0
        self.letter_list = list(self.letters.keys())
        self.is_playing = False
        
        # Load progress
        self.load_progress()
        
        # Test voices on startup
        self.test_voices_on_startup()
        
        # Create GUI
        self.create_gui()
        
    def create_gui(self):
        """Create the main GUI interface"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Sidebar for stages
        self.create_sidebar(main_frame)
        
        # Main content area
        self.create_main_content(main_frame)
        
        # Status bar
        self.create_status_bar(main_frame)
        
    def create_sidebar(self, parent):
        """Create the sidebar with stage buttons"""
        sidebar = ttk.Frame(parent, width=250)
        sidebar.grid(row=0, column=0, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        sidebar.grid_propagate(False)
        
        # Title
        title_label = ttk.Label(sidebar, text="Learning Journey\nرحلة التعلم", 
                              font=('Arial', 14, 'bold'), anchor='center')
        title_label.pack(pady=10)
        
        # Progress info
        progress_frame = ttk.LabelFrame(sidebar, text="Progress - التقدم")
        progress_frame.pack(fill='x', pady=5)
        
        self.points_label = ttk.Label(progress_frame, text=f"Points: {self.progress['points']}")
        self.points_label.pack(anchor='w')
        
        self.badges_label = ttk.Label(progress_frame, text=f"Badges: {len(self.progress['badges'])}")
        self.badges_label.pack(anchor='w')
        
        # Stage buttons
        stages_frame = ttk.LabelFrame(sidebar, text="Stages - المراحل")
        stages_frame.pack(fill='both', expand=True, pady=5)
        
        self.stage_buttons = []
        for stage in self.stages:
            btn = ttk.Button(stages_frame, text=f"{stage['emoji']} {stage['name']}\n{stage['description']}",
                           command=lambda s=stage: self.select_stage(s['id']),
                           state='normal' if stage['id'] in self.progress['unlocked_stages'] else 'disabled')
            btn.pack(fill='x', pady=2)
            self.stage_buttons.append(btn)
            
        # Settings
        settings_frame = ttk.LabelFrame(sidebar, text="Settings - الإعدادات")
        settings_frame.pack(fill='x', pady=5)
        
        self.sound_var = tk.BooleanVar(value=self.progress['preferences']['sound_enabled'])
        ttk.Checkbutton(settings_frame, text="Sound Effects", variable=self.sound_var,
                       command=self.toggle_sound).pack(anchor='w')
        
        self.arabic_var = tk.BooleanVar(value=self.progress['preferences']['arabic_transliteration'])
        ttk.Checkbutton(settings_frame, text="Arabic Transliteration", variable=self.arabic_var,
                       command=self.toggle_arabic).pack(anchor='w')
        
        # Test voices button
        ttk.Button(settings_frame, text="🔊 Test Voices", command=self.test_voices).pack(anchor='w', pady=5)
        
    def create_main_content(self, parent):
        """Create the main content area"""
        content_frame = ttk.Frame(parent)
        content_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10)
        
        # Header
        header_frame = ttk.Frame(content_frame)
        header_frame.pack(fill='x', pady=(0, 10))
        
        self.stage_title = ttk.Label(header_frame, text="Letter Recognition - تعرف على الحروف", 
                                   font=('Arial', 16, 'bold'))
        self.stage_title.pack(side='left')
        
        # Main game area
        self.game_frame = ttk.Frame(content_frame, relief='sunken', borderwidth=2)
        self.game_frame.pack(fill='both', expand=True)
        
        # Render current stage
        self.render_current_stage()
        
    def create_status_bar(self, parent):
        """Create the status bar"""
        status_frame = ttk.Frame(parent)
        status_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=10, pady=5)
        
        self.status_label = ttk.Label(status_frame, text="Ready to learn! - جاهز للتعلم!")
        self.status_label.pack(side='left')
        
        # Time spent
        self.time_label = ttk.Label(status_frame, text="Time: 00:00")
        self.time_label.pack(side='right')
        
    def render_current_stage(self):
        """Render the current learning stage"""
        # Clear existing content
        for widget in self.game_frame.winfo_children():
            widget.destroy()
            
        stage_id = self.progress['current_stage']
        
        if stage_id == 1:
            self.render_letter_recognition()
        elif stage_id == 2:
            self.render_phonics()
        elif stage_id == 3:
            self.render_words()
        elif stage_id == 4:
            self.render_colors()
        else:
            self.render_placeholder_stage(stage_id)
            
    def render_letter_recognition(self):
        """Render the letter recognition stage"""
        # Current letter display
        letter_frame = ttk.Frame(self.game_frame)
        letter_frame.pack(expand=True)
        
        current_letter = self.letter_list[self.current_letter_index]
        letter_data = self.letters[current_letter]
        
        # Large letter display
        letter_label = ttk.Label(letter_frame, text=current_letter, font=('Arial', 120, 'bold'))
        letter_label.pack(pady=20)
        
        # Letter info
        info_frame = ttk.Frame(letter_frame)
        info_frame.pack(pady=10)
        
        word_label = ttk.Label(info_frame, text=f"Word: {letter_data['word']}", font=('Arial', 24))
        word_label.pack()
        
        phonetic_label = ttk.Label(info_frame, text=f"Sound: {letter_data['phonetic']}", font=('Arial', 18))
        phonetic_label.pack()
        
        if self.arabic_var.get():
            arabic_label = ttk.Label(info_frame, text=f"Arabic: {letter_data['arabic']}", font=('Arial', 18))
            arabic_label.pack()
        
        emoji_label = ttk.Label(info_frame, text=letter_data['emoji'], font=('Arial', 48))
        emoji_label.pack()
        
        # Control buttons
        control_frame = ttk.Frame(letter_frame)
        control_frame.pack(pady=20)
        
        ttk.Button(control_frame, text="🔊 Pronounce", command=self.pronounce_current_letter).pack(side='left', padx=5)
        ttk.Button(control_frame, text="⬅️ Previous", command=self.previous_letter).pack(side='left', padx=5)
        ttk.Button(control_frame, text="Next ➡️", command=self.next_letter).pack(side='left', padx=5)
        ttk.Button(control_frame, text="🎯 Practice", command=self.practice_letter).pack(side='left', padx=5)
        
    def render_phonics(self):
        """Render the phonics stage"""
        content_frame = ttk.Frame(self.game_frame)
        content_frame.pack(expand=True, fill='both')
        
        ttk.Label(content_frame, text="🔊 Phonics Stage - مرحلة الأصوات", 
                 font=('Arial', 20, 'bold')).pack(pady=20)
        
        # Phonics grid
        grid_frame = ttk.Frame(content_frame)
        grid_frame.pack(expand=True, fill='both', padx=20)
        
        row, col = 0, 0
        for letter in self.letter_list:
            letter_data = self.letters[letter]
            btn = ttk.Button(grid_frame, text=f"{letter}\n{letter_data['phonetic']}", 
                           command=lambda l=letter: self.pronounce_letter(l),
                           width=8)
            btn.grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col >= 6:
                col = 0
                row += 1
                
    def render_words(self):
        """Render the words stage"""
        content_frame = ttk.Frame(self.game_frame)
        content_frame.pack(expand=True, fill='both')
        
        ttk.Label(content_frame, text="📝 Words Stage - مرحلة الكلمات", 
                 font=('Arial', 20, 'bold')).pack(pady=20)
        
        # Words grid
        grid_frame = ttk.Frame(content_frame)
        grid_frame.pack(expand=True, fill='both', padx=20)
        
        row, col = 0, 0
        for letter in self.letter_list:
            letter_data = self.letters[letter]
            word_frame = ttk.Frame(grid_frame, relief='solid', borderwidth=1)
            word_frame.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            
            ttk.Label(word_frame, text=letter, font=('Arial', 24, 'bold')).pack()
            ttk.Label(word_frame, text=letter_data['word'], font=('Arial', 16)).pack()
            
            # Show Arabic translation if enabled
            if self.arabic_var.get():
                ttk.Label(word_frame, text=letter_data['arabic'], font=('Arial', 14), 
                         foreground='blue').pack()
            
            ttk.Label(word_frame, text=letter_data['emoji'], font=('Arial', 32)).pack()
            
            # Pronunciation button
            ttk.Button(word_frame, text="🔊", command=lambda l=letter: self.pronounce_letter(l)).pack(pady=5)
            
            col += 1
            if col >= 4:
                col = 0
                row += 1
                
    def render_colors(self):
        """Render the colors stage"""
        content_frame = ttk.Frame(self.game_frame)
        content_frame.pack(expand=True, fill='both')
        
        ttk.Label(content_frame, text="🎨 Colors & Shapes - الألوان والأشكال", 
                 font=('Arial', 20, 'bold')).pack(pady=20)
        
        # Colors grid
        for category, colors in self.colors.items():
            category_frame = ttk.LabelFrame(content_frame, text=category)
            category_frame.pack(fill='x', padx=20, pady=10)
            
            grid_frame = ttk.Frame(category_frame)
            grid_frame.pack(fill='x', padx=10, pady=10)
            
            row, col = 0, 0
            for color in colors:
                color_frame = ttk.Frame(grid_frame, relief='solid', borderwidth=1)
                color_frame.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
                
                # Color display
                color_display = ttk.Frame(color_frame)
                color_display.pack(fill='x', pady=5)
                color_display.configure(background=color['hex'])
                
                # Color info
                ttk.Label(color_frame, text=color['english'], font=('Arial', 16, 'bold')).pack()
                ttk.Label(color_frame, text=color['arabic'], font=('Arial', 14), 
                         foreground='blue').pack()
                ttk.Label(color_frame, text=color['emoji'], font=('Arial', 24)).pack()
                ttk.Label(color_frame, text=color['hex'], font=('Arial', 10), 
                         foreground='gray').pack()
                
                # Pronunciation button
                ttk.Button(color_frame, text="🔊", 
                          command=lambda c=color: self.pronounce_color(c)).pack(pady=5)
                
                col += 1
                if col >= 4:
                    col = 0
                    row += 1
            
    def render_placeholder_stage(self, stage_id):
        """Render a placeholder for unimplemented stages"""
        content_frame = ttk.Frame(self.game_frame)
        content_frame.pack(expand=True, fill='both')
        
        stage = next((s for s in self.stages if s['id'] == stage_id), None)
        if stage:
            ttk.Label(content_frame, text=f"{stage['emoji']} {stage['name']}", 
                     font=('Arial', 20, 'bold')).pack(pady=50)
            ttk.Label(content_frame, text=f"Coming Soon! - قريباً!", 
                     font=('Arial', 16)).pack()
            ttk.Label(content_frame, text=f"{stage['description']}", 
                     font=('Arial', 14)).pack(pady=10)
                     
    def select_stage(self, stage_id):
        """Select a learning stage"""
        if stage_id in self.progress['unlocked_stages']:
            self.progress['current_stage'] = stage_id
            self.render_current_stage()
            self.update_ui()
        else:
            messagebox.showinfo("Locked Stage", "This stage is locked. Complete previous stages to unlock it.")
            
    def pronounce_current_letter(self):
        """Pronounce the current letter"""
        current_letter = self.letter_list[self.current_letter_index]
        self.pronounce_letter(current_letter)
        
    def pronounce_letter(self, letter):
        """Pronounce a specific letter with Arabic support"""
        if letter in self.letters:
            letter_data = self.letters[letter]
            word = letter_data['word']
            arabic = letter_data['arabic']
            
            # Simple pronunciation using system TTS
            try:
                import pyttsx3
                engine = pyttsx3.init()
                
                # Get available voices
                voices = engine.getProperty('voices')
                
                # Try to find Arabic voice
                arabic_voice = None
                for voice in voices:
                    if 'arabic' in voice.name.lower() or 'ar' in voice.id.lower():
                        arabic_voice = voice
                        break
                
                # Set voice and properties
                if arabic_voice:
                    engine.setProperty('voice', arabic_voice.id)
                    engine.setProperty('rate', 120)  # Slower for Arabic
                    engine.setProperty('volume', 0.9)
                else:
                engine.setProperty('rate', 150)
                    engine.setProperty('volume', 1.0)
                
                # Pronounce English text
                engine.say(f"{letter} for {word}")
                engine.runAndWait()
                
                # Pronounce Arabic text if enabled
                if self.arabic_var.get() and arabic_voice:
                    engine.say(arabic)
                    engine.runAndWait()
                    
            except ImportError:
                # Fallback to simple message
                messagebox.showinfo("Pronunciation", f"{letter} for {word}\nArabic: {arabic}")
            except Exception as e:
                # Handle any other TTS errors
                print(f"TTS Error: {e}")
                messagebox.showwarning("Pronunciation Error", f"Could not pronounce {letter}. Please check your audio system.")
                
    def pronounce_arabic_word(self, letter):
        """Pronounce Arabic word for a specific letter"""
        if letter in self.letters:
            letter_data = self.letters[letter]
            arabic = letter_data['arabic']
            
            try:
                import pyttsx3
                engine = pyttsx3.init()
                
                # Get available voices
                voices = engine.getProperty('voices')
                
                # Try to find Arabic voice
                arabic_voice = None
                for voice in voices:
                    if 'arabic' in voice.name.lower() or 'ar' in voice.id.lower():
                        arabic_voice = voice
                        break
                
                if arabic_voice:
                    engine.setProperty('voice', arabic_voice.id)
                    engine.setProperty('rate', 120)
                    engine.setProperty('volume', 0.9)
                    engine.say(arabic)
                    engine.runAndWait()
                else:
                    messagebox.showwarning("Arabic Voice", "No Arabic voice found. Please install Arabic language pack.")
                    
            except ImportError:
                messagebox.showinfo("Arabic Pronunciation", f"Arabic: {arabic}")
            except Exception as e:
                print(f"Arabic TTS Error: {e}")
                messagebox.showwarning("Arabic Pronunciation Error", f"Could not pronounce Arabic word. Error: {e}")
                
    def pronounce_color(self, color):
        """Pronounce a color name"""
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say(f"{color['english']} - {color['arabic']}")
            engine.runAndWait()
        except ImportError:
            messagebox.showinfo("Color Pronunciation", f"{color['english']} - {color['arabic']}")
        except Exception as e:
            print(f"Color TTS Error: {e}")
            messagebox.showwarning("Color Pronunciation Error", f"Could not pronounce color. Error: {e}")
                
    def next_letter(self):
        """Move to the next letter"""
        self.current_letter_index = (self.current_letter_index + 1) % len(self.letter_list)
        self.render_current_stage()
        
    def previous_letter(self):
        """Move to the previous letter"""
        self.current_letter_index = (self.current_letter_index - 1) % len(self.letter_list)
        self.render_current_stage()
        
    def practice_letter(self):
        """Practice the current letter"""
        current_letter = self.letter_list[self.current_letter_index]
        letter_data = self.letters[current_letter]
        
        # Simple practice dialog
        answer = simpledialog.askstring("Practice", f"What word starts with '{current_letter}'?")
        
        if answer and answer.lower() == letter_data['word'].lower():
            self.progress['points'] += 10
            messagebox.showinfo("Correct!", f"Great job! You earned 10 points!")
            self.update_ui()
        elif answer:
            messagebox.showinfo("Try Again", f"The correct answer is '{letter_data['word']}'")
            
            
    def toggle_sound(self):
        """Toggle sound effects"""
        self.progress['preferences']['sound_enabled'] = self.sound_var.get()
        self.save_progress()
        
    def toggle_arabic(self):
        """Toggle Arabic transliteration"""
        self.progress['preferences']['arabic_transliteration'] = self.arabic_var.get()
        self.save_progress()
        self.render_current_stage()
        
    def test_voices(self):
        """Test available voices and Arabic support"""
        try:
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            
            print(f"Available voices: {len(voices)}")
            arabic_voices = []
            
            for i, voice in enumerate(voices):
                print(f"{i+1}. {voice.name} ({voice.id})")
                if 'arabic' in voice.name.lower() or 'ar' in voice.id.lower():
                    arabic_voices.append(voice)
            
            print(f"Arabic voices found: {len(arabic_voices)}")
            for voice in arabic_voices:
                print(f"Arabic: {voice.name} ({voice.id})")
            
            if arabic_voices:
                messagebox.showinfo("Voice Test", f"Found {len(arabic_voices)} Arabic voice(s).\nTesting pronunciation...")
                # Test Arabic pronunciation
                engine.setProperty('voice', arabic_voices[0].id)
                engine.setProperty('rate', 120)
                engine.say("مرحبا")
                engine.runAndWait()
            else:
                messagebox.showwarning("Voice Test", "No Arabic voices found.\nArabic text may not be pronounced correctly.")
                
        except ImportError:
            messagebox.showerror("Voice Test", "pyttsx3 not available. Please install it.")
        except Exception as e:
            messagebox.showerror("Voice Test", f"Error testing voices: {e}")
            
    def test_voices_on_startup(self):
        """Test voices on application startup"""
        try:
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            
            arabic_voices = [v for v in voices if 'arabic' in v.name.lower() or 'ar' in v.id.lower()]
            
            if arabic_voices:
                print(f"✅ Found {len(arabic_voices)} Arabic voice(s) - Arabic support available")
            else:
                print("⚠️ No Arabic voices found - Arabic text may not be pronounced correctly")
                
        except ImportError:
            print("⚠️ pyttsx3 not available - Text-to-speech disabled")
        except Exception as e:
            print(f"⚠️ Voice test error: {e}")
        
    def update_ui(self):
        """Update the user interface"""
        self.points_label.config(text=f"Points: {self.progress['points']}")
        self.badges_label.config(text=f"Badges: {len(self.progress['badges'])}")
        
        # Update stage buttons
        for i, stage in enumerate(self.stages):
            if stage['id'] in self.progress['unlocked_stages']:
                self.stage_buttons[i].config(state='normal')
            else:
                self.stage_buttons[i].config(state='disabled')
                
    def load_progress(self):
        """Load user progress from file"""
        try:
            if os.path.exists('progress.json'):
                with open('progress.json', 'r', encoding='utf-8') as f:
                    loaded_progress = json.load(f)
                    # Validate loaded data
                    if isinstance(loaded_progress, dict):
                        self.progress.update(loaded_progress)
                    else:
                        print("Warning: Invalid progress data format")
        except FileNotFoundError:
            print("Progress file not found, starting with default progress")
        except json.JSONDecodeError as e:
            print(f"Error parsing progress file: {e}")
        except Exception as e:
            print(f"Error loading progress: {e}")
            messagebox.showwarning("Progress Error", "Could not load saved progress. Starting fresh.")
            
    def save_progress(self):
        """Save user progress to file"""
        try:
            with open('progress.json', 'w', encoding='utf-8') as f:
                json.dump(self.progress, f, ensure_ascii=False, indent=2)
        except PermissionError:
            print("Error: Permission denied when saving progress")
            messagebox.showwarning("Save Error", "Could not save progress. Check file permissions.")
        except OSError as e:
            print(f"Error saving progress: {e}")
            messagebox.showwarning("Save Error", "Could not save progress. Check disk space.")
        except Exception as e:
            print(f"Error saving progress: {e}")
            messagebox.showwarning("Save Error", "Could not save progress. Please try again.")
            
    def run(self):
        """Run the application"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def on_closing(self):
        """Handle application closing"""
        self.save_progress()
        self.root.destroy()

def main():
    """Main function"""
    print("Starting English Alphabet Learning Platform...")
    print("بدء منصة تعلم الأبجدية الإنجليزية...")
    
    try:
        # Check for required modules
        import tkinter as tk
        from tkinter import ttk, messagebox
        
        app = EnglishAlphabetPlatform()
        app.run()
    except ImportError as e:
        print(f"Missing required module: {e}")
        print("Please install required packages: pip install pygame pyttsx3")
        messagebox.showerror("Missing Dependencies", 
                           f"Missing required module: {e}\n\n"
                           "Please install required packages:\n"
                           "pip install pygame pyttsx3")
    except Exception as e:
        print(f"Error starting application: {e}")
        messagebox.showerror("Error", f"Failed to start application: {e}")

if __name__ == "__main__":
    main()
