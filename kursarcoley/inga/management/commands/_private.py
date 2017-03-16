from oldinga import models as old
from inga import models as inga
from oldinga import models as oldinga
import datetime
import pytz
import sys


class BuildUtil:
    def get_source(self, field, origin):
        if field["type"] == "value":
            value = ""

            if len(field["field_name"]) == 1:
                return getattr(origin, field["field_name"][0])

            for idx, name in enumerate(field["field_name"]):
                value += str(getattr(origin, name))

                if idx < len(field["field_name"]) - 1:
                    value += ", "

            return value

        elif field["type"] == "reference":
            reference_name = field["reference_model"]
            reference_model = getattr(inga, reference_name)

            local_field_name = field["local_field_name"]
            remote_field_name = field["remote_field_name"]

            local_value = getattr(origin, local_field_name)

            return self.wire(reference_model, **{remote_field_name: local_value})

        elif field["type"] == "multireference":
            return "multireference-field";

        elif field["type"] == "date":
            return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

        elif field["type"] == "boolean":
            source_value = getattr(origin, field["field_name"][0]).lower()

            if 'y' in source_value or 'e' in source_value or 's' in source_value:
                return True
            elif 'n' in source_value or 'o' in source_value:
                return False
            else:
                return None


    def build(self, destination_name, mapping):
        destination_model = getattr(inga, destination_name)

        destination_model.objects.all().delete()

        origin_name = mapping["origin"]
        origin_model = getattr(oldinga, origin_name)
        origins = origin_model.objects.all()

        for idx, origin in enumerate(origins):
            if idx % 1000 == 0 or idx == len(origins) - 1:
                print(str(idx) + " objects converted")
            

            for instance in mapping["fields"]:
                destination = destination_model()
                multireference_fields = []

                for field in instance:
                    source_value = self.get_source(instance[field], origin)

                    if source_value == "multireference-field":
                        multireference_fields.append(field);
                    else:
                        setattr(destination, field, source_value)

                destination.save()

                for field in multireference_fields:
                    source_value = self.get_multireference(instance[field], origin)

                destination.save()

            

    def build_date(self, day, month, year):
        return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    def build_date_from_single(self, date):
        return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

    def get_multireference(self, field, origin):
        reference_name = field["reference_model"]
        reference_model = getattr(inga, reference_name)

        local_field_name = field["local_field_name"]
        remote_field_name = field["remote_field_name"]

        local_value = getattr(origin, local_field_name)

        if local_value is None:
            return []

        filter_values = list(filter(None, [x.strip() for x in local_value.split(",")]))

        values = [self.wire(reference_model, **{remote_field_name: filter_value}) for filter_value in filter_values]

        return values;

    def wire(self, model, **kwargs):
        inexact_kwargs = {}

        for key, value in kwargs.items():
            inexact_kwargs[key + "__iexact"] = str(value).strip()
            if (inexact_kwargs[key + "__iexact"] == "Null" or
                    inexact_kwargs[key + "__iexact"] == "None"):
                try:
                    generic = model.objects.get(generic=True)
                except model.DoesNotExist:
                    generic = model()
                    generic.generic = True
                    generic.save()

                return generic

            elif inexact_kwargs[key + "__iexact"] == "":
                new = model()
                new.save()
                return new

        try:
            return model.objects.get(**inexact_kwargs)
        except model.MultipleObjectsReturned:
            return model.objects.filter(**inexact_kwargs)[0]

        except model.DoesNotExist:
            errmsg = "Creating " + model.__name__ + " with the values:\n"

            for arg in kwargs:
                errmsg += "\t" + arg + ": " + str(kwargs[arg]) + "\n"

            print(errmsg, file=sys.stderr)

            new = model(**kwargs)
            new.save()
            return new