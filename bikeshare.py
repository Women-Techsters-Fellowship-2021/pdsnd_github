import time
import pandas as pd
import numpy as np

#Creating a dictionary containing the data for the three cities
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#Creating a dictionary containing all the months from January to February and 'all'
MONTH_DATA = {'january': 1,
              'february': 2,
              'march': 3,
              'april': 4,
              'may': 5,
              'june': 6,
              'july': 7,
              'august': 8,
              'september': 9,
              'october': 10,
              'november': 11,
              'december': 12,
              'all': 13}

#Creating a list containing all the days in a week  and 'all'
DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


# Function to filter the city, month and day required by the user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which of these city data would like to explore: Chicago, New York, or Washington? ').lower().strip()
    while city not in(CITY_DATA.keys()):
        print('\nYou provided invalid city name. Check spellimng and kindly enter any of the following city Chicago, New York, or Washington')
        city = input('Which of these city data would like to explore: Chicago, New York, or Washington? ').lower().strip()

    
    # get user input for month (all, january, february, ... , june)
    month = input("Enter which of the month between January to December, you want to obtain the data or 'all' in order not to filter the month: ").lower().strip()
    while month not in MONTH_DATA:
        print("\nYou provided invalid month. Check spelling and kindly enter the month January to December or 'all' in order not to filter the month")
        month = input("\nEnter which of the month between January to December, you want to obtain the data or 'all' in order not to filter the month: ").lower().strip()

        

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nEnter which of the days in a week, you want to obtain the data or 'all' in order not to filter the day: ").lower().strip()
    while day not in DAY_LIST:
        print("\nYou provided invalid day. Check spelling and kindly enter a day in a week or 'all' in order not to filter the day")
        day = input("\nEnter which of the days in a week, you want to obtain the data or 'all' in order not to filter the day: ").lower().strip()

    
    print('-'*40)
    return city, month, day


# Function to load the required .csv files
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        param1 (str): name of the city to analyze
        param2 (str): name of the month to filter by, or "all" to apply no month filter
        param3 (str): name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df: Pandas DataFrame containing city data filtered by month and day
    """
    #Load data for city
    print("\n Please wait Loading data...\n")
    
    df = pd.read_csv(CITY_DATA[city])    
     
    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month from Start Time to create new column for the month
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    
    #Extract day of week from Start Time to create new column for the days of the week
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
   
    return df


   
# Function for calculating time statistics
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #      display the most common month
    #      Extract hour from Start Time to create new column for the hour
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    common_month = df['month'].mode()[0]
    for months in MONTH_DATA:
        if MONTH_DATA[months]==common_month:
            common_month = months.title()
    print('The most common month is {}'.format(common_month))
    
    

    #     display the most common day of week
    #     Extract hour from Start Time to create new column for the hour
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is: {}'.format(common_day))

    #     display the most common start hour
    #     Extract hour from Start Time to create new column for the hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    common_hour = df['month'].mode()[0]
    print('The most common hour is: {}'.format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #     display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(common_start_station))

    #     display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end station is: {}".format(common_end_station))

    
    #     display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'] + ' to ' + df['End Station']
    start_end_station = df['Start To End'].mode()[0]

    print("\nThe most frequent combination of trips are from {}.".format(start_end_station))

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)   
    
    
    
# Function for calculating trip duration statistics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #     display total travel time
    #     Uses sum method to calculate the total trip duration
    total_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    day =  total_duration.days
    hour = total_duration.seconds // (60*60)
    minute = total_duration.seconds % (60*60) // 60
    second = total_duration.seconds % (60*60) % 60
    print("The total trip duration is {} hours, {} minutes and {} seconds.".format(hour, minute, second))

    
    #     display mean travel time
    mean_total_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    day =  total_duration.days
    hour = total_duration.seconds // (60*60)
    minute = total_duration.seconds % (60*60) // 60
    second = total_duration.seconds % (60*60) % 60
    print("The total trip duration is {} hours, {} minutes and {} seconds.".format(hour, minute, second))


    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)
    
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
#     #     Display counts of user types
#     user_type = df['User Type'].value_counts()
#     print("The types of users by number are:\n".format(user_type))
    
    user_type = df.groupby('User Type',as_index=False).count()
    print("The types of users by number are:\n".format(user_type)) 
    for i in range(len(user_type)):
        print('{}s - {}'.format(user_type['User Type'][i], user_type['Start Time'][i]))

    #     Display counts of gender
    #     Errors are handled here in case data don't have gender column
    try:
#         gender = df['Gender'].value_counts()
#         print("\nThe types of users by gender are given below:\n".format(gender))
        gender = df.groupby('Gender',as_index=False).count()
        print('\nThe types of users by gender are given below: {}'.format(len(gender)))
        for i in range(len(gender)):
            print('{}s - {}'.format(gender['Gender'][i], gender['Start Time'][i]))
        print('Gender data for {} users is not available.'.format(len(df)-gender['Start Time'][0]-gender['Start Time'][1]))
    except:
        print("\nThere is no 'Gender' column in this file.")


    #     Display earliest, most recent, and most common year of birth
    #     The try is used in order to handled errors 
    #     in case data doesn't have birth column
    try:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth is: {}\nThe most recent year of birth is: {}\nThe most common year of birth is: {}".format(earliest_year, recent_year, common_year))
    except:
        print("There are no birth year details in this file.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
    
def display_data(df):
    """Displays first 5 rows of data from the selected csv file
    
        Args:
        (df): The dataframe you decided to work with.
    Returns:
        None.
    """
    
    raw_data = input("\nDo you wish to display the raw data (yes or no?").lower().strip()
#     use index for displaying first 5 lines
    first_index = 0
    end_index = 5
#     use while loop to Continue iterating these prompts and displaying the next 5 lines of raw data if yes
    while raw_data == 'yes' and end_index <= df.size:
        print(df[first_index:end_index])
        first_index = end_index
        end_index +=5
        raw_data = input("\nDo you wish to view more 5 lines of raw data?").lower()
        
    print('-'*40)
     

              
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

