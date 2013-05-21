def getGlobalStatus(statuses):
    global_status = 0    # 0 = ok, 1 = scheduled, 2 = minor, 3 = major
    for service in statuses.keys():
        status = statuses[service]['status']
        if status == 'scheduled' and global_status < 1:
            global_status = 1
        elif status == 'minor' and global_status < 2:
            global_status = 2
        elif status == 'major' and global_status < 3:
            global_status = 3
    if global_status == 0:
        return 'good'
    elif global_status == 1:
        return 'scheduled'
    elif global_status == 2:
        return 'minor'
    else:
        return 'major'

def getVerboseStatus(global_status):
    if global_status == "good":
        return "All systems go"
    elif global_status == "scheduled":
        return "There are scheduled downtimes in progress"
    elif global_status == "minor":
        return "Minor service disruption"
    elif global_status == "major":
        return "Major service disruption"
