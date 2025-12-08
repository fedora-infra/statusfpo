Title: rdu2 to rdu3 datacenter move
Date: 2025-12-08 13:00+0000
OutageFinish: 2025-12-09 20:00+0000
Ticket: 12955

We will be powering off hardware in our rdu2 datacenter,
it will be deracked and moved to our rdu3 datacenter,
reracked, and reconfigured for the new network.

retrace/abrt/faf will be down and not accepting user reports
smtp-auth-cc-rdu01 will be down and not accepting emails
download-cc-rdu01 will be down, use another mirror
proxy03/proxy14 will be down, but removed from dns, so no impact.
