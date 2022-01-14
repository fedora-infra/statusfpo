Title: Datanommer Migration
Date: 2022-01-17 11:00+0000
OutageFinish: 2022-01-17 13:00+0000
Ticket: 10476

We are making some improvements to the performance of the Datanommer database
including adding the Timescaledb plugin, a migration to a new database was
required as this involved some breaking changes, the migration has already taken
place but the required apps will now be required to point to the new database

Datanommer/Datagrepper and any service which interacts with these will be
affected
