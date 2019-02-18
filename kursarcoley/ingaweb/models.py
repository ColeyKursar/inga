import csv
from io import TextIOWrapper
import json
import traceback
from django.db import models
import inga.models as inga

class Batch(models.Model):
    input_file = models.FileField(null=True, blank=True)
    table = models.CharField(max_length=100)
    mapping = models.TextField(null=True, blank=True)
    headers = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def process(self):
        mapping = json.loads(self.mapping)
        model = getattr(inga, self.table)
        errors = []

        self.input_file.file.close()
        self.input_file.file.open('rt')
        csvfile = self.input_file.file

        file = csv.DictReader(csvfile)

        for idx, row in enumerate(file):
            if idx % 100 == 0: print(idx)
            new = model()
            fields = set()
            try:
                references = {}
                for column, value in mapping.items():
                    table, field = value.split('.')
                    fields.add(row[column])

                    # If the table is ourself, just set the value
                    if table == self.table:
                        if row[column] not in ["NULL", ""]:
                            setattr(new, field, row[column])
                    else:
                        # Otherwise, we need to add it to our lookup values
                        path, table = table.rsplit(':', 1)
                        path = path.split(":")
                        local = path[0]
                        path = path[1:]
                        path.append(field)                        

                        reference_field = "__".join(path)
                        reference_value = row[column]

                        if "__" not in reference_field:
                            if local in references:
                                references[local]["table"] = table
                            else:
                                references[local] = {
                                    "table": table,
                                    "params": {}
                                }

                        if local in references:
                            references[local]["params"][reference_field] = reference_value
                        else:
                            references[local] = {
                                "params": {
                                    reference_field: reference_value
                                }
                            }
                print(fields)
                if len(fields) == 1 and "" in fields:
                    continue

                for local in references:
                    table = references[local]["table"]
                    params = references[local]["params"]
                    external = getattr(inga, table)
                    reference = external.objects.get(**params)
                    setattr(new, local, reference)

                new.save()
            except Exception as e:
                message = e.__class__.__name__ + ": " + str(e)
                problem = row
                problem["error"] = message
                errors.append(problem)
                continue

        self.complete = True
        self.save()
        self.input_file.close()

        return errors
