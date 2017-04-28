# Inga Database Manager
This repository contains the data-model and interfacing adapters for all data generated and collected by the Kursar/Coley group in the Department of Biology at the University of Utah!

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
