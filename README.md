This is a proof of concept for a new status.fp.o

### Trying it out

1. ```sudo dnf install pelican python-packaging```
2. ```git clone https://github.com/ryanlerch/status-playground.git```
3. ```cd status-playground```
4. ```make devserver```
5. http://0.0.0.0:8000

### Create a new outage
1. Add a markdown file to the directory in `content/` that is the status of your outage. There are only 3 statuses (planned, resolved, ongoing).
2. Add your outage notice.
```
Title: Bugzilla Slow
Date: 2021-04-28 10:22+0000
OutageFinish: 2021-04-28 13:30+0000
Ticket: 123456

A swarm of bees have taken up residence in one of the Buzilla Server rooms. Consequently, some requests to Bugzilla may respond slower than usual. An apiarist has been called to capture and relocate the swarm.
```
Note that `OutageFinish` is optional.
3. To move an outage, simply move the markdown file into a different status directory in `content/`
