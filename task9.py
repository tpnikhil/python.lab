# Student Timetable Conflict Detection

# Timetable: (Subject, Day, Start Time, End Time, Room)

timetable = [
    ("Python", "Monday", 9, 10, "Room 101"),
    ("Maths", "Monday", 10, 11, "Room 102"),
    ("English", "Tuesday", 9, 10, "Room 103")
]

# Unavailable rooms
unavailable_rooms = ["Room 104", "Room 105"]

# Display timetable
print("--- Student Timetable ---")

for course in timetable:
    print(course)

# Check timetable conflicts
conflict = False

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):

        subject1, day1, start1, end1, room1 = timetable[i]
        subject2, day2, start2, end2, room2 = timetable[j]

        # Check time overlap
        if day1 == day2 and start1 < end2 and start2 < end1:
            print("\nTime Conflict:")
            print(subject1, "and", subject2, "have overlapping classes")
            conflict = True

        # Check room availability
        if room1 in unavailable_rooms:
            print("Room unavailable:", room1)
            conflict = True

        if room2 in unavailable_rooms:
            print("Room unavailable:", room2)
            conflict = True

# Final result
print("\n--- Timetable Validation ---")

if conflict:
    print("Timetable is NOT valid")
else:
    print("Timetable is valid")