Title: Ongoing 502 & 503 errors with HTTP endpoints
Date: 2025-11-10 12:00+0000
OutageFinish: 2025-10-08 00:00+0000
Ticket: https://pagure.io/fedora-infrastructure/issue/12814

We have ongoing intermittent issues with the communication between the Fedora
proxies and the backend services. This manifests as intermittent 502 / 503
errors when talking to services such as Koji, Src, and so on.

We are working with the networking team to track it down, see the Pagure ticket
for more detail.

Update: The issue should be resolved for the most part, but there's one 
502 issue still being tracked in https://pagure.io/fedora-infrastructure/issue/12913
