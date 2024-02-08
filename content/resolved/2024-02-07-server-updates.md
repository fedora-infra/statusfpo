Title: Server updates/reboots
Date: 2024-02-07 22:00+0000
OutageFinish: 2024-02-08 02:00+0000
Ticket: 11754

We will be applying updates and rebooting servers.
No one service should be down long, but may be up and down in the outage window.
Additionally, as time permits we will be doing the following additional work:
* resizing disks on database servers
* moving some database servers to rhel9 and newer postgresql
* applying some firmware updates

21:20 - Unfortunately some updates got applied early to the koji builders,
so builds may be affected and it looks like the outage is starting
early. Sorry for the trouble.

02:00 - all services should be back to normal with the exception
of koji (the fedora buildsystem). We are working to bring it back
online.

Koji is still offline, we will bring it back up as soon as we can.
