import pyttsx3

# تهيئة المحرك
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print("welcome to python speck\n==================================\n")
while True:

    user_speck = input("Enter what you want python to say, 'q to quit': ")
    if user_speck != 'q':
        # تحويل النص إلى كلام
        engine.say(user_speck)
        engine.runAndWait()
    else:
        print("goodbye!")
        break
