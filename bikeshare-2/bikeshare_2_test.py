CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITY_DATA = { 'chicago': r'C:\Users\IRACIC\PycharmProjects\pythonProject\venv\udacity python\Project\bikeshare-2\chicago.csv',
              'new york city': r'C:\Users\IRACIC\PycharmProjects\pythonProject\venv\udacity python\Project\bikeshare-2\new_york_city.csv',
              'washington': r'C:\Users\IRACIC\PycharmProjects\pythonProject\venv\udacity python\Project\bikeshare-2\washington.csv' }
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
    cities = ["chicago", "new york city", "washington"]

    while True:
        city = input(f"Enter a city from list:\n {cities}").title()
        print(f"city:{city}")

        if city.lower() in cities:
            break


    # get user input for month (all, january, february, ... , june)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    while True:
        month = input(f"filter from the following months:\n{months}").title()

        if month.title() in months:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    dayOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    while True:
        day = input(f"filter from the following days:\n{dayOfWeek}").title()

        if day.title() in dayOfWeek:
            break



    print('-'*40)
    return city, month, day

# get_filters()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    #import libraries
    import pandas as pd
    import numpy as np

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    print(df)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df["Start Time"].dt.month_name()
    df['day_of_week'] = df["Start Time"].dt.day_name()

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    # month = input(f"Filter by or 'all', or choose from list of months:\n{months}")

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        # month =  [i+1 for i, j in enumerate(months)]
        month_index =  months.index(month) + 1


        # filter by month to create the new dataframe
        month = month.title()
        # df = df[df['month' == month]]
        df = df[df['month'] ==  month]

        # filter by day of week if applicable
        # if day != 'all':
        # filter by day of week to create the new dataframe
        day = day.title()
        df = df[df['day_of_week'] == day]

    return df

df = load_data('chicago', 'march', 'friday')

