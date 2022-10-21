Title: Fedora Copr storage upgrade
Date: 2022-10-28 19:00+0000
OutageFinish: 2022-10-30 14:30+0000
Ticket: 10951

Fedora Copr RPM/DNF/YUM storage needs a major upgrade, we'll need to stop
processing the build queue for about 20 hours, and do two short HTTP (2x5
minutes) outages (`dnf update` will have problems to update anything being
hosted in Fedora Copr during this short period).

This will affect the [Fedora Copr](https://copr.fedorainfracloud.org/),
especially the [backend part](https://copr-be.cloud.fedoraproject.org/).
