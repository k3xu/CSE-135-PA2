# CSE-135-PA1

## Team
* Ivan Luu
* Jonathan Moon
* Kody Xu

**Server user:** grader

**Server password:** password

**SSH Key password:** sshkey

**Site:** [ilvvsion.dev](https://ilvvsion.dev)

## Github Auto Deploy Setup

We used Github hooks to to deploy from Github. This was done by setting up a repository. Our .git
directory is located at '/var/www'. After this was done we edited the  post-commit file with

    #!/bin/bash
    unset GIT_INDEX_FILE
    git --work-tree=/var/www/html --git-dir=$HOME/proj/.git checkout -f


## Username/password info for logging into the site
**Site username:** grader

**Site password:** password

## Changes to HTML file in DevTools after compression

The contents of the file does not appear to change, but the time taken to load
the file decreases significantly.

## Removing \'server\' Header
To change the server header to "CSE 135 Server" we ran these commands:

    $ sudo apt install libapache2-mod-security2
    $ sudo a2enmod security2

After this, we ran this command

    $ sudo vim /etc/apache2/apache2.conf

We then changed/added these lines to the bottom of the configuration file:

    ServerTokens Full

    SecServerSignature “CSE 135 Server”

And then ran this command:

    $ sudo systemctl restart apache2
