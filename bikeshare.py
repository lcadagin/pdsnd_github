import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_selection = ['january', 'february', 'march', 'april', 'may', 'june']

weekday_selection = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.  Will prompt user again if invalid data is provided.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter city name (chicago, new york city, or washington): ').lower()
    while city not in CITY_DATA:
        city = input('Does not compute, please try entering a valid city name (chicago, new york city, or washington) and check for spelling: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter a specific month you would like to filter on (january, february, march, april, may, june) or type 'all': ").lower()
    while (month not in month_selection) and (month != 'all'):
        month = input('Does not compute, please try entering a valid selection (january, february, march, april, may, june, or all) and check for spelling: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter a specific day of the week you would like to filter on (monday, tuesday, wednesday, thursday, friday, saturday, sunday) or type 'all': ").lower()
    while (day not in weekday_selection) and (day != 'all'):
        day = input('Does not compute, please try entering a valid selection (monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all) and check for spelling: ').lower()

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        month = month_selection.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most frequent month of travel:', month_selection[df['month'].mode()[0] - 1])

    # TO DO: display the most common day of week
    print('The most frequent day of week to travel:', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most fequent hour of the day to travel:', str(df['hour'].mode()[0]) + ':00 (24 hour clock)')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is:', df['Start Station'].value_counts().index[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station is:', df['End Station'].value_counts().index[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip:', df.groupby(['Start Station', 'End Station']).size().nlargest(1).index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time for all trips in this period is: ' + str(df['Trip Duration'].sum()/60) + ' minutes')

    # TO DO: display mean travel time
    print('The mean travel time for all trips in this period is: ' + str(df['Trip Duration'].mean()/60) + ' minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of User Types:')
    print(df['User Type'].value_counts().index[0], df['User Type'].value_counts()[0], 'people')
    print(df['User Type'].value_counts().index[1], df['User Type'].value_counts()[1], 'people')

    # TO DO: Display counts of gender
    print('Counts of Gender:')
    if 'Gender' in df:
        print(df['Gender'].value_counts().index[0], df['Gender'].value_counts()[0], 'people')
        print(df['Gender'].value_counts().index[1], df['Gender'].value_counts()[1], 'people')
    else:
        print('Gender data not collected for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Birth Year Statistics:')
    if 'Birth Year' in df:
        print('The Earliest year of birth for this group is', int(df['Birth Year'].min()))
        print('The most recent year of birth for this gorup is', int(df['Birth Year'].max()))
        print('The most common year of birth for this group is', int(df['Birth Year'].mode()))
    else:
        print('Birth Year data not collected for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
