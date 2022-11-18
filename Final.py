### IMPORTS
import numpy as np
import pandas as pd
import os
import fontstyle as fs
import matplotlib.pyplot as plt
from prettytable import PrettyTable

##Design
print("=+=+=" * 100)

##Underline Capture
underline_start = "\33[4m"
Underline_end = "\033[0m"

# Time
import time



## intro
intro = "Welcome to my project"
intro = fs.apply(intro, "RED/BOLD/UNDERLINE")
intro_print = intro.center(150)
intro = "\33[4m " + "Welcome to my project"
print(intro_print)

print("\nIn this project: \nWe wil be analysing the data of the some of the top "
      "Tech related Companies of the 21st century......\n")#

print("In this project we will be analysing the data of netflix.")



## if if is not satisfied
while_1 = ("Choose the correct Option")
while_1 = fs.apply(while_1, "RED,BLINK")
while_2 = fs.apply("Please enter a valid option!!", "RED,STRIKE,BLINK")

##Menu Table


# serive providing companies, entertainment services, other servies
# google separate column : including youtube and all
#                        : or can write as a google service

##Additional Beauty
error = "ERROR!!!"
error = fs.apply(error, "RED,BOLD")
continuer_designer="\nWould you like to explore more options?\t:\t"
continuer_designer=fs.apply(continuer_designer,"BLUE,ITALIC")
##csv calling
netflix_csv=pd.read_csv("C:/Users/bhavesh/Downloads/netflix_titles.csv")

### Project Code Starter

##linker
lagger = 0

