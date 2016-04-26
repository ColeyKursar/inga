package main;

import model.Chemistry;
import model.Extraction;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;

import java.io.*;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

/**
 * Created by Zach Zundel on 4/24/2016.
 */
public class ExtractionParser {
    /*
    public static HashMap<Integer, Extraction> parse(File input, Date date) throws ImportException{
        Iterable<CSVRecord> records = new ArrayList<>();
        HashMap<Integer, ExtractionRecord> result = new HashMap<>();
        try {
            Reader in = new FileReader(input);
            records = CSVFormat.EXCEL.parse(in);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            throw new ImportException("Could not parse CSV file. " + e.getMessage());
        }

        for (CSVRecord record : records) {
            result.put((int)record.getRecordNumber(), new Extraction(record.get("Extraction Number"),
                    new Chemistry().setChemistryNumber(record.get(record.get("Chemistry Number"))), date,
                    record.get("Method"), record.get("Chemist"), record.get("Notebook Number"), record.get("Extraction Notebook Number"),
                    record.get("Page Number"), n));
        }

        return result;
    }*/
}
