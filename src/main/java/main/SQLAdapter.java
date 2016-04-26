package main;

import model.Plant;
import model.PlantSpecies;
import model.Site;
import org.hibernate.Session;
import org.hibernate.Transaction;


import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Date;
import java.util.logging.Level;
import java.util.stream.Collector;

import static java.util.logging.Level.OFF;

/**
 * Created by Zach Zundel on 4/22/2016.
 */
public class SQLAdapter {
    private static Session session;

    public static void main(String[] args) {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(OFF);
        session = HibernateUtil.getSessionFactory().openSession();
        readPlants();
        session.flush();
        session.close();
        HibernateUtil.closeSessionFactory();
    }

    private static void readPlants() {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(OFF);
        ResultSet rs = SQLReader.connectToAndQueryDatabase("SELECT * FROM plant_table");
        try {
            while (rs.next()) {
                Plant plant = new Plant();
                plant.setId(rs.getInt("id"));
                plant.setCollectors(rs.getString("collectors"));
                plant.setPlantNumber(rs.getInt("Plant#"));
                plant.setSpecies(parseSpecies(rs.getString("Species_code")));
                Transaction tx = session.beginTransaction();
                session.saveOrUpdate(plant);
                tx.commit();
            }
        } catch(SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    private static PlantSpecies parseSpecies(String species_code) {

        ResultSet rs = SQLReader.connectToAndQueryDatabase("SELECT * FROM species WHERE species_code = \"" + species_code + "\";");
        PlantSpecies species;
        try{
            rs.next();
            Transaction tx = session.beginTransaction();
            species = session.get(PlantSpecies.class, rs.getInt("id"));
            tx.commit();
            if(species != null) {
                return species;
            }
            else {
                species = new PlantSpecies();
                species.setId(rs.getInt("id"));
                species.setOldSpeciesNumber(rs.getString("Old_Species_Number"));
                species.setSpeciesCode(species_code);
                species.setGenus(rs.getString("Genus"));
                species.setSpeciesName(rs.getString("Species_name"));
                species.setComment(rs.getString("comment"));
                species.setAuthority(rs.getString("authority"));
                species.setNoteChemAnal(rs.getString("Note_Chem_Anal"));
                return species;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
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
