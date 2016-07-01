package main;

import model.*;
import org.hibernate.Criteria;
import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.criterion.Restrictions;


import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
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
        HibernateUtil.init();
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(OFF);
        session = HibernateUtil.getSessionFactory().openSession();
        readChlorophyll();
        //readSpecies();
        //readPlants();
        //readChemistry();
        session.flush();
        session.close();
        HibernateUtil.closeSessionFactory();
    }

    private static void readChemistry() {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(OFF);
        ResultSet rs = SQLReader.connectToAndQueryDatabase("SELECT * FROM chemistry");
        try {
            while (rs.next()) {
                Chemistry chemistry = new Chemistry();
                chemistry.setId(rs.getInt("id"));
                chemistry.setChemistryNumber(rs.getString("Chem#"));
                chemistry.setPlant(fetchPlant(rs.getInt("Plant#")));
                chemistry.setDate(parseDate(rs));
                chemistry.setSize(rs.getString("size"));
                chemistry.setLight(rs.getString("light"));
                chemistry.setExpMin(rs.getString("Exp_Min"));
                chemistry.setExpMax(rs.getString("Exp_Max"));
                chemistry.setHeight(rs.getDouble("Height"));
                chemistry.setDBH(rs.getString("DBH"));
                chemistry.setFWg(rs.getString("FWg"));
                chemistry.setAge(rs.getString("Age"));
                chemistry.setUse(rs.getString("Use"));
                chemistry.setCur_w(rs.getDouble("cur_w"));
                chemistry.setVial_w(rs.getDouble("vial_w"));
                chemistry.setUnusedMaterial(rs.getDouble("Unnused_Materialg"));
                chemistry.setBoxNumber(rs.getString("Box#"));
                chemistry.setNumberPlants(rs.getString("#_of_plants"));
                chemistry.setNotes(rs.getString("Notes10") +", " + rs.getString("Notes12") + ", " + rs.getString("Notes13"));
                chemistry.setStatus(rs.getString("Status"));
                chemistry.setExtracted(rs.getString("Extracted"));
                Transaction tx = session.beginTransaction();
                session.saveOrUpdate(chemistry);
                tx.commit();
            }
        } catch(SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    private static void readSpecies() {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(OFF);
        ResultSet rs = SQLReader.connectToAndQueryDatabase("SELECT * FROM species");
        try {
            while (rs.next()) {
                PlantSpecies species = new PlantSpecies();
                species.setId(rs.getInt("id"));
                species.setOldSpeciesNumber(rs.getString("Old_Species_Number"));
                species.setSpeciesCode(rs.getString("species_code"));
                species.setGenus(rs.getString("Genus"));
                species.setSpeciesName(rs.getString("Species_name"));
                species.setComment(rs.getString("comment"));
                species.setAuthority(rs.getString("authority"));
                species.setNoteChemAnal(rs.getString("Note_Chem_Anal"));
                Transaction tx = session.beginTransaction();
                session.saveOrUpdate(species);
                tx.commit();
            }
        } catch(SQLException e) {
            e.printStackTrace(System.out);
        }
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
                plant.setSpecies(fetchSpecies(rs.getString("Species_code")));
                plant.setDate(parseDate(rs));
                plant.setSize(rs.getString("size"));
                plant.setLight(rs.getString("light"));
                plant.setHeight(rs.getString("Height"));
                plant.setDBH(rs.getString("DBH"));
                plant.setLH(rs.getString("LH"));
                plant.setDNA(rs.getString("DNA"));
                plant.setHerbariumSample(rs.getString("herbarium_sample"));
                plant.setFlowerColor(rs.getString("flower_color"));
                plant.setDescription(rs.getString("description"));
                plant.setNewLeaves(rs.getInt("New_Leaves"));
                plant.setCode(rs.getInt("code"));
                Transaction tx = session.beginTransaction();
                session.saveOrUpdate(plant);
                tx.commit();
            }
        } catch(SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    private static PlantSpecies fetchSpecies(String speciesCode) {
        Criteria criteria = session.createCriteria(PlantSpecies.class);
        return (PlantSpecies) criteria.add(Restrictions.eq("speciesCode", speciesCode)).list().get(0);
    }

    private static Plant fetchPlant(int plantNumber) {
        Criteria criteria = session.createCriteria(Plant.class);
        return (Plant) criteria.add(Restrictions.eq("plantNumber", plantNumber)).list().get(0);
    }

    private static void readChlorophyll() {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(OFF);
        ResultSet rs = SQLReader.connectToAndQueryDatabase("SELECT * FROM chlorophyll");
        try {
            while (rs.next()) {
                ResultSetMetaData rsmd = rs.getMetaData();
                int count = rsmd.getColumnCount();
                for(int i = 1; i < count; i++) {
                    System.out.println("|" + rsmd.getColumnName(i) + "|");
                }
                Chlorophyll chlorophyll = new Chlorophyll();
                chlorophyll.setChl_mg_dm2(rs.getDouble("Chl_mg/dm2"));
                chlorophyll.setChlorophyllId(rs.getInt("id"));
                chlorophyll.setDate(parseDate(rs));
                chlorophyll.setLight(rs.getString("light"));
                chlorophyll.setNotes(rs.getString("Notes"));
                chlorophyll.setPercentExposed(rs.getInt("%exp"));
                chlorophyll.setSize(rs.getString("size"));
                chlorophyll.setSpadd(rs.getInt("Spadd"));
                chlorophyll.setPlant(fetchPlant(rs.getInt("Plant#")));
                Transaction tx = session.beginTransaction();
                session.saveOrUpdate(chlorophyll);
                tx.commit();
            }
        } catch(SQLException e) {
            e.printStackTrace(System.out);
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
