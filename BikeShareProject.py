import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Select a city that you would like to explore data on: chicago, new york city, washington: \n')).lower()
        if city in CITY_DATA:
            break
        else:
            print('Your entry of \'{}\' is not a valid city. \nPlease choose between:\n-chicago\n-new york city\n-washington\n'.format(city))
      
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['january','february','march','april','may','june','all']
    while True:
        month = str(input('\nSelect a month that you would like to explore data on: january, february, ..., june, or all: \n')).lower()
        if (month in month_list):
            break
        else:
            print('Your entry of \'{}\' is not a valid month.\nPlease enter a valid month:\n-january\n-february\n-march\n-april\n-may\n-june'.format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        day = str(input('\nSelect a day that you would like to explore data on: monday, tuesday, ..., sunday, or all: \n')).lower()
        if (day in day_list):
            break
        else:
            print('Your entry of \'{}\' is not a valid day.\nPlease enter a valid day:\n-sunday\n-monday\n-tuesday\n-wednesday\n-thursday\n-friday\n-saturday'.format(day))
    
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()  
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = str(df['month'].mode()[0])
    month_dict = {'1': 'January','2': 'February','3': 'March','4': 'April','5': 'May', '6': 'June'}
    print('Most common month: ' + month_dict[most_common_month])

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_day = df['day_of_week'].mode()[0]  
    print('Most common day of week: ' + str(most_common_day))

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    most_common_hour = df['start_hour'].mode()[0]
    print('Most common start hour: ' + str(most_common_hour).rjust(2,'0') + ":00")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('The most common \'Start Station\': ' + most_common_start)
    
    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('The most common \'End Station\': ' + most_common_end)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + " \033[1mTO\033[0m " + df['End Station']
    most_common_s_e = df['start_end'].mode()[0]
    print('The most common \'Start\' \033[1mTO\033[0m \'End\' route is: ' + most_common_s_e)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds: ' + str(total_travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time in seconds: ' + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
    except:
        user_types = '\033[1;31mThe column \'User Type\' is not present.\033[0;37m'
    finally:
        print(str(user_types) + '\n')

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
    except:
        gender_types = '\n\033[1;31mUnable to display gender metrics.\nThe column \'Gender\' is not present.\033[0;37m'
    print(str(gender_types) + '\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = df['Birth Year'].min()
        latest_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
        print('Earliest Year Of Birth: ' + str(int(earliest_yob)))
        print('Latest Year Of Birth: ' + str(int(latest_yob)))
        print('Most common Year Of Birth: ' + str(int(most_common_yob)))
    except:
        print('\n\033[1;31mUnable to display birth year metrics.\nThe column \'Birth Year\' is not present.\033[0;37m')


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
        
        '''
        The lines below ask the user if they would like to view the raw data and then ask for additional data if the answer is yes.
        If the ask for additional data is also yes, it continues to ask and give until the user responds no or end of file reached.
        After the user ends the requests for raw data it bring them back into the loop to restart the program to view additional city data
        '''
        
        with open(CITY_DATA[city]) as read_file:
            outer_loop = True
            while outer_loop == True:            
                check_raw = input('\nWould you like to review the first 5 lines of the raw data? Enter yes or no.\n')
                if check_raw.lower() != 'yes':
                    break
                else:                 
                    print('\n' + next(read_file))
                    print(next(read_file))
                    print(next(read_file))
                    print(next(read_file))
                    print(next(read_file))
                    while True:
                        check_more = input('\nWould you like to review the next 5 lines of the raw data? Enter yes or no.\n')
                        if check_more.lower() != 'yes':
                            outer_loop = False
                            break
                        else:
                            try:
                                print('\n' + next(read_file))
                            except:
                                print('\033[1;31mYou have reached the end of the file.\033[0;37m')
                                outer_loop = False
                                break
                            try:
                                print(next(read_file))
                            except:
                                print('\033[1;31mYou have reached the end of the file.\033[0;37m')
                                outer_loop = False
                                break
                            try:
                                print(next(read_file))
                            except:
                                print('\033[1;31mYou have reached the end of the file.\033[0;37m')
                                outer_loop = False
                                break
                            try:
                                print(next(read_file))
                            except:
                                print('\033[1;31mYou have reached the end of the file.\033[0;37m')
                                outer_loop = False
                                break
                            try:
                                print(next(read_file))
                            except:
                                print('\033[1;31mYou have reached the end of the file.\033[0;37m')
                                outer_loop = False
                                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
