package main;

import java.sql.*;
import java.util.ArrayList;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class SQLReader {
    public static void main(String args[]) {
        ArrayList<Object> result = connectToAndQueryDatabase("SELECT * FROM plant_table");
        for(Object code : result) {
            System.out.println((String) code);
        }
    }


    public static ArrayList<Object> connectToAndQueryDatabase(String query) {
        ArrayList<Object> result = new ArrayList<>();
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/inga", "root", "");

            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            while(rs.next()) {
                result.add(rs.getString("species_code"));
            }
        } catch(Exception e) {
            e.printStackTrace(System.err);
        }

        return result;
    }
}
