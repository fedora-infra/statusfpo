Title: Fedora Copr storage upgrade
Date: 2022-10-28 19:00+0000
OutageFinish: 2022-10-30 14:30+0000
Ticket: 10951

**The performance is degraded**.  If possible, please delay your long-running
builds and larger rebuilds till Sunday evening.

For more info see the [outage schedule](https://docs.google.com/spreadsheets/d/1URopuw2R533H6i4vSTH8Nt47EIhs3ubWcLUXvRcxTRQ/edit#gid=0).

Fedora Copr RPM/DNF/YUM storage needs a major upgrade, we'll need to stop
processing the build queue for about 20 hours, any running builds will be
stopped and restarted on Sunday.

Two full short HTTP (2x5 minutes) outages are planned, too (`dnf update` will
have problems to update anything being hosted in Fedora Copr during these short
periods).

This will affect the [Fedora Copr](https://copr.fedorainfracloud.org/),
especially the [backend part](https://copr-be.cloud.fedoraproject.org/).
