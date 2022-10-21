Title: Upgrade of Copr servers
Date: 2022-10-28 19:00+0000
OutageFinish: 2022-10-30 14:30+0000
Ticket: 10951

Fedora Copr RPM/DNF/YUM storage needs a major upgrade, we'll need to stop
processing the build queue for a while, and do two short HTTP (2x5 minutes)
outages (`dnf update` will have problems to update anything from copr).

This will affect the [copr service](https://copr.fedorainfracloud.org/),
especially the [copr-backend](https://copr-be.cloud.fedoraproject.org/).
