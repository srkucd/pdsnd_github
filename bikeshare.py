#Well this is another modification under refactoring branch.

#Looks like I failed last time, I am going to pass this submission.
>>>>>>> refactoring
import time
import pandas as pd
import datetime
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_dict = {1: 'january',
              2: 'february',
              3: 'march',
              4: 'april',
              5: 'may',
              6: 'june'}

weekday_dict = {1: 'monday',
                2: 'tuesday',
                3: 'wednesday',
                4: 'thursday',
                5: 'friday',
                6: 'saturday',
                7: 'sunday'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Insert the name of city you are interested in(Chicago, New York City, Washington)")
        if city.lower() in CITY_DATA.keys():
            print('Okay, got it. you choose ' + city.title() + '.\n')
            break
        else:
            print("Invalid data, please confirm your input city is Chicago, New York City or Washington.\n")
            continue

    #Get user input for month (all, january, february, ... , june)

    while True:
        month_input = input("Insert the number of the month you are interested.[Jan(1)-Jun(6)], for unfiltered data, "
                            "please input 'all'.")
        if month_input in str(list(month_dict.keys())):
            month = month_dict.get(int(month_input))
            print('Okay, got it. you choose ' + month.title() + '.\n')
            break
        elif month_input == 'all':
            month = 'all'
            print("Okay, got it, no month filter selected.\n")
            break
        else:
            print("Invalid data, please confirm your input between 1-6\n")
            continue
    #Get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day_input = input("Insert the weekday number you are interested.[Mon-Sun:1-7],for unfiltered data, please "
                          "input 'all'.")
        if day_input in str(list(weekday_dict.keys())):
            day = weekday_dict.get(int(day_input))
            print('Okay, got it. you choose ' + day.title() + '.\n')
            break
        elif day_input == 'all':
            day = 'all'
            print('Okay, got it, no weekday filter selected.\n')
            break
        else:
            print("Invalid data, please confirm your input between 1-7")
            continue

    print('City: '+city.title())
    print('Month: '+month.title())
    print('Weekday: '+day.title())



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':

        df = df[df['month'] == month.title()]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    top_month = df['month'].value_counts().head(1)
    top_day = df['day_of_week'].value_counts().head(1)
    top_hours = df['Start Time'].dt.hour.value_counts().head(1)

    #Display the most common month
    if df['month'].nunique() == 1:
        print('You use month as a filter, hence, most common month display function is not available.\n')
    else:
        print('The most common month is: ' + str(top_month.index[0]) + '. ' + 'Count: ' + str(top_month[0]))

    #Display the most common day of week
    if df['day_of_week'].nunique() == 1:
        print('You use weekday as filter, hence, most common day display function is not available.\n')
    else:
        print('The most common day is: ' + str(top_day.index[0]) + '. Count: ' + str(top_day[0]))

    #Display the most common start hour
    print('The most common start hour is ' + str(top_hours.index[0]) + ':00 (24 hours). Count: '
          + str(top_hours[top_hours.index[0]]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    top_start = df['Start Station'].value_counts().head(1)
    top_end = df['End Station'].value_counts().head(1)

    #Display most commonly used start station
    print('The most commonly used start station is ' + str(top_start.index[0]) + '. Count: ' + str(top_start[0]))

    #Display most commonly used end station
    print('The most commonly used end station is ' + str(top_end.index[0] + '. Count: ' + str(top_end[0])))

    #Display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + '-' + df['End Station']
    top_combination = df['Combination'].value_counts().head(1)
    print('The most frequent combination between start station and end station is: ' + str(top_combination.index[0])
          + '. Count: ' + str(top_combination[0]))

    #This column is no longer useful.
    del df['Combination']

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('Calculating Trip Duration...\n')
    start_time = time.time()

    #Display total travel time
    total_sec = np.sum(df['Trip Duration'])
    total_format = datetime.timedelta(seconds = int(total_sec))
    print('Total trip duration is ' + str(total_format) + '.')

    #Display average trip duration
    avg_sec = np.average(df['Trip Duration'])
    avg_format = datetime.timedelta(seconds = int(avg_sec))
    print('Average trip duration is ' + str(avg_format) + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('Calculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print('User Type Count:')
    print(df['User Type'].value_counts())
    print()

    #Display counts of gender
    print('User Gender Count:')
    try:
        print(df['Gender'].value_counts())
        print()
    except:
        print('Sorry, gender information only available in NYC and Chicago.\n')

    #Display earliest, most recent, and most common year of birth
    print('Birth year description: ')
    try:
        top_birth = df['Birth Year'].value_counts().head(1)
        print('The oldest user was born in ' + str(int(df['Birth Year'].min())) + '.')
        print('The youngest user was born in ' + str(int(df['Birth Year'].max())) + '.')
        print('The most common user was born in ' + str(int(top_birth.index[0]))+ ', Count: ' + str(top_birth[top_birth.index[0]]))
    except:
        print('Sorry, age information only available in NYC and Chicago.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    raw_order = input("Do you need to scan the raw data? (y)es/(n)o")
    if raw_order == 'y':
        num = 5
        print(df.head(num))
        while num < len(df.index):
            five_more = input("Do you want to scan five more rows? (y)es/(n)o")
            try:
                if five_more == 'y':
                    num += 5
                    more = df.head(num)
                    print(more.tail(5))
                    continue
                elif five_more == 'n':
                    print('Thank you. ' + str(num) + ' rows of dataset casted.')
                    break
                else:
                    print('Invalid value, please try again.')
                    continue
            except:
                print(df.tail())
                print("You arrived to the bottom of the dataset.")
    elif raw_order == 'n':
        print('Thank you. no raw data will be casted.')
    else:
        print("Invalid value, please try again.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? yes/no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
