Title: Planned outage for OpenShift upgrade
Date: 2024-05-13 08:00+0000
OutageFinish: 
Ticket: 11912

We will be upgrading our production OpenShift cluster that runs many of our applications.
Normally, this would just be a 0 downtime event, but in this case we are switching
networking models, so we need to completely reboot all the nodes,
causing some applications to be unavailable for short time periods.
