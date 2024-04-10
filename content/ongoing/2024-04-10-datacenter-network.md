Title: Network outage in datacenter
Date: 2024-04-10 18:00+0000
OutageFinish: 
Ticket: 

One of our datacenters primary network link is down.
A secondary link is up, but some providers are still
trying to route over the down link, resulting in
connectivity problems.

Affected fedora resources include:

* pagure.io
* download-cc-rdu01

The provider is looking for the outage cause and networking
is working on improving routing to get all traffic to use
the secondary link.
