Title: koji database upgrade
Date: 2023-06-01 14:30+0000
OutageFinish: 2023-06-01 23:30+0000
Ticket: 11350

We will be moving the koji buildsystem database (and the virthost it runs on) to RHEL9 and postgresql 15 (from RHEL8 and postgresql 12). This outage will happen while the outage of s390x builders is occuring to consolidate outages. During the outage window koji will be unavailable and builds will not be possible. After this outage is over, the s390x builder outage may still be ongoing, so archfull builds may still not complete until that outage is over.
