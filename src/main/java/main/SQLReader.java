package main;

import java.sql.*;
import java.util.ArrayList;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class SQLReader {
    public static ResultSet connectToAndQueryDatabase(String query) {
        ResultSet rs = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/inga", "root", "");

            Statement stmt = con.createStatement();
            rs = stmt.executeQuery(query);


        } catch(Exception e) {
            e.printStackTrace(System.err);
        }

        return rs;
    }
}
