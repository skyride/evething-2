EVEthing 2
=========
EVEthing 2 is a terribly named web application intended to ease the pain of managing your [EVE Online](http://www.eveonline.com/) space empire. Based on [EVEthing](https://github.com/madcowfred/evething), EVEthing 2 is major rewrite designed to use the new Swagger-based [ESI](https://community.eveonline.com/news/dev-blogs/introducing-esi/) API, replacing the deprecated [XML API](http://eveonline-third-party-documentation.readthedocs.io/en/latest/xmlapi/) that is set to be switched off on May 2018.

New Features
------------

* Full support for Citadels/Engineering Complexes/etc
* Jump Clones
* Jump Fatigue

Missing Features
----------------
As ESI is still a work-in-progress, EVEthing 2 is currently missing a few features. These will be added as soon as possible, but the ball is entirely in CCP's court.

* Wallet Journal
* Wallet Transactions
* Anything to do with Corporations



Installation
------------
There are some common requirements for any install method, these
will be installed using pip in 'Common Install Steps' below:

- [Python](http://www.python.org) \>=2.7 <3.0
- A MySQL database.
- The current EVE Static Data Export imported into a database. The recommended course is to
  get the SQLite conversion from [fuzzwork](http://www.fuzzwork.co.uk/dump/) and use that as
  your 'import' database. If you can't do that, [zofu](http://zofu.no-ip.de/) has MySQL and
  Postgres versions that take a long, long time to import.

Common Install Steps
--------------------
1.  Make a new virtualenv: `virtualenv thingenv`.
2.  Activate the virtualenv: `cd thingenv`, `source bin/activate`.
3.  Clone the EVEthing git repository:
    `git clone https://github.com/skyride/evething-2.git`.
4.  Install the required libraries using pip: `cd evething`,
    `pip install -r requirements.txt`.
5.  Copy evething/local\_settings.example to evething/local\_settings.py
    then open local\_settings.py in some sort of text editor and edit
    settings.
6.  `python manage.py syncdb`, say NO when it asks if you would like to
    create an admin user.
7.  `python manage.py migrate --all`, this will apply database
    migrations in order.
8.  `python manage.py createsuperuser` to create a new superuser.
9. `python import.py` to import the initial data from the SDE database.

If you update EVEthing in the future, make sure to run
`python manage.py migrate` to apply any database schema changes!

Common Post-install Steps
-------------------------
1.  LEAVE DEBUG ENABLED FOR NOW - it will spit out tracebacks that
    should help you track down any problems.
2.  Log in as the superuser you created earlier.
3.  Click the username dropdown in the top right and head to Account
    Management.
4.  Add one or more Characters.

Celery Worker Setup
-------------------

EVEthing 2 has a much simplified celery task system.
 - et_high: This is used for task spawner jobs.
 - et_medium: This is used for everything else.
 - eth_low: Currently unused.

The current update script has a few deadlock conditions, so I'd avoid starting
more than 4 worker threads. For an easy config, just run this command:

  `celery worker -A evething -B -c 4`

Apache Install
--------------

You will need to install Apache and [mod_wsgi](http://code.google.com/p/modwsgi/).

1. Make a directory somewhere to act as the site root. Do NOT use the same directory you placed the EVEthing
   files earlier.
2. Make a 'static' sub-directory inside this directory.
3. Add a vhost to your Apache config with these extra directives:
  ```
  Alias /static/ /www/whatever/static/

  <Directory /www/whatever>
      Order allow,deny
      Allow from all
  </Directory>

  WSGIDaemonProcess evething threads=2 user=nobody python-path=/path/to/evething:/path/to/virtualenv/lib/python2.7/site-packages
  WSGIProcessGroup evething

  WSGIScriptAlias / /path/to/evething/evething/wsgi.py

  <Directory /path/to/evething>
      <Files wsgi.py>
          Order allow,deny
          Allow from all
     </Files>
  </Directory>
   ```
4. Reload Apache config.
5. Run `python manage.py collectstatic`, answer 'yes'.
6. Open <http://whatever/> in a web browser.
7. To force an EVEthing reload later (updated code or changed config)
   run `touch evething/wsgi.py` in the EVEthing directory.
