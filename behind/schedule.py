import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table

classdict = {'THU': ('1 Title', '1 BLDG Venue', '1 Instructor'),
             'WFZ': ('2 Title', '2 BLDG Venue', '2 Instructor'),
             'DE': ('3 Title', '3 BLDG Venue', '3 Instructor')}

monlist = []
tueslist = []
wedlist = []
thurslist = []
frilist = []
satlist = []

# sorting classes into days
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

# filtering school days
forpopping = []
for weekday in day:
    if day[weekday] == []:
        forpopping.append(weekday)

for weekend in forpopping:
    day.pop(weekend)

classtimes = {}

# creating active times
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

schedule = {'': timeslots}
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


if __name__ == "__main__":
    df = pd.DataFrame(schedule)
    print(df)

    fig, ax = plt.subplots(figsize=(10.8, 19.2)) # set size frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
    tabla = table(ax, df, loc='center', colWidths=[0.175]*len(df.columns))  # where df is your data frame
    tabla.auto_set_font_size(True) # Activate set fontsize manually
    # tabla.set_fontsize(12) # if ++fontsize is necessary ++colWidths
    tabla.scale(1.2, 1.2) # change size table
    plt.savefig('table.png', transparent=True)

    # Dimensions: 1080 x 1920
