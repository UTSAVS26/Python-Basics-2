#Program to print the Zodiac Sign for the user’s date of birth 
day = int(input("Input birthday: ")) 
month = input("Input month of birth (e.g. March, July etc): ") 
if month == 'December':
    if (day < 22) :
        astro_sign = 'SAGITTARIUS' 
    else:
        astro_sign = 'CAPRICORN' 
elif month == 'January': 
    if (day < 20):  
         astro_sign = 'CAPRICORN' 
    else:
        astro_sign ='AQUARIUS' 
elif month == 'February': 
    if (day < 19):
        astro_sign = 'AQUARIUS'  
    else: 
       astro_sign ='PISCES' 
elif month == 'March':
    if (day < 21):	
        astro_sign = 'PISCES'  
    else: 
        astro_sign = 'ARIES' 
elif month == 'April': 
    if (day < 20):
            astro_sign = 'ARIES'  
    else:
            astro_sign ='TAURUS' 
elif month == 'May': 
    if (day < 21):
            astro_sign = 'TAURUS'  
    else:   
            astro_sign ='GEMINI' 
elif month == 'June': 
    if (day < 21):
        astro_sign = 'GEMINI'  
    else:
        astro_sign ='CANCER' 
elif month == 'July': 
    if (day <23):
             astro_sign = 'CANCER'  
    else:
            astro_sign ='LEO' 
elif month == 'August': 	
    if (day <23):
        astro_sign = 'LEO'
    else:
        astro_sign ='VIRGO' 
elif month == 'September': 	
    if (day < 23):
        astro_sign = 'VIRGO' 
    else: 
       astro_sign ='LIBRA' 
elif month == 'October': 
    if (day < 23): 
        astro_sign = 'LIBRA' 
    else:
        astro_sign ='SCORPIO' 
elif month == 'November': 	   
    if (day < 22):
        astro_sign = 'SCORPIO' 
    else: 
        astro_sign = 'SAGITTARIUS' 
print("Your Astrological sign is :",astro_sign)
