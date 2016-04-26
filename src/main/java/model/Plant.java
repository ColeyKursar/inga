package model;

import javax.persistence.*;
import java.util.Date;
import java.util.List;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class Plant {

    @Id
    int id;
    int plantNumber;
    String collectors;
    @ManyToOne(cascade = CascadeType.ALL)
    Site site;
    Date date;

    @ManyToOne(cascade = CascadeType.ALL)
    PlantSpecies species;
    String size;
    String light;
    String height;
    String DBH;
    String LH;
    String DNA;
    Date dateDNASent;

    @ManyToMany(cascade = CascadeType.ALL)
    List<Voucher> vouchers;
    String herbariumSample;
    String flowerColor;
    String description;
    int newLeaves;
    int code;

    public Plant() {
        this.id = 0;
        this.plantNumber = 0;
        this.collectors = null;
        this.site = null;
        this.date = null;
        this.species = null;
        this.size = null;
        this.light = null;
        this.height = null;
        this.DBH = null;
        this.LH = null;
        this.DNA = null;
        this.dateDNASent = null;
        this.vouchers = null;
        this.herbariumSample = null;
        this.flowerColor = null;
        this.description = null;
        this.newLeaves = 0;
        this.code = 0;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getPlantNumber() {
        return plantNumber;
    }

    public void setPlantNumber(int plantNumber) {
        this.plantNumber = plantNumber;
    }

    public String getCollectors() {
        return collectors;
    }

    public void setCollectors(String collectors) {
        this.collectors = collectors;
    }

    public Site getSite() {
        return site;
    }

    public void setSite(Site site) {
        this.site = site;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public PlantSpecies getSpecies() {
        return species;
    }

    public void setSpecies(PlantSpecies species) {
        this.species = species;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public String getLight() {
        return light;
    }

    public void setLight(String light) {
        this.light = light;
    }

    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public String getDBH() {
        return DBH;
    }

    public void setDBH(String DBH) {
        this.DBH = DBH;
    }

    public String getLH() {
        return LH;
    }

    public void setLH(String LH) {
        this.LH = LH;
    }

    public String getDNA() {
        return DNA;
    }

    public void setDNA(String DNA) {
        this.DNA = DNA;
    }

    public Date getDateDNASent() {
        return dateDNASent;
    }

    public void setDateDNASent(Date dateDNASent) {
        this.dateDNASent = dateDNASent;
    }

    public List<Voucher> getVouchers() {
        return vouchers;
    }

    public void setVouchers(List<Voucher> vouchers) {
        this.vouchers = vouchers;
    }

    public String getHerbariumSample() {
        return herbariumSample;
    }

    public void setHerbariumSample(String herbariumSample) {
        this.herbariumSample = herbariumSample;
    }

    public String getFlowerColor() {
        return flowerColor;
    }

    public void setFlowerColor(String flowerColor) {
        this.flowerColor = flowerColor;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public int getNewLeaves() {
        return newLeaves;
    }

    public void setNewLeaves(int newLeaves) {
        this.newLeaves = newLeaves;
    }

    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }
}
