import twint
from datetime import datetime, timedelta

#function for changing recency to a date that was input, and then will pull tweets after that date
#twint isn't infallable however, and there is a limit to how far back it can actually pull tweets
def afterdate(s,recency):
    year=input("Input a year\n")
    if int(year)<2006:
        print("Invalid year\n")
        year=input("Input a year (2006 or later)\n")
    mon=input("Input a month numerically \n")
    if int(mon)>12 or int(mon)<1:
        print("Invalid Month\n")
        mon = input("Input a month Numerically (between 1 and 12)\n")
    days=input("Input a day\n")
    if int(mon)== 2 and int(days)>28:
        print("Too many days for Februrary")
        days = input("Please input a number of days equal to or less than 28")
    recency=(year+'-'+mon+'-'+days)
    print("Tweets from",s.Username,"from after",recency)
    s.Since=recency
    s.Limit=5000
    twint.run.Search(s)

#function for finding tweets with a specific keyword from given user
def usrkeywords(s):
    word = input("What word should all pulled tweets contain?\n")
    s.Search= word
    s.Limit=20
    twint.run.Search(s)

def userscrape(s,recency):
    desiredusr=input("What user would you like to scrape?\n")
    s.Username=desiredusr
    s.Limit=20
    s.User_full = True
    while(True):
        inp=input("What would you like to find from this user?\n1)Their most recent tweets?\n2)Who they follow?\n3)Who is following them?\n")
        if inp=="1":
            inp=input("Would you like to pull tweets after a specific date? (Y/N)\n")
            if inp == "Y":
                #calls afterdate function
                afterdate(s,recency)
            elif inp=="N":
                inp=input("Would you like to pull tweets containing a specific keyword? (Y/N)\n")
                if inp=='Y':
                    usrkeywords(s)
                elif inp=='N':
                    print("20 Most recent tweets from",s.Username)
                    twint.run.Search(s)
            break
        elif inp=="2":
            print(s.Username,"is following")
            twint.run.Following(s)#will always return a critical indexerror because of the way that twint codes looking into following
        elif inp=="3":
            print(s.Username+"'s followers")
            twint.run.Followers(s) #will always return a critical indexerror because of the way that twint codes looking into followers
#be able to input y,m,d to show tweets since a specific day
    return 0


if __name__ == "__main__":
    s = twint.Config()
    s.Pandas=True
    recency =(datetime.today()-timedelta(days=2)).strftime('%Y-%m-%d') #recency is up to two days ago, and the is reformatted to work w/ twint
    print("Welcome to TwitScrape\n")
    #loop to get started with the program 
    while(True):
        usrimp = input("What would you like to scrape today? \n 1)A specific user \n 2)A hashtag \n")
        if usrimp=="1":
            userscrape(s,recency)
        break

