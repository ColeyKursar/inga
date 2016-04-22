package model;

import javax.persistence.Entity;
import javax.persistence.Id;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
@Entity
public class Site {
    @Id
    int siteId;
    String country;
    String latitudeDegrees;
    int latitudeMinutes;
    String longitudeDegrees;
    int longitudeMinutes;
    int altitude;
    double temp;
    int annualRainfall;
    String ranfallSeasonality;
    String rainfallSeasonalityPDFS;
    String soils;
    String soildPDFS;


    public Site(int siteId, String country, String latitudeDegrees, int latitudeMinutes, String longitudeDegrees,
                int longitudeMinutes, int altitude, double temp, int annualRainfall, String ranfallSeasonality,
                String rainfallSeasonalityPDFS, String soils, String soildPDFS) {
        this.siteId = siteId;
        this.country = country;
        this.latitudeDegrees = latitudeDegrees;
        this.latitudeMinutes = latitudeMinutes;
        this.longitudeDegrees = longitudeDegrees;
        this.longitudeMinutes = longitudeMinutes;
        this.altitude = altitude;
        this.temp = temp;
        this.annualRainfall = annualRainfall;
        this.ranfallSeasonality = ranfallSeasonality;
        this.rainfallSeasonalityPDFS = rainfallSeasonalityPDFS;
        this.soils = soils;
        this.soildPDFS = soildPDFS;
    }

    public Site() {
        this.siteId = 0;
        this.country = null;
        this.latitudeDegrees = null;
        this.latitudeMinutes = 0;
        this.longitudeDegrees = null;
        this.longitudeMinutes = 0;
        this.altitude = 0;
        this.temp = 0;
        this.annualRainfall = 0;
        this.ranfallSeasonality = null;
        this.rainfallSeasonalityPDFS = null;
        this.soils = null;
        this.soildPDFS = null;
    }

    public int getSiteId() {
        return siteId;
    }

    public void setSiteId(int siteId) {
        this.siteId = siteId;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getLatitudeDegrees() {
        return latitudeDegrees;
    }

    public void setLatitudeDegrees(String latitudeDegrees) {
        this.latitudeDegrees = latitudeDegrees;
    }

    public int getLatitudeMinutes() {
        return latitudeMinutes;
    }

    public void setLatitudeMinutes(int latitudeMinutes) {
        this.latitudeMinutes = latitudeMinutes;
    }

    public String getLongitudeDegrees() {
        return longitudeDegrees;
    }

    public void setLongitudeDegrees(String longitudeDegrees) {
        this.longitudeDegrees = longitudeDegrees;
    }

    public int getLongitudeMinutes() {
        return longitudeMinutes;
    }

    public void setLongitudeMinutes(int longitudeMinutes) {
        this.longitudeMinutes = longitudeMinutes;
    }

    public int getAltitude() {
        return altitude;
    }

    public void setAltitude(int altitude) {
        this.altitude = altitude;
    }

    public double getTemp() {
        return temp;
    }

    public void setTemp(double temp) {
        this.temp = temp;
    }

    public int getAnnualRainfall() {
        return annualRainfall;
    }

    public void setAnnualRainfall(int annualRainfall) {
        this.annualRainfall = annualRainfall;
    }

    public String getRanfallSeasonality() {
        return ranfallSeasonality;
    }

    public void setRanfallSeasonality(String ranfallSeasonality) {
        this.ranfallSeasonality = ranfallSeasonality;
    }

    public String getRainfallSeasonalityPDFS() {
        return rainfallSeasonalityPDFS;
    }

    public void setRainfallSeasonalityPDFS(String rainfallSeasonalityPDFS) {
        this.rainfallSeasonalityPDFS = rainfallSeasonalityPDFS;
    }

    public String getSoils() {
        return soils;
    }

    public void setSoils(String soils) {
        this.soils = soils;
    }

    public String getSoildPDFS() {
        return soildPDFS;
    }

    public void setSoildPDFS(String soildPDFS) {
        this.soildPDFS = soildPDFS;
    }
}
