classdict = {'1 Title': ('THU', '1 BLDG Venue', '1 Instructor'),
        '2 Title': ('WFU', '2 BLDG Venue', '2 Instructor'),
        '3 Title': ('ABC', '3 BLDG Venue', '3 Instructor')}

print(classdict['1 Title'][1])

monlist = []
tueslist = []
wedlist = []
thurslist = []
frilist = []
satlist = []

# sorting classes into days
for subject in classdict:
    # 1 - 1.5 hour classes
    if classdict[subject][0][:2] == 'TH':
        tueslist.append(subject)
        thurslist.append(subject)
    elif classdict[subject][0][:2] == 'WF':
        wedlist.append(subject)
        frilist.append(subject)
    elif classdict[subject][0][:1] == 'M':
        monlist.append(subject)
    elif classdict[subject][0][:1] == 'S':
        satlist.append(subject)
    # 2 hour classes
    elif classdict[subject][0][:3] == 'ABC':
        # monday 8-10
        monlist.append(subject)
    elif classdict[subject][0][:2] == 'DE':
        # monday 10-12
        monlist.append(subject)
    # 3 hour classes
    elif classdict[subject][0][:1] == 'A':
        # tuesday 11:30 - 2:30
        tueslist.append(subject)
    elif classdict[subject][0][:1] == 'B':
        # tuesday 8:30 - 11:30
        tueslist.append(subject)
    elif classdict[subject[0][:1]] == 'C':
        # W 8:30-11:30AM lab TBA
        wedlist.append(subject)
    elif classdict[subject[0][:1]] == 'D':
        # Th 8:30-11:30AM lab TBA
        thurslist.append(subject)
    elif classdict[subject[0][:1]] == 'E':
        # F 8:30-11:30AM lab TBA
        frilist.append(subject)

day = {'Mon': monlist,
       'Tues': tueslist,
       'Wed': wedlist,
       'Thurs': thurslist,
       'Fri': frilist,
       'Sat': satlist}

print(day)

# creating active times
timeslots = []
for subject in classdict:
    if subject[0][1:] == 'Q':
        # Q 7:00 - 8:30 AM
        if '07:00' in timeslots:
            pass
        else:
            timeslots.append('07:00')
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
    elif classdict[subject][0][1:] == 'R':
        # R 8:30 - 10:00 AM
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
        if '10:00' in timeslots:
            pass
        else:
            timeslots.append('10:00')
    elif classdict[subject][0][1:] == 'U':
        # U 10:00 - 11:30
        if '10:00' in timeslots:
            pass
        else:
            timeslots.append('10:00')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
    elif classdict[subject][0][1:] == 'V':
        # V 11:30 - 1:00 PM
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
        if '13:00' in timeslots:
            pass
        else:
            timeslots.append('13:90')
    elif classdict[subject][0][1:] == 'W':
        # W 1:00 - 2:30
        if '13:00' in timeslots:
            pass
        else:
            timeslots.append('13:00')
        if '14:30' in timeslots:
            pass
        else:
            timeslots.append('14:30')
    elif classdict[subject][0][1:] == 'X':
        # X 2:30 - 4:00
        if '14:30' in timeslots:
            pass
        else:
            timeslots.append('14:30')
        if '16:00' in timeslots:
            pass
        else:
            timeslots.append('16:00')
    elif classdict[subject][0][1:] == 'Y':
        # Y 4:00 - 5:30
        if '16:00' in timeslots:
            pass
        else:
            timeslots.append('16:00')
        if '17:30' in timeslots:
            pass
        else:
            timeslots.append('17:30')
    elif classdict[subject][0][1:] == 'Z':
        # Z 5:30 - 7:00
        if '17:30' in timeslots:
            pass
        else:
            timeslots.append('17:30')
        if '19:00' in timeslots:
            pass
        else:
            timeslots.append('19:00')
    elif classdict[subject][0][:3] == 'ABC':
        # monday 8-10
        if '08:00' in timeslots:
            pass
        else:
            timeslots.append('08:00')
        if '10:00' in timeslots:
            pass
        else:
            timeslots.append('10:00')
    elif classdict[subject][0][:2] == 'DE':
        # monday 10-12
        if '10:00' in timeslots:
            pass
        else:
            timeslots.append('10:00')
        if '12:00' in timeslots:
            pass
        else:
            timeslots.append('12:00')
    # 3 hour classes
    elif classdict[subject][0][:1] == 'A':
        # tuesday 11:30 - 2:30
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
        if '14:30' in timeslots:
            pass
        else:
            timeslots.append('14:30')
    elif classdict[subject][0][:1] == 'B':
        # tuesday 8:30 - 11:30
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
    elif classdict[subject[0][:1]] == 'C':
        # W 8:30-11:30AM lab TBA
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
    elif classdict[subject[0][:1]] == 'D':
        # Th 8:30-11:30AM lab TBA
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')
    elif classdict[subject[0][:1]] == 'E':
        # F 8:30-11:30AM lab TBA
        if '08:30' in timeslots:
            pass
        else:
            timeslots.append('08:30')
        if '11:30' in timeslots:
            pass
        else:
            timeslots.append('11:30')

print(timeslots)

# Further, a class held 7:00-8:00 a.m. Tuesdays and Thursdays has a section of THQ also. A class held 8:00-9:00 a.m. Tuesdays and Thursdays will
# have a section of THQR.
# Finally, a class held 7:00-8:00 a.m. on Wednesdays will have a section of WQ.

# Dimensions: 1080 x 1920