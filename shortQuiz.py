#!python3

name = input("What is your name?")
print("Hi %r, nice to meet you." % name)
yes =input("I'd like to ask you a few questions.Can I proceed?")

likes = input("What do you like doing in your spare time?")
lives = input("Where do you live?")
aspiration = input("What are your life aspirations?")
inspiration = input("What inspires you most?")
To_Do = input("What are you doing to make sure you fulfill your dreams?")

print('''\nAlright, so you said you like %r. You live in %r.\n
And your aspirations are %r.\n
Your inspirations are %r and you are doing %r\
to fulfill your dreams and goals. Nice.''' % (likes, lives, aspiration, inspiration, To_Do))
