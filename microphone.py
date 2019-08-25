# challenge found at https://open.kattis.com/problems/hissingmicrophone

a = input().lower()

if len(a.strip())<=30:
    if "ss" in a:
        print ("hiss")
    else:
        print ("no hiss")
