"""ราศี"""
DAY = input()
MONTH = input()
if (MONTH == "12" and DAY >= "22") or (MONTH == "1" and DAY <= "19"):
    print("capricorn")
elif (MONTH == "1" and DAY >= "20") or (MONTH == "2" and DAY <= "18"):
    print("aquarius")
elif (MONTH == "2" and DAY >= "19") or (MONTH == "3" and DAY <= "20"):
    print("pisces")
elif (MONTH == "3" and DAY >= "21") or (MONTH == "4" and DAY <= "19"):
    print("aries")
elif (MONTH == "4" and DAY >= "20") or (MONTH == "5" and DAY <= "20"):
    print("taurus")
elif (MONTH == "5" and DAY >= "21") or (MONTH == "6" and DAY <= "21"):
    print("gemini")
elif (MONTH == "6" and DAY >= "22") or (MONTH == "7" and DAY <= "22"):
    print("cancer")
elif (MONTH == "7" and DAY >= "23") or (MONTH == "8" and DAY <= "22"):
    print("leo")
elif (MONTH == "8" and DAY >= "23") or (MONTH == "9" and DAY <= "22"):
    print("virgo")
elif (MONTH == "9" and DAY >= "23") or (MONTH == "10" and DAY <= "23"):
    print("libra")
elif (MONTH == "10" and DAY >= "24") or (MONTH == "11" and DAY <= "21"):
    print("scorpio")
elif (MONTH == "11" and DAY >= "22") or (MONTH == "12" and DAY <= "21"):
    print("sagittarius")
