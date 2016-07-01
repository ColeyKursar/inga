package main;

import javax.swing.*;

/**
 * Created by Zach Zundel on 4/28/2016.
 */
public class FormUtil {
    public static double readDouble(JTextField field) throws ImportException{
        try {
            return Double.parseDouble(field.getText());
        } catch (NumberFormatException e) {
            if(field.getText().equals("")) {
                return -1;
            }
            throw new ImportException(field.getName() + " is not a valid typed number.");
        }
    }

    public static double readDouble(JLabel field) throws ImportException{
        try {
            return Double.parseDouble(field.getText());
        } catch (NumberFormatException e) {
            if(field.getText().equals("") || field.getText().equals("Incomplete Data")) {
                return -1;
            }
            throw new ImportException(field.getName() + " is not a valid generated number.");
        }
    }

    public static String readString(JTextField field) {
            return field.getText();
    }

    public static int readInt(JTextField field) throws ImportException{
        try {
            return Integer.parseInt(field.getText());
        } catch (NumberFormatException e) {
            if(field.getText().equals("")) {
                return -1;
            }
            throw new ImportException(field.getName() + " is not a valid integer.");
        }
    }

    public static float readFloat(JTextField field) throws ImportException {
        try {
            return Float.parseFloat(field.getText());
        } catch (NumberFormatException e) {
            if(field.getText().equals("")) {
                return -1;
            }
            throw new ImportException(field.getName() + " is not a valid integer.");
        }
    }
}
