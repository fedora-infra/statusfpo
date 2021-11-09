Title: build systems ( koji, osbs, mbs, src, pdc, kojipkgs, odcs, registry)
Date: 2021-11-09 17:00+0000
OutageFinish: 2021-11-09 21:00+0000
Ticket: 10302

We will be doing several maint tasks during this outage:

    All the s390x builders will be moving from the current z13 maintframe to a z15 mainframe.

    koji hub and builders will be updated from 1.25.1 to 1.26.1

    Updates will be applied to all build servers and reboots done to the latest kernel.

Maintainers are advised to avoid starting builds before the outage that won't complete
before the outage is over. Some builds may restart or need to be resubmitted if
they are running during the maint window. 
