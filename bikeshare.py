import time
import pandas as pd

CITY_DATA= { 'chicago': 'chicago.csv',
               'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    """

    print('Hello! Let\'s explore some US bikeshare data!')

   #Gets user input for city (chicago, new york city, washington) and uses a 'while' loop to handle invalid inputs.
    city = input("Would you like to see data for Chicago, New York City, or Washington?:").title()
    while city not in ('Chicago', 'New York City', 'Washington'):
        print("Please enter a valid answer")
        city = input("Would you like to see data for Chicago, New York City, or Washington?:").title()

    #Gets user input for month (all, january, february, ... , june) and uses a 'while' loop to handle invalid inputs.
    month = input("Which month would you like to see data for? Or type 'all' to see data for all months:").title()
    while month not in ('January', 'February','March','April','May','June','July','All'):
        print("Answer not valid, please try again")
        month = input("Which month would you like to see data for? Or type 'all' to see data for all months:").title()


    #Gets user input for day of week (all, monday, tuesday, ... sunday) and uses a 'while' loop to handle invalid inputs.
    day = input("Which day would you like to see data for? Or type 'all' for every day of the week:").title()
    while day not in ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All'):
        print("Please enter a valid answer")
        day = input("Which day would you like to see data for? Or type 'all' for every day of the week:").title()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    month = month.lower()
    day = day.lower()

    #Loads CSV based on the city, result returned in df.
    df = pd.read_csv(CITY_DATA[city.lower()])

    #Converts string date into datetime format.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Extracts month, day of week, and start hour from Start Time to create new columns.
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    #Filters by month.
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filters by month to create the new dataframe.
        df = df[df['month'] == month]

    #Filters by day of week if applicable.
    if day != 'all':
        #Filters by day of week to create the new dataframe.
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    #Starts tracking the time to process the function.
    start_time = time.time()

    #Display the most common month.
    popular_month = df['month'].mode()[0]
    print('The most common month is {}'.format(popular_month))

    #Displays the most common day of week.
    common_dow = df['day_of_week'].mode()[0]
    print('The most common day of the week is {}'.format(common_dow))

    #Displays the most common start hour.
    common_start_hour = df['start_hour'].mode()[0]
    print('The most common start hour is {}'.format(common_start_hour))

    #Prints out the time the function took to be processed.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    #Starts tracking the time to process the function.
    start_time = time.time()

    #Most frequently used start station.
    most_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(most_start_station))

    #Most frequently used end station.
    most_end_station = df['End Station'].mode()[0]
    print('The most commonly used end stations is: {}'.format(most_end_station))

    #Most frequently used combination of start and end station.
    df['Start and End Station'] = '\nTo start at' + ' ' + df['Start Station'] + ' ' + '\nAnd end at'+ ' ' + df['End Station']
    combined_station = df['Start and End Station'].mode()[0]
    print('The most popular travel combination is: {}'.format(combined_station))

    #Prints out the time the function took to be processed.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Takes the sum of the trip duration.
    total_travel = df['Trip Duration'].sum()
    print('Total trip duration for this is: {}'.format(float(total_travel)))

    #Calculates the average of the trip duration.
    mean_travel = df['Trip Duration'].mean()
    print('Average trip duration is: {}'.format(float(mean_travel)))

    #Prints out the time the function took to be processed.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Takes a count of and groups the user types together.
    user_count = df['User Type'].value_counts()
    print('Total counts for user types are:\n{}'.format(user_count))

    #Catches if Gender is not present in the CSV file
    try:
            #Takes a count of and groups the genders together.
            gender_count = df['Gender'].value_counts()
            print('\nTotal gender counts are:\n{}'.format(gender_count))
    except KeyError:
        pass

    #Catches if birth year is not present in the CSV file.
    try:

        #Takes the minimum, maximum, and most common Birth Year.
            earliest_birth_year = df['Birth Year'].min()
            recent_birth_year = df['Birth Year'].max()
            common_birth_year = df['Birth Year'].mode()[0]
            print('\nThe earliest, recent, and most common birth years are {}, {}, and {} respectively.'.format(int(earliest_birth_year),int(recent_birth_year),int(common_birth_year)))
    except KeyError:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    #Defined variables used for a while loop that takes additional rows depending on user input.
    i = 5
    v = 10
    ldf = len(df)
    #Loops until answer matches 'yes' or 'no'.
    userinput = input('Would you like to see the raw data? (yes/no)').lower()
    while userinput not in('yes','no'):
        print("Please enter 'yes' or 'no'")
        userinput = input('Would you like to see the raw data? (yes/no)').lower()
    #If answer in loop was 'yes', it prints the first 5 rows of data.
    if userinput in('yes'):
        print(df.iloc[0:5,:])
        #Prompts user if they want 5 more rows of data and loops until they answer 'no'.
        while v <= ldf:
            more_rows = input('Would you like to see an additional 5 rows of data? (yes/no)').lower()
            if more_rows in('yes'):
                print(df.iloc[i:v,:])
                i+=5
                v+=5
            else:
                if more_rows in ('no'):
                    break
                else:
                    print('Please enter a valid input')


def main():
    #This calls all the declared functions.
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        #Prompts the user if they want to run this again.
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
