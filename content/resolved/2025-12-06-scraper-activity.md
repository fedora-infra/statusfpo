Title: src.fedoraproject.org access degraded
Date: 2025-12-06 16:30+0000
OutageFinish: 2025-12-06 18:00+0000
Ticket: 12964

There is heavy scraper activity cauing high load and slow load times
on https://src.fedoraproject.org.

We are investigating and trying to mitigate it.

The issue was scrapers hitting /history/ and /blame/ endpoints recursively.
We have at least for now blocked those endpoints. Please git clone locally
if you need to run those things.
