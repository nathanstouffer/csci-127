class Date:
    """Date class for representing and manipulating dates"""

    def __init__(self, month, day, year):
        """A constructor method that sets the month, day and year"""
        self.month = month
        self.day = day
        self.year = year

    def get_month(self):
        """A reader method that returns the month"""
        return self.month

    def get_day(self):
        """A reader method that returns the day"""
        return self.day

    def get_year(self):
        """A reader method that returns the year"""
        return self.year

    def set_day(self, day):
        """A writer methods that sets the day"""
        self.day = day
    
# -------------------------------

# Create an instance of Date with the value March 6, 2017
today = Date("October", 18, 2017)
print("Date:", today.get_month(), today.get_day(), today.get_year())

# Update the instance to be one day later
day = today.get_day()
today.set_day(day + 1)
print("Date:", today.get_month(), today.get_day(), today.get_year())
