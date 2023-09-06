# Meeting Scheduling
This repository contains the code for a Python class that can be used to schedule meetings between two or more people. The class, called `Person`, has the following methods:

* `__init__()`: This method initializes the object and sets the name and timesTable attributes.
* `setWorkingHours()`: This method sets the working hours for the person.
* `addMeeting()`: This method adds a meeting to the person's schedule.
* `removeMeeting()`: This method removes a meeting from the person's schedule.
* `resetTimeTable()`: This method resets the person's schedule to all free time.
* `printTimeTable()`: This method prints the person's schedule.
  
The `Person` class is designed to be used in a modular way.  
Each person has their own schedule, and meetings are scheduled between two or more people's schedules.  
The `Person` class provides methods for adding, removing, and printing meetings, as well as resetting the schedule to all free time.

The `Person` class can be used to schedule meetings between two or more people in a variety of ways.  
```
For example:
you could use the class to schedule meetings between employees in a company, or between students in a school.
```

The class is also flexible enough to be used to schedule meetings between people who are not affiliated with any particular organization.



## Usage
To use the Person class:

1. first create a new instance of `Person` and set the name attribute.
2. Then, use the `setWorkingHours()` method to set the person's working hours.
3. You can then use the `addMeeting()` method to add meetings to the person's schedule.
4. To remove a meeting, use the `removeMeeting()` method.
5. To reset the person's schedule to all free time, use the `resetTimeTable()` method.
6. To print the person's schedule, use the `printTimeTable()` method.

## Here is an example of how to use the Person class:
```
>>> p1 = Person("Mohammad")
>>> p1.setWorkingHours("08:00", "16:00")
>>> p1.addMeeting("09:00", "10:00")
>>> p1.addMeeting("11:00", "12:00")
>>> p1.printTimeTable()

[0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 15, 16, 17]
```
```
This code creates a new instance of Person called p1 and sets its name to "Mohammad".
It then sets the person's working hours to 08:00 to 16:00.
Finally, it adds two meetings to the person's schedule, one from 09:00 to 10:00 and one from 11:00 to 12:00.
The printTimeTable() method then prints the person's schedule, which is all free time except for the two meetings.
```
