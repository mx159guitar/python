def room_number():
    number = {"CS101": "3004", "CS102": "4501", "CS103": "6755", "NT110": "1244", "CM241": "1411"}

    return number


def instructor():
    name = {"CS101": "Haynes", "CS102": "Alvarado", "CS103": "Rich", "NT110": "Burke", "CM241": "Lee"}

    return name


def meeting_time():
    time = {"CS101": "800a.m.", "CS102": "9:00a.m.", "CS103": "10:00a.m.", "NT110": "11:00a.m.", "CM241": "1:00p.m."}

    return time


def main():
    course_num = input("Please input a room number: ")
    room = room_number()
    name = instructor()
    time = meeting_time()

    print("Room: ", room.get(course_num))
    print("Room: ", name.get(course_num))
    print("Room: ", time.get(course_num))


main()
