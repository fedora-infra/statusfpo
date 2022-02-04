Title: Migrating Copr Backend to Let's Encrypt certificate
Date: 2022-02-04 14:30+0000
OutageFinish: 2022-02-04 14:45+0000
Ticket: 10512

Copr is going to be migrated from an assigned DigiCert certificate (expires very
soon) to the automated Let's Encrypt certificate.  We expect that some HTTPD
service hiccups can occur, but shouldn't take more then a few minutes.

This outage may affect users who are consuming the content from the Fedora Copr
repositories, e.g. enabled through the "dnf copr" command.

[copr-backend](https://copr-be.cloud.fedoraproject.org/) and
[the CDN](https://download.copr.fedorainfracloud.org/) can be affected.
