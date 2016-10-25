# Inga Database Manager
This repository contains the data-model and interfacing adapters for all data generated and collected by the Kursar/Coley group in the Department of Biology at the University of Utah.

# Dependencies
The web application is built using the [Django framework](http://djangoproject.org) version 1.10. Documentation for how to create models and work with Django generally can be found there.

# Structure
## Apps
There are four applications in the Django project. Each handles a separate bit of the project.

### inga
This is the main application in the project. It contains the models for the new datamodel and their relations. It also contains the code for the `build` and  `sync` commmands, which are found in its `management/commands` directory. 

### oldinga
This model connects to the old database and provides a programmatic gateway to the old data. This is used to run the `build` and `sync` commands and will be used in the future to allow csv uploads. 

### ingaweb
This is an application that contains the web interface for inga. Currently, that is just the Extraction form, but it can be expanded in the future.

### ingaapi
This is a RESTful API which provides programmatic access to the data contained in the project. 

# Modifying the data model
## Modifying Django models
To modify the Inga datamodel, you must navigate to the application directory and then the `inga` subfolder. Inside, you will see a file called `models.py`. 
Every model begins with the line: `class [ModelName](models.Model):` or `class [ModelName](IngaBase):`. It is advised to use the inga base since that allows for the `updated` time column and synchronization tagging
After the first line, there will be a series of indented lines, one for each column, or field, of the model. The fields are Django model fields, and more information can be found in their documentation. Most lines take the format of `[field name] = models.[FieldType]()`

## Migrating changes to the database
Once you have created all of the models you like, you must migrate them into the database. To do so, use the command line to navigate to the `webapps` directory. (`/var/www/webapps`) and then type the command `. kursarcoleyenv/bin/activate`. Your next command line should be preceded by `(kursarcoleyenv)`. You should now move into the application directory (`/var/www/webapps/kc`) and run the command `sudo python manage.py makemigrations`. This command will scan all of the models files in your project and create any necessary SQL code to push your changes to the database. If this command completes successfully, you should then be able to run `sudo python manage.py migrate` to actually execute the changes in the database. 
