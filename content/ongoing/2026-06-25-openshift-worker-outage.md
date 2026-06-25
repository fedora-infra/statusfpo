Title: Partial Outage - 2 of 5 Openshift workers down
Date: 2026-06-25 11:00+0000
OutageFinish: 
Ticket: 13419

Some hosts are being relocated and have been taken down for that purpose. OCP
workers 04 and 05 are on the list.

While this should have been transparent to end users, it has caused unforseen
consequences with the Apache LoadBalancer setup for Openshift Apps, when
requests mistakenly get sent to the down workers. We're investigating why
Apache is not correctly removing them from the pool, but for now there ill be
some failed page-loads for the Forge, Bodhi, etc.
