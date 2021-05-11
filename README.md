source and content for [status.fedoraproject.org](https://status.fedoraproject.org)

### Staging Locally

You are able to easily check how status will look with your new or edited outage by running the devserver on your local machine.

1. Install the packages you need to run the devserver with:

    ```sudo dnf install pelican python-packaging```

2. Run the devserver with

    ```make devserver```

3. View the generated site at http://0.0.0.0:8000. Note that any changes to the content and theme will automatically regenerate.

### Create a new outage
1. Add a markdown file to either `content/planned/`, `content/ongoing`, or `content/resolved/`. The name of the file needs to be unique, so check the resolved outages for an idea on how to name your file.
2. Add your outage notice to the markdown file, for example:
```
Title: Buzzilla Slow
Date: 2021-04-28 10:22+0000
OutageFinish: 2021-04-28 13:30+0000
Ticket: 123456

A swarm of bees have taken up residence in one of the Buzzilla Server
 rooms. Consequently, some requests to Buzzilla may respond slower than
 usual. An apiarist has been called to capture and relocate the swarm.
```

* Note that `OutageFinish` is optional, but should really only be ommited if the projected / or actual outage time is unknown.
* When providing dated, keep the timezone offset at +0000 / UTC datetimes

### Moving an Outage
To move an outage, say from **Planned** to **Ongoing** simply move the markdown file into a different status directory in `content/`, and regenerate.

### Publishing
#### Initial Configuration for Publishing
To set up your system for publishing to status.fedoraproject.org, complete the following steps:
1. First, install the AWS command line tool with:

    ```sudo dnf install aws-cli```

2. Grab ```ansible-private/files/aws-status-credentials``` and store in ```~/.aws/credentials```.

3. Run the following command:

    ```aws configure set preview.cloudfront true```

#### Publishing
Once you are satisfied with your changes and how they look on the devserver, commit your changes to Git, and push the built changes live with the command:

```make upload```

Note that this command only updates content changes (i.e. adding / moving outages)

#### Publishing theme changes
If your changes involve changes to the theme, run the following command to upload everything content and theme changes to the live server:

```make upload-theme```

