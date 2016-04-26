package main;

import com.sun.corba.se.spi.orbutil.fsm.Guard;
import com.sun.rowset.CachedRowSetImpl;

import javax.sql.rowset.CachedRowSet;
import java.sql.*;
import java.util.ArrayList;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class SQLReader {
    public static CachedRowSet connectToAndQueryDatabase(String query) {
        CachedRowSetImpl crs = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
        } catch (Exception e){}

        try (Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/inga?useSSL=false", "root", "")){
            crs = new CachedRowSetImpl();
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            crs.populate(rs);
        } catch(Exception e) {
            e.printStackTrace(System.err);
        }

        return crs;
    }
}
