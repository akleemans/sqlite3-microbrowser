# SQLite3 MicroBrowser

Lightweight SQLite3 database browser with Python/Flask and AngularJS.

Just drop your SQLite3 database into the root directory and start `run.sh`, no configuration needed!

[Todo: Screenshot]

## Prerequisites
* [Python](https://www.python.org/), [Flask](http://flask.pocoo.org/): `pip install flask`
* SQLite3
* Optional (for schema diagram): [ERAlchemy](https://github.com/Alexis-benoist/eralchemy) (`pip install eralchemy`)

## How it works

First, the root directory is crawled for a database file (a file with extension 'sqlite', 'sqlite3', 'db3', 'db'). If found, some schema information and a limited amount of rows from each table are fetched and provided via a API to the AngularJS client, which builds a tab for each table and shows the table, along with some options for fetching or column filtering.

## Features
* Drop a SQLite database into this directory, start `run.sh` and browse your database
* Quick overview over database
* Tabs for each table, material design with [Angular material](https://material.angularjs.org)

## Example database

There's a sample database included. To build it from the dump, run `sqlite3 example.db < example_db.sql`.
