from oldinga import models as old
from inga import models as inga
from oldinga import models as oldinga
import csv
import datetime
import pytz
import sys
import json


def get_source(field, origin):
    """
    Get the data from its indicated source.
    If it's a reference, fetch the reference object.
    """
    if field["type"] == "value":
        value = ""

        for idx, name in enumerate(field["field_name"]):
            temp = getattr(origin, name)

            if temp is not None and isinstance(temp, basestring):
                value += getattr(origin, name).encode('utf-8', 'ignore')

                if field["field_name"] == "chemistry_number" and value != "" and value[0] != "c":
                    value = 'c' + value

                if idx < len(field["field_name"]) - 1:
                    value += ", "
            else:
                return temp

        return value

    elif field["type"] == "reference":
        reference_name = field["reference_model"]
        reference_model = getattr(inga, reference_name)

        local_field_names = field["local_field_name"]
        remote_field_names = field["remote_field_name"]

        params = {}

        for i in range(len(local_field_names)):
            params[remote_field_names[i]] = getattr(origin, local_field_names[i])

        return wire(reference_model, **params)

    elif field["type"] == "multireference":
        return "multireference-field"

    elif field["type"] == "date":
        day = getattr(origin, field["day_field"]) if field["day_field"] else 1
        month = getattr(origin, field["month_field"])if field["month_field"] else 1
        year = getattr(origin, field["year_field"]) if field["year_field"] else 1

        return build_date(day, month, year)

    elif field["type"] == "boolean":
        source_value = getattr(origin, field["field_name"][0]).lower()

        if 'y' in source_value or 'e' in source_value or 's' in source_value:
            return True
        elif 'n' in source_value or 'o' in source_value:
            return False
        else:
            return None


def build(destination_name, mapping):
    """
    Create destination models using the mapping information given
    """
    destination_model = getattr(inga, destination_name)

    destination_model.objects.all().delete()
    universal = {}
    errors = []

    origin_name = mapping["origin"]
    origin_model = getattr(oldinga, origin_name)
    origins = origin_model.objects.all()

    for idx, origin in enumerate(origins):
        try:
            if idx % 1000 == 0 or idx == len(origins) - 1:
                print(str(idx) + " objects converted")

            for field in mapping["universal"]:
                source_value = get_source(mapping["universal"][field], origin)
                universal[field] = source_value

            for instance in mapping["fields"]:
                sources = set()

                destination = destination_model()
                multireference_fields = []

                for field in instance:
                    source_value = get_source(instance[field], origin)

                    if instance[field]["type"] == "value":
                        sources.add(str(source_value) if source_value is not None else None)

                    if source_value == "multireference-field":
                        multireference_fields.append(field)
                    else:
                        if (destination._meta.get_field(field).__class__.__name__ == "IntegerField"
                                and source_value is not None):
                            try:
                                source_value = int(source_value)
                            except ValueError:
                                source_value = None

                        setattr(destination, field, source_value)

                for field in universal:
                    setattr(destination, field, universal[field])

                if len(sources.difference(("0", "", None))) == 0:
                    continue

                destination.save()

                for field in multireference_fields:
                    source_value = get_multireference(instance[field], origin)

                destination.save()
        except ValueError as e:
            error = origin.__dict__
            error["error message"] = e.message
            errors.append(origin.__dict__)

    if len(errors) > 0:
        with open(origin_name + "2" + destination_name + "-errors.csv", "w+") as csvfile:
            fieldnames = [field.name for field in origin_model._meta.get_fields()]
            fieldnames.append("error message")
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            csvwriter.writeheader()
            csvwriter.writerows(errors)

def build_date(day, month, year):
    """
    Build a date object from a day, month, and year strings
    """
    year = int(year) if year is not None else 1
    day = int(day) if day is not None else 1
    month = parse_month(month) if month is not None else 1

    if day < 1:
        day = 1

    if month < 1:
        month = 1

    if year == 0:
        year = 1

    try:
        return datetime.date(year, month, day)
    except ValueError:
        try:
            if month > 1000:
                return datetime.date(month, year, day)
            elif month > 12:
                return datetime.date(year, day, month)
            elif day == 31:
                return datetime.date(year, month, 30)
            else:
                print(year, month, day)
        except ValueError:
            print(year, month, day)


def parse_month(month):
    """
    Interpret a month string
    """

    if str(month).strip() == "":
        return 1

    try:
        return int(month)
    except ValueError:
        if len(month) >= 3:
            if 'jan' in month.lower():
                return 1
            if 'feb' in month.lower():
                return 2
            if 'mar' in month.lower():
                return 3
            if 'apr' in month.lower():
                return 4
            if 'may' in month.lower():
                return 5
            if 'jun' in month.lower():
                return 6
            if 'jul' in month.lower():
                return 7
            if 'aug' in month.lower():
                return 8
            if 'sep' in month.lower():
                return 9
            if 'oct' in month.lower():
                return 10
            if 'nov' in month.lower():
                return 11
            if 'dec' in month.lower():
                return 12

    print("Sorry, but the following month string could not be interpreted: '" + month + "'")
    interpretation = input("Please enter a value for the month: ")
    return int(interpretation)


def get_multireference(field, origin):
    """
    Return multiple models for the multireference fields
    """
    reference_name = field["reference_model"]
    reference_model = getattr(inga, reference_name)

    local_field_name = field["local_field_name"]
    remote_field_name = field["remote_field_name"]

    local_value = getattr(origin, local_field_name)

    if local_value is None:
        return []

    filter_values = list(filter(None, [x.strip() for x in local_value.split(",")]))

    values = [wire(reference_model, **{remote_field_name: filter_value})
              for filter_value in filter_values]

    return values

def trim_references(kwargs):
    trimmed = {}

    for key in kwargs:
        if "__" not in key:
            trimmed[key] = kwargs[key]

    return trimmed

def wire(model, **kwargs):
    """
    Retrieve referenced model and return it.
    If the referenced model cannot be found, it will create a generic model and return that
    If a generic model has been previously created, it will return that.
    """
    inexact_kwargs = {}

    for key in kwargs:
        iexact_key = key + '__iexact'
        inexact_kwargs[iexact_key] = str(kwargs[key]).strip()
        if inexact_kwargs[iexact_key].lower() in ["null", "none"]:
            del inexact_kwargs[iexact_key]
        if key == "chemistry_number" and kwargs[key].lower()[0] != 'c':
            inexact_kwargs[iexact_key] = 'c' + inexact_kwargs[iexact_key]

    if len(inexact_kwargs) == 0:
        print("nothing???")
        print(kwargs)
        print(model)
        return None
    try:
        queryset = model.objects.filter(generic=False, **inexact_kwargs)
        return queryset.get()
    except model.MultipleObjectsReturned:
        print("Multiple " + model.__name__ + " objects returned matching " + json.dumps(kwargs))
        raise ValueError("Multiple " + model.__name__ + " objects returned matching " + json.dumps(kwargs))
    except model.DoesNotExist:
        if "chemistry_number" in kwargs:
            if kwargs["chemistry_number"].lower()[0] == "c":
                inexact_kwargs["chemistry_number__iexact"] = kwargs["chemistry_number"][1:]
            try:
                return model.objects.get(**inexact_kwargs)
            except model.DoesNotExist:
                pass   
        try:
            generic = model.objects.get(generic=True)
            print("Generic found")
        except model.DoesNotExist:
            print("Creating generic")
            generic_args = trim_references(kwargs)
            print(generic_args)
            generic = model(**generic_args)
            generic.generic = True
            generic.save()

        print(generic.__dict__)
        return generic