while lagger < 1:

    ##Menu

    a = input('Press any key to start the programme    :\t')
    # add by serial number
    # Awards
    # type of content metaplot
    # avability, usgae

    ## Netflix Data
    if a==1:
        print()
    else:
        print("\n Netflix:".center(10),
              "\n\tNetflix is an American subscription streaming service and production company."
              "\n\tIt that allows our members to watch TV shows and movies without commercials on an internet-connected device.")

        ## Table Created
        Netflix_table = PrettyTable(["Company", "Netflix"])

        ## Add rows
        Netflix_table.add_row(["Owners", " Reed Hastings \n Marc Randolph "])
        Netflix_table.add_row(["", ""])
        Netflix_table.add_row(["Founder In Year", "1997"])
        Netflix_table.add_row(["", ""])
        Netflix_table.add_row(["Industry", "Technology & Entertainment industry, mass media"])
        Netflix_table.add_row(["", ""])
        Netflix_table.add_row(
            ["Key People", "Reed Hastings (Chairman, Co-CEO)\nTed Sarandos (Co-CEO, CCO)\nGreg Peters (COO, CPO) "])
        print(Netflix_table)
        types_of_data = netflix_csv['type'].unique()
        len_type = len(types_of_data)

        ##### Check 1
        #####  Netflix_table = fs.apply (Netflix_table, "RED/BOLD" )
        #  print ( Netflix_table )
        #  q = "Which year sows and movie you would like to count"
        #        c=[]
        #        for b in netflix_csv["release_year"]:
        #               c=c+[b]
        #        number of shows =
        #        print(c.count(q))
        #
        #  else :
        #              print()
        #             else:
        #       print()

        # Options.add_row([""])

        ## Options Table for Netflix
        Options = PrettyTable(["Analyes Data ", "Options "])
        Options.add_row(["Rough Idea of Data in CSV", " 1 "])

        ##### once it is used it get soff the list

        # include , no of shows, no. of serials,
        # inlude detailed andd # Individual Analyisis by the User

        Options.add_row(["Get into More Commands", " 2 "])
        Options.add_row(["Graphical Analysis of CSV", " 3 "])
        Options.add_row(["Specific Analysis", " 4 "])
        Options.add_row(["Exit Netflix Data Analysis", " 5 "])
        Options.add_row(["Exit Program", " 6 "])

        netflix_while1 = 0
        k = True
        print()

        while netflix_while1 < 1:
            k = True
            print(Options)
            option_checker = int(input("Which option would you like to choose\t:\t"))
            if option_checker == 1:
                print("\nThe given csv is on Netflix\n")
                print('The csv contains\t:\n')
                nod = netflix_csv['show_id'].count()
                print('DATA of', nod, "Shows")
                ####Color it

                print('Netflix contain:', types_of_data)
                tod = netflix_csv['director'].count()
                print("The data is directed by about", tod, "people")
                noc = 0
                for l in netflix_csv['country'].unique():
                    noc += 1
                print("The shows are available in around ", noc, "countries")

                continuer_netflix = input(continuer_designer)
                if continuer_netflix == 'Yes' or continuer_netflix == "YES" or continuer_netflix == "Ok" or continuer_netflix == "yes":
                    print()
                    k = False
                else:
                    netflix_while1 += 10
                    k = False



            elif option_checker == 2:

                netflix_while2 = 0
                while netflix_while2 < 1:
                    Options1 = PrettyTable(["Analyes Data ", "Options "])
                    Options1.add_row(["On type of Data", " 1 "])
                    Options1.add_row(["On Basis of Country", " 2 "])
                    Options1.add_row(["Rating", " 3 "])
                    ###
                    Options1.add_row(["date_added", " 4 "])
                    Options1.add_row(['release_year', "5"])

                    Options1.add_row(["Exit More Commands Prompt", " 6 "])
                    Options1.add_row(["Exit Netflix Data Analysis", " 7 "])
                    print(Options1)
                    option_checker2 = int(input("Which type of data you want to see\t:\t"))

                    rate_calculator=0

                    if option_checker2 == 1:
                        print('The csv has', len_type, "Type of data which are", types_of_data)
                        type_while_satisfier = 0
                        while type_while_satisfier < len_type:
                            type_while_counter = 0
                            for b in netflix_csv['type']:
                                if b == types_of_data[type_while_satisfier]:
                                    type_while_counter += 1
                            print('Number of', types_of_data[type_while_satisfier], "=", type_while_counter)

                            type_while_satisfier += 1

                        asker_show_on_type = input('\nWould you like to see all data on basis of type\t:\t')
                        while_type_satisfier = 0
                        while while_type_satisfier < 1:
                            if asker_show_on_type == "yes" or asker_show_on_type == "YES" or asker_show_on_type == 'Yes':
                                asker_show_on_type2 = input('Which one would like to choose?\t:\t')
                                for type_while in types_of_data:
                                    if asker_show_on_type2 == type_while:
                                        a = 0
                                        while a < len(netflix_csv):
                                            if netflix_csv.loc[a]['type'] == type_while:
                                                print(netflix_csv.loc[a])
                                                rate_calculator+=1
                                            a += 1

                                    print("There were total",rate_calculator,"records in the rating ",asker_show_on_type2)

                                while_type = input("\nWould you like to see for others also\t:\t")
                                if while_type == "Yes" or while_type == "YES" or while_type == "yes":
                                    print()
                                elif while_type == "No" or while_type == "NO" or while_type == "no":
                                    print()
                                    while_type_satisfier += 21
                                else:
                                    print(error, "Please choose from Yes/No")


                            else:
                                print()
                                while_type_satisfier += 1

                        continuer_netflix2 = input(continuer_designer)

                        if continuer_netflix2 == 'Yes' or continuer_netflix2 == "YES" or continuer_netflix2 == "Ok" or continuer_netflix2 == "yes":
                            print()
                            k = False

                        else:
                            netflix_while2 += 1


                    ###add in while
                    elif option_checker2 == 2:
                        netflix_while3 = 0
                        while netflix_while3 < 1:
                            country_counter_netflix = 0
                            country_input_netflix = input('Which country would you like to check?:')
                            for d in netflix_csv['country']:
                                if d == country_input_netflix:
                                    country_counter_netflix = country_counter_netflix + 1
                            print("\n", country_counter_netflix, "shows are available in your country",
                                  country_input_netflix)

                            asker_showon_country3 = input("\nWould you like to see the details of the shows also?\t:\t")
                            if asker_showon_country3 == "yes" or asker_showon_country3 == "YES" or asker_showon_country3 == "Yes":
                                a = 0
                                c = 0
                                while a < len(netflix_csv):
                                    if netflix_csv.loc[a]['country'] == country_input_netflix:
                                        print(netflix_csv.loc[a])
                                        c += 1
                                    a += 1
                            else:
                                print()
                            asker_showon_country2 = input("\nWould like to see for other countries also?\t:\t")
                            if asker_showon_country2 == 'YES' or asker_showon_country2 == "Yes" or asker_showon_country2 == "yes":
                                print()
                            else:
                                netflix_while3 += 1
                        print("")
                        continuer_netflix2 = input(continuer_designer)
                        if continuer_netflix2 == 'Yes' or continuer_netflix2 == "YES" or continuer_netflix2 == "Ok" or continuer_netflix2 == "yes":
                            print()
                        else:
                            netflix_while2 += 1


                    elif option_checker2 == 3:
                        print("\n Ratings available for the shows are :\n\n", netflix_csv['rating'].unique())
                        asker_shown_rating = int(input(
                            "Would you like to choose specifically on your own\t :: \t press : 1 \n\t\t\t\t\t\t\t\t\t"
                            "or\n \t\t\t\t\tComputer do the job\t ::\t press : 2\n\t\t\t\t\t\t\t:"))
                        while_rating = 0

                        while while_rating < 1:
                            if asker_shown_rating == 1:
                                asker_shown_rating_table = PrettyTable(["Options Available", "Identifier"])
                                option_fixer = 1
                                while option_fixer < len(netflix_csv['rating'].unique()) + 1:
                                    for b in netflix_csv['rating'].unique():
                                        asker_shown_rating_table.add_row([b, option_fixer])
                                        option_fixer += 1
                                print(asker_shown_rating_table)

                                input_rating_1 = [int(x) for x in
                                                  input("Enter the ratings you would like to choose: ").split(",")]
                                for controller in input_rating_1:
                                    option_fixer2 = 1
                                    while option_fixer2 < len(netflix_csv['rating'].unique()) + 1:
                                        for b in netflix_csv['rating'].unique():

                                            if controller == option_fixer2:
                                                c = 0
                                                k = 0
                                                for d in netflix_csv['rating']:
                                                    if d == b:
                                                        c = c + 1
                                                print("\nThere are", c, "number of shows with rating:", b)
                                            option_fixer2 += 1
                                print()
                                asker_shown_rating2 = input("Would also like to see the data of the ratings?\t:\t")
                                if asker_shown_rating2 == "Yes" or asker_shown_rating2 == "yes" or asker_shown_rating2 == "Yes":

                                    for controller in input_rating_1:
                                        option_fixer3 = 1
                                        while option_fixer3 < len(netflix_csv['rating'].unique()) + 1:
                                            for b in netflix_csv['rating'].unique():
                                                if controller == option_fixer3:
                                                    a = 0
                                                    c = 0
                                                    print('\nData with rating " ', b, '"\t:')
                                                    while a < len(netflix_csv):
                                                        if netflix_csv.loc[a]['rating'] == b:
                                                            print(netflix_csv.loc[a])
                                                            print()

                                                        a += 1

                                                option_fixer3 += 1
                                            while_rating += 1
                                else:
                                    while_rating += 1
                                    print()



                            elif asker_shown_rating == 2:
                                print()
                                option_fixer3 = 1
                                while option_fixer3 < len(netflix_csv['rating'].unique()) + 1:
                                    for b in netflix_csv['rating'].unique():
                                        option_fixer3 += 1
                                        c = 0
                                        for d in netflix_csv['rating']:
                                            if d == b:
                                                c += 1
                                        print("There are", c, "shows with", b, 'rating ')

                                print()
                                while_rating += 1
                            else:
                                print(error, "Please select a valid option.")

                        continuer_netflix2 = input(continuer_designer)
                        if continuer_netflix2 == "Yes" or continuer_netflix2 == "YES" or continuer_netflix2 == "Ok" or continuer_netflix2 == "yes":
                            print()



                        else:
                            netflix_while2 += 1


                    elif option_checker2==4:
                        unique_date = []
                        d = 0
                        for a in netflix_csv["date_added"] :
                            if a not in unique_date :
                                d = d + 1
                                uique_date = unique_date.append ( a )


                        print ( 'There are ',len(netflix_csv["date_added"]),"out of which there are only",d ,"unique released dates")

                        date_asker=input("Would you like to see the dates also?\t:\t")
                        if date_asker=="yes"or date_asker=="Yes"or date_asker=="YES":
                            print("The following are the dates:")
                            for unique_date1 in unique_date:
                                print(unique_date1)
                            print()
                        date_asker100=input('Would you like to see data on the basis of date\t:\t')
                        if date_asker100=='Yes'or date_asker100=='yes'or date_asker100=="YES":
                            date_asker200 =  ( input ( "Which date record would you like to see\t:\t" ) )
                            a = 0
                            counter_release_year = 0
                            while a < len ( netflix_csv ) :
                                if netflix_csv.loc[a]['date_added'] == date_asker200 :
                                    print ( netflix_csv.loc[a] )
                                    counter_release_year += 1

                                a += 1

                            print ( "there were " , counter_release_year , "records for the year" , date_asker200 )

                        continuer_netflix2 = input ( continuer_designer )
                        if continuer_netflix2 == "Yes" or continuer_netflix2 == "YES" or continuer_netflix2 == "Ok" or continuer_netflix2 == "yes" :
                            print ()



                        else :
                            netflix_while2 += 1


                    elif option_checker2==5:
                        unique_date1 = []
                        d1 = 0
                        for a1 in netflix_csv["release_year"] :
                            if a1 not in unique_date1 :
                                d1 = d1 + 1
                                uique_date1 = unique_date1.append ( a1 )

                        print ( 'There are ' , len ( netflix_csv["release_year"] ) , "out of which there are only " , d1 ,
                                "unique records on basis of released year" )

                        date_asker1= input ( "Would you like to see the dates also?\t:\t" )
                        if date_asker1 == "yes" or date_asker1 == "Yes" or date_asker1 == "YES" :
                            print ( "The following are the years:" )
                            for unique_date2 in unique_date1 :
                                print ( unique_date2 )
                            print ()

                        year_asker=input("Would you like to see the data on the basis of released year\t:\t")
                        if year_asker=="Yes" or year_asker=="yes" or year_asker=="YES":
                            date_asker20 = input ( "Which year would you like to choose\t:\t" )
                            a = 0
                            counter_release_year = 0
                            while a < len ( netflix_csv ) :
                                if netflix_csv.loc[a]['release_year'] == date_asker20 :
                                    print ( netflix_csv.loc[a] )
                                    counter_release_year += 1

                                a += 1

                            print ( "there were " , counter_release_year , "records for the year" , date_asker20 )



                        continuer_netflix2 = input ( continuer_designer )
                        if continuer_netflix2 == "Yes" or continuer_netflix2 == "YES" or continuer_netflix2 == "Ok" or continuer_netflix2 == "yes" :
                            print ()



                        else :
                            netflix_while2 += 1












                    elif option_checker2 == 6:
                        print()
                        netflix_while2 += 1
                        k=False
                    elif option_checker2 == 7:
                        print()
                        netflix_while2 += 1
                        netflix_while1 += 3
                        k=False
                    else:
                        print(error, '\nPlease Select a valid command')


            elif option_checker==3:
                print()









            elif option_checker == 4:

                while_specific = 0

                limitetator = 0

                specific_table = PrettyTable ( ["Options" , "Identifier"] )

                specific_table.add_row ( ["See the Whole Record " , "1"] )

                specific_table.add_row ( ["Choose the feilds to see from" , "2"] )

                specific_table.add_row ( ["See the feilds Available" , "3"] )


                while while_specific<1:
                    toma_tata=True





                    while_specific1 = 0


                    j = 0
                    j1 = 0

                    print ( specific_table )

                    specific_table_input = int ( input ( 'Which option would you like to choose \t:\t' ) )

                    t = 0
                    t1 = 0

                    while while_specific1 < 1 :



                        print ()

                        if specific_table_input == 1 :

                            print ()

                            while j < 1 :

                                print ()

                                while t < 1 :
                                    print ( ("Type 'Dont Know' if you want to see feilds").center ( 200 ) )

                                    t += 1

                                specific_input = [(x) for x in

                                                  input (
                                                      "Enter the field on which you would like to identify the data: " ).split (

                                                      "," )]

                                if specific_input == ["Dont Know"] :

                                    print ( "Following are the fields available :\n" )

                                    for netflix_table_fields in netflix_csv :
                                        print ( netflix_table_fields )

                                    k = False

                                    t += 1

                                    print ()

                                else :

                                    for controller2 in specific_input :

                                        asker = input (

                                            "Enter the detail of the column on the basis of the chosen field \t:\t" )

                                        a = 0

                                        while a < len ( netflix_csv ) :

                                            if netflix_csv.loc[a][controller2] == asker :
                                                print ( netflix_csv.loc[a] )

                                            a += 1

                                    continuer_netflix2 = input ( "Would you like to see for other fields?\t:\t" )

                                    if continuer_netflix2 == "Yes" or continuer_netflix2 == "YES" or continuer_netflix2 == "Ok" or continuer_netflix2 == "yes" :

                                        print ()

                                        t = 10


                                    else :

                                        j = 10

                                        while_specific1 = 10

                                        k = False

                            #############

                            else :
                                k = False

                                print ()

                                while_specific1 += 1

                        elif specific_table_input == 2 :

                            print ()
                            while j1 < 1 :
                                print ()


                                while t1 < 1 :
                                    print ( ("Type 'Dont Know Fields' if you want to see fields").center ( 200 ) )
                                    t1 += 1

                                specific_input3 = [(x) for x in
                                                   input (
                                                       "Enter the field on which you would like to identify the data: " ).split (
                                                       "," )]
                                if specific_input3 == ["Dont Know Fields"] :

                                    print ( "Following are the fields available :\n" )

                                    for netflix_table_fields in netflix_csv :
                                        print ( netflix_table_fields )

                                    k = False

                                    t1 += 10



                                    print ()

                                else :
                                    specific_input4 = [(x) for x in
                                                       input (
                                                           "Enter the columns you would like to see :  " ).split (
                                                           "," )]
                                    for controller2 in specific_input3 :

                                        asker2 = [(x) for x in input (
                                            "Enter the detail of the column on the basis of the chosen field : " ).split (
                                            "," )]
                                        for controller5 in asker2 :
                                            a = 0

                                            while a < len ( netflix_csv ) :
                                                if netflix_csv.loc[a][controller2] == controller5 :
                                                    for controller3 in specific_input4 :
                                                        print ( controller3 , "is" , netflix_csv.loc[a][controller3] )
                                                a += 1


                                    continuer_netflix2 = input ( "Would you like to see for other fields?\t:\t" )
                                    if continuer_netflix2 == "Yes" or continuer_netflix2 == "YES" or continuer_netflix2 == "Ok" or continuer_netflix2 == "yes" :
                                        print ()

                                    else :
                                        print ()

                                        while_specific1 += 1
                                        j1 = 10










                        elif specific_table_input == 3 :

                            print ()

                            for netflix_table_fields in netflix_csv :
                                print ( netflix_table_fields )

                            while_specific1 += 1

                            print ()

                        elif specific_table_input == 4 :

                            netflix_while1 = 0

                            while_specific1 += 1

                            while_specific += 1
                            toma_tata = False


                        else :

                            print ( error , "\n Please select a valid Command" )

                    if toma_tata == True :
                        continuer_netflix2 = input ( continuer_designer )
                        if continuer_netflix2 == "Yes" or continuer_netflix2 == "YES" or continuer_netflix2 == "Ok" or continuer_netflix2 == "yes" :
                            print ()



                            while limitetator < 1 :
                                specific_table.add_row ( ["Exit Specific Analysis" , "4"] )
                                print("noob")
                                limitetator = 10

                            while_specific1 = 0






                        else :
                            while_specific += 1
                    else :
                        while_specific1 += 1









































            elif option_checker == 5:
                print()
                netflix_while1 += 3
            elif option_checker == 6:
                print('''\nThank you...
                                  Hope you enjoyed the project
                                  Bye , have a great day a head.''')
                exit()

            else:
                if k==True:
                    print("\n", error, "\nPlease select a valid option.\n")
                else:
                    print()
        #####apply full time analyis
        ## Individual Analyisis by the User ### kala kala specify karna

        ## Linker for escape phase 1

    cutter = 0

    while cutter < 1:
        lagger_cutter3 = 0
        lagger_cutter = input("Do you want to see again ?\t:")
        while lagger_cutter3 < 1:
            if lagger_cutter == "Yes" or lagger_cutter == "Ok" or lagger_cutter == "YES" or lagger_cutter == "yes":
                print()
                lagger_cutter3 += 1
                cutter += 1
                K = False
            elif lagger_cutter == "No" or lagger_cutter == "no" or lagger_cutter == "NO" or lagger_cutter == "Exit":
                print()
                lagger_cutter4 = 0
                lagger_cutter2 = input("Are you sure you want to exit the programme?\t:")
                if lagger_cutter2 == "Yes" or lagger_cutter2 == "Ok" or lagger_cutter2 == "YES" or lagger_cutter2 == "yes":
                    lagger += 1
                    print('''\nThank you...
                                                                                  Hope you enjoyed the project
                                                                                  Bye , have a greatday a head.''')
                    exit()
                elif lagger_cutter2 == "No" or lagger_cutter2 == "no" or lagger_cutter2 == "NO":
                    print()
                    lagger_cutter3 += 1
                else:
                    print(while_2)





            else:
                print(while_2)
                print()
                lagger_cutter3 += 1





    else:
        if K==True:
            print(error,"\n",while_1)

