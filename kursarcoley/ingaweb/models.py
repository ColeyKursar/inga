import csv
from io import TextIOWrapper
import json
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
            try:
                for column, value in mapping.items():
                    table, field = value.split('.')
                    if table == self.table:
                        if row[column] != "NULL":
                            setattr(new, field, row[column])
                    else:
                        local, table = table.split(':')
                        external = getattr(inga, table)
                        params = {field: row[column]}
                        external = external.objects.get(**params)
                        setattr(new, local, external)
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
