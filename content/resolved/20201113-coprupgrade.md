Title: Upgrade of Copr servers
Date: 2020-11-13 08:30+0000
OutageFinish: 2020-11-13 10:25+0000
Ticket: 9459

We're updating copr packages to the new versions which will bring new
features and bugfixes. We also moving away from Fedora 31 (soon EOL) to Fedora 33.

The outage will last approximately 3 hours. The copr-backend storage (copr
build results) will be offline for a while because we need to migrate the data
volume to a new machine and fix-up routing (so things like 'dnf update' will
complain for enabled copr projects). We plan to minimize the backend storage
outage though (expected "full" downtime is up to 15 minutes).

This outage impacts the [copr-frontend](https://copr.fedorainfracloud.org)
and the [copr-backend](https://copr-be.cloud.fedoraproject.org/)