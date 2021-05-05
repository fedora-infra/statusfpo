Title: Fedora Packager Dashboard production deployment
Date: 2021-02-02 08:00+0000
OutageFinish: 2021-02-04 12:24+0000
Ticket: 9612

We will be Moving the project from its temporary server to the final, production hosting.

Affected Services include:

* **Fedora Packager Dashboard** - you can use [staging instance](https://packager-dashboard.stg.fedoraproject.org/) for the time being
* **Fedora Easy Karma** - fast pre cached data from bodhi via oraculum won't be available, the app automatically falls back to the old and slow data fetching directly from Bodhi