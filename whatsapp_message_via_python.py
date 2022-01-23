import pywhatkit as kit

try:
    kit.sendwhatmsg("+1**********", "Hello World!",00,00) #("phone number","message","hour","min")
    print("Message sent successfully!")
except:
    print("Something went wrong, try again.")
