# Returns post content to TopPostOnVoat.py

import time

# Post/log files
TOP_POST = [line.rstrip('\n') for line in open('/home/pi/TopPostOnVoat/topPost.txt', 'r')]
LAST_POST = [line.rstrip('\n') for line in open('/home/pi/TopPostOnVoat/lastPost.txt', 'r+b')]
#WRITE_LAST = open('/home/pi/TopPostOnVoat/lastPost.txt', 'r+b')


def main():
    # Sets post content
    title = TOP_POST[0]
    href = TOP_POST[1]
    last = LAST_POST[0]
    
    if href != last:
        # Add current post to duplicate-avoid file
        LAST_POST.write(href)
        # Check char length - twitter max: 140 - shorten title if > 110 char
        if len(title) <= 110:
            status = title + ' - ' +  href
        else:
            status = (title[:110] + '... - ' + href)
    else:
        status = 'null' 

    return status



main()
