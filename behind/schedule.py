import pandas as pd

classdict = {'THU': ('1 Title', '1 BLDG Venue', '1 Instructor'),
             'WFZ': ('2 Title', '2 BLDG Venue', '2 Instructor'),
             'DE': ('3 Title', '3 BLDG Venue', '3 Instructor')}

monlist = []
tueslist = []
wedlist = []
thurslist = []
frilist = []
satlist = []

# SECTION 1
# Sorting inputted classes into days
for section, course in classdict.items():
    # 1 - 1.5 hour classes
    if section[:2] == 'TH':
        tueslist.append(course[0])
        thurslist.append(course[0])
    elif section[:2] == 'WF':
        wedlist.append(course[0])
        frilist.append(course[0])
    elif section[:1] == 'M':
        monlist.append(course[0])
    elif section[:1] == 'S':
        satlist.append(course[0])
    # 2 hour classes
    elif section[:3] == 'ABC':
        # monday 8-10
        monlist.append(course[0])
    elif section[:2] == 'DE':
        # monday 10-12
        monlist.append(course[0])
    # 3 hour classes
    elif section[:1] == 'A':
        # tuesday 11:30 - 2:30
        tueslist.append(course[0])
    elif section[:1] == 'B':
        # tuesday 8:30 - 11:30
        tueslist.append(course[0])
    elif section[:1] == 'C':
        # W 8:30-11:30AM lab TBA
        wedlist.append(course[0])
    elif section[:1] == 'D':
        # Th 8:30-11:30AM lab TBA
        thurslist.append(course[0])
    elif section[:1] == 'E':
        # F 8:30-11:30AM lab TBA
        frilist.append(course[0])

day = {'Mon': monlist,
       'Tues': tueslist,
       'Wed': wedlist,
       'Thurs': thurslist,
       'Fri': frilist,
       'Sat': satlist}

# SECTION 1.1
# Filtering school days
forpopping = []
for weekday in day:
    if day[weekday] == []:
        forpopping.append(weekday)

for weekend in forpopping:
    day.pop(weekend)



# SECTION 2
# Making the schedule using dict

# SECTION 2.1
# Making a list of active timeslots

classtimes = {}
timeslots = []
for section, course in classdict.items():
    subject = course[0]
    if section[1:] == 'Q':
        # Q 7:00 - 8:30 AM
        classtimes[subject] = ('07:00', '08:30')
        if '07:00' in timeslots:
            pass
        else:
            timeslots.append('07:00')
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
    elif section[2:] == 'R':
        # R 8:30 - 10:00 AM
        classtimes[subject] = ('08:30', '10:00')
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
        if '10:00' in timeslots:
            pass
        else:
            timeslots.append('10:00')
    elif section[2:] == 'U':
        # U 10:00 - 11:30
        classtimes[subject] = ('10:00', '11:30')
        if '10:00' in timeslots:
            pass
        else:
            timeslots.append('10:00')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
    elif section[2:] == 'V':
        # V 11:30 - 1:00 PM
        classtimes[subject] = ('11:30', '13:00')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
        if '13:00' in timeslots:
            pass
        else:
            timeslots.append('13:90')
    elif section[2:] == 'W':
        # W 1:00 - 2:30
        classtimes[subject] = ('13:00', '14:30')
        if '13:00' in timeslots:
            pass
        else:
            timeslots.append('13:00')
        if '14:30' in timeslots:
            pass
        else:
            timeslots.append('14:30')
    elif section[2:] == 'X':
        # X 2:30 - 4:00
        classtimes[subject] = ('14:30', '16:00')
        if '14:30' in timeslots:
            pass
        else:
            timeslots.append('14:30')
        if '16:00' in timeslots:
            pass
        else:
            timeslots.append('16:00')
    elif section[2:] == 'Y':
        # Y 4:00 - 5:30
        classtimes[subject] = ('16:00', '17:30')
        if '16:00' in timeslots:
            pass
        else:
            timeslots.append('16:00')
        if '17:30' in timeslots:
            pass
        else:
            timeslots.append('17:30')
    elif section[2:] == 'Z':
        # Z 5:30 - 7:00
        classtimes[subject] = ('17:30', '19:00')
        if '17:30' in timeslots:
            pass
        else:
            timeslots.append('17:30')
        if '19:00' in timeslots:
            pass
        else:
            timeslots.append('19:00')
    elif section[:3] == 'ABC':
        # monday 8-10
        classtimes[subject] = ('08:00', '10:00')
        if '08:00' in timeslots:
            pass
        else:
            timeslots.append('08:00')
        if '10:00' in timeslots:
            pass
        else:
            timeslots.append('10:00')
    elif section[:2] == 'DE':
        # monday 10-12
        classtimes[subject] = ('10:00', '12:00')
        if '10:00' in timeslots:
            pass
        else:
            timeslots.append('10:00')
        if '12:00' in timeslots:
            pass
        else:
            timeslots.append('12:00')
    # 3 hour classes
    elif section[:1] == 'A':
        # tuesday 11:30 - 2:30
        classtimes[subject] = ('11:30', '14:30')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
        if '14:30' in timeslots:
            pass
        else:
            timeslots.append('14:30')
    elif section[:1] == 'B':
        # tuesday 8:30 - 11:30
        classtimes[subject] = ('08:30', '11:30')
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
    elif section[:1] == 'C':
        # W 8:30-11:30AM lab TBA
        classtimes[subject] = ('08:30', '11:30')
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
    elif section[:1] == 'D':
        # Th 8:30-11:30AM lab TBA
        classtimes[subject] = ('08:30', '11:30')
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
    elif section[:1] == 'E':
        # F 8:30-11:30AM lab TBA
        classtimes[subject] = ('08:30', '11:30')
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
timeslots.sort()

# SECTION 2.2
# Creating the actual dict
schedule = {'Time': timeslots}
for weekday in day:
    orderedclass = []
    for subject in day[weekday]:
        for startctr in range(len(timeslots) - 1):
            if classtimes[subject][0] == timeslots[startctr]:
                orderedclass.append(subject)
                durationctr = startctr + 1
                while timeslots[durationctr] != classtimes[subject][1]:
                    orderedclass.append(subject)
                    durationctr = durationctr + 1
                    startctr = durationctr
            else:
                orderedclass.append('')
            startctr = startctr + 1
    while len(orderedclass) < len(timeslots):
        orderedclass.append('')
    schedule[weekday] = orderedclass


# SECTION 3
# Creating the DataFrame for tabular schedule
if __name__ == "__main__":
    df = pd.DataFrame(schedule)
    df.set_index('Time', inplace=True)
    print(df)

# SECTION 4
# Creating the HTML file for stylized schedule
    htmlfile = open("htmlfile.html", "w+")
    imagepath = '\path\image.jpg' # Image background

    # Styling
    style = 'Light'
    template = open("light.html", "r") if style == 'Light' else open("dark.html", "r") # Different Modes
    htmlfile.write(imagepath.replace('<!--Insert-image-path-here-->', df.to_html())) # Edit image background into html file
    htmlfile.write(template.read().replace('<!--Insert-table-here-->', df.to_html()))
    htmlfile.close()

    # Dimensions: 1080 x 1920
