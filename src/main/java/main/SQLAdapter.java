package main;

import model.Plant;
import model.Site;
import org.hibernate.Session;
import org.hibernate.Transaction;


import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Date;
import java.util.logging.Level;

import static java.util.logging.Level.OFF;

/**
 * Created by Zach Zundel on 4/22/2016.
 */
public class SQLAdapter {
    private static Session session;

    public static void main(String[] args) {
        session = HibernateUtil.getSessionFactory().openSession();
        readPlants();
        session.close();
        HibernateUtil.closeSessionFactory();
    }

    private static void readPlants() {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(OFF);
        ArrayList<Plant> plants = new ArrayList<>();
        ResultSet rs = SQLReader.connectToAndQueryDatabase("SELECT * FROM plant_table LIMIT 10");
        try {
            while (rs.next()) {
                Plant plant = new Plant();
                plant.setId(rs.getInt("id"));
                plant.setDate(parseDate(rs));
                plant.setPlantNumber(rs.getInt("Plant#"));
                plants.add(plant);
            }
        } catch(SQLException e) {
            e.printStackTrace(System.out);
        }

        for(Plant plant : plants) {
            Transaction tx = session.beginTransaction();
            session.save(plant);
            tx.commit();
        }
    }

    private static Date parseDate(ResultSet rs) {
        try {
            int day = rs.getInt("Day");
            String monthString = rs.getString("Month");
            int year = rs.getInt("Year");

            int month = 1;
            switch(monthString) {
                case "Apr":
                    month = 4;
                    break;
                case "Aug":
                case "Augu":
                case "aug":
                case "augu":
                    month = 8;
                    break;
                case "Dec":
                case "Dece":
                    month = 12;
                    break;
                case "Feb":
                case "feb":
                    month = 2;
                    break;
                case "Jul":
                case "July":
                    month = 7;
                    break;
                case "Jun":
                case "June":
                    month = 6;
                    break;
                case "Mar":
                    month = 3;
                    break;
                case "May":
                    month = 5;
                    break;
                case "Nov":
                case "Nove":
                    month = 11;
                    break;
                case "Oct":
                case "Octo":
                case "OCT":
                    month = 10;
                    break;
                case "Sep":
                case "Sept":
                    month = 9;
                    break;
            }

            return new Date(year, month, day);
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return null;
    }
}
