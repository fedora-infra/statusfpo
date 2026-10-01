Title: Fedora Copr outage - updating servers
Date: 2026-10-01 06:00+0000
Ticket: 13597

There will be a Fedora Copr outage while we upgrade infrastructure
machines to the latest Copr packages.

The build queue processing will be stopped during the outage, and the
Frontend/Web-UI will be down most of the time (no new tasks accepted).
The DNF packages and repositories (hosted on copr-backend) will remain
available during this outage.

This outage impacts the
[copr-frontend](https://copr.fedorainfracloud.org).
and the [copr-backend](https://download.copr.fedorainfracloud.org/).
