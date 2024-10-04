Title: koji upgrades
Date: 2024-10-09 21:00+0000
OutageFinish:
Ticket: 12221

We will be upgrading koji to the latest upstream version,
1.35.0 with various bugfixes and enhancements.

During the outage the koji hubs will be down as the database
schema is updated, and various builders may restart as their
koji version is updated.

Additionally, we will be reinstalling some virthosts with rhel9.
