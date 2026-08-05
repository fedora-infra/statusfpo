Title: Migration of fedora-scm-requests from Pagure to Forgejo
Date: 2026-08-05 12:00+0000

The fedora-scm-requests ticket queue is being migrated from pagure.io/releng/fedora-scm-requests
to forge.fedoraproject.org/releng/fedora-scm-requests.

As part of this migration, fedpkg has been updated to file new requests against Forgejo instead
of Pagure. Toddlers, the automation that processes these requests and performs the actual dist-git
operations (creating repositories, branches, handling unretirements), has also been updated to read
from the new location.

During the migration window, filing new requests via fedpkg may be temporarily unavailable.

Please ensure you have updated fedpkg before filing new requests.

For more information about the migration see the tracker ticket:

https://forge.fedoraproject.org/releng/tickets/issues/13108
