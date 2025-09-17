# Audio Files for Mobile App - ملفات صوتية للتطبيق الجوال

## Overview - نظرة عامة

This folder contains audio files extracted from the English Learning Journey web app for use in mobile applications. The web app uses Text-to-Speech (TTS) which works in browsers but may not work in mobile WebView apps.

هذا المجلد يحتوي على ملفات صوتية مستخرجة من تطبيق رحلة تعلم الإنجليزية للاستخدام في تطبيقات الجوال. تطبيق الويب يستخدم تحويل النص إلى كلام (TTS) الذي يعمل في المتصفحات لكن قد لا يعمل في تطبيقات WebView للجوال.

## Files - الملفات

### 1. `audio_extractor.html`
- Interactive tool to extract and test audio files
- أداة تفاعلية لاستخراج واختبار الملفات الصوتية
- Allows downloading individual audio files
- يسمح بتحميل الملفات الصوتية الفردية

### 2. `mobile_audio.js`
- JavaScript file containing all audio data in base64 format
- ملف JavaScript يحتوي على جميع البيانات الصوتية بتنسيق base64
- Ready to be integrated into mobile apps
- جاهز للدمج في تطبيقات الجوال

### 3. `README.md` (this file)
- Documentation and usage instructions
- التوثيق وتعليمات الاستخدام

## Audio Content - المحتوى الصوتي

### Letters - الحروف
- All English letters A-Z
- جميع الحروف الإنجليزية من A إلى Z
- Pronunciation of each letter
- نطق كل حرف

### Words - الكلمات
- Basic English words
- كلمات إنجليزية أساسية
- Common vocabulary
- مفردات شائعة

### Sound Effects - المؤثرات الصوتية
- Correct answer sound
- صوت الإجابة الصحيحة
- Wrong answer sound
- صوت الإجابة الخاطئة
- Click sound
- صوت النقر
- Success sound
- صوت النجاح
- Level up sound
- صوت التقدم للمستوى التالي

## Integration Instructions - تعليمات التكامل

### For Mobile App Developers - لمطوري تطبيقات الجوال

1. **Include the audio file:**
   ```html
   <script src="mobile_audio.js"></script>
   ```

2. **Use the audio functions:**
   ```javascript
   // Play letter audio
   playMobileAudio('letters', 'A');
   
   // Play word audio
   playMobileAudio('words', 'Apple');
   
   // Play sound effect
   playMobileAudio('sounds', 'Correct');
   ```

3. **Check if audio exists:**
   ```javascript
   if (hasAudioFile('letters', 'A')) {
       playMobileAudio('letters', 'A');
   }
   ```

4. **Get all available audio:**
   ```javascript
   const allAudio = getAllAudioFiles();
   console.log(allAudio.letters); // ['A', 'B', 'C', ...]
   ```

### For Web App Integration - لتكامل تطبيق الويب

1. **Replace TTS with audio files:**
   ```javascript
   // Instead of using speechSynthesis
   function speak(text, type = 'letters') {
       if (hasAudioFile(type, text)) {
           playMobileAudio(type, text);
       } else {
           // Fallback to TTS
           const utterance = new SpeechSynthesisUtterance(text);
           speechSynthesis.speak(utterance);
       }
   }
   ```

2. **Update the main app:**
   - Include `mobile_audio.js` in your HTML
   - Modify the `speak` function to use audio files first
   - Keep TTS as fallback for missing audio

## Technical Details - التفاصيل التقنية

### Audio Format - تنسيق الصوت
- Format: WAV
- Encoding: Base64
- Quality: Optimized for mobile devices
- Size: Compressed for faster loading

### Browser Support - دعم المتصفحات
- All modern browsers
- Mobile WebView apps
- Progressive Web Apps (PWA)
- Cordova/PhoneGap apps

### Performance - الأداء
- Audio files are embedded in JavaScript
- No external HTTP requests needed
- Instant playback
- Offline functionality

## Troubleshooting - استكشاف الأخطاء

### Audio Not Playing - الصوت لا يعمل
1. Check if audio context is initialized
2. Ensure user interaction before playing audio
3. Check browser audio permissions
4. Verify audio file exists

### Mobile App Issues - مشاكل تطبيق الجوال
1. Enable audio permissions in app manifest
2. Initialize audio context on user interaction
3. Use fallback TTS if audio fails
4. Test on different devices

## Adding New Audio - إضافة صوت جديد

1. **Record or generate audio file**
2. **Convert to base64:**
   ```javascript
   // Use online converter or JavaScript
   const audioData = 'data:audio/wav;base64,' + base64String;
   ```
3. **Add to appropriate object:**
   ```javascript
   lettersAudio['NewLetter'] = audioData;
   ```
4. **Test the audio:**
   ```javascript
   playMobileAudio('letters', 'NewLetter');
   ```

## License - الترخيص

These audio files are provided for educational purposes as part of the English Learning Journey project.

هذه الملفات الصوتية مقدمة لأغراض تعليمية كجزء من مشروع رحلة تعلم الإنجليزية.

## Contact - الاتصال

For questions or support, contact: math2020amir@gmail.com

للأسئلة أو الدعم، اتصل بـ: math2020amir@gmail.com
