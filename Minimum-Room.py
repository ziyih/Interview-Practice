"""
Program to find the minimum room to accomodate meetings

@Author: Ziyi Huang

11/30/2018
"""
def min_room_1(meetings):
    """
    approach 1:
        Assume the meetings are given in a dict with the format
            {'meeting_name': ["14:00", "15:00"]}
        A room is a dict that stores the same key-value pairs of the meetings it accomodates
        Use a list to keep track of the rooms allocated
        For each meeting given, traverse all the rooms in the room_list to see if
        it can be accomodated

    """
    room_list = []
    for key in meetings.keys():
        s = meetings[key][0]                # parse the start time
        e = meetings[key][1]                # parse the end time

        # check if there is a room that can accomodate this meeting
        add_room_flag = 1                   # if this flag == 1, a new room is needed
        for room in room_list:
            for key in room.keys():
                s_2 = room[key][0]          # parse the start time
                e_2 = room[key][1]          # parse the end time
                if (later(s, s_2) and ) or not later(s_2, e):
                    # if it ever conflicts with a time here
                    break
            if add_room_flag == 0:
                break
        if add_room_flag == 1:
            room_list.append({})
            room_list[-1][key] = meetings[key]

    return len(room_list)


def later(time1, time2):
    """
    helper function to compare if time1 is not earlier than stime2
    """
    h1 = int(time1.split(":")[0])
    m1 = int(time1.split(":")[1])
    h2 = int(time2.split(":")[0])
    m2 = int(time2.split(":")[1])

    if h1 < h2:
        return False
    elif h1 == h2 and m1 < m2:
        return False
    else:
        return True



if __name__ == "__main__":
    meetings = {"Zhia":["14:00", "16:30"], "Shopping":["13:00", "17:00"]}
    print min_room_1(meetings)
