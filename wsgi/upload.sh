rm -f status.html
./generate.py >status.html
scp status.html puiterwijk@fedorapeople.org:public_html
scp statuses.json puiterwijk@fedorapeople.org:public_html
rm -f status.html
