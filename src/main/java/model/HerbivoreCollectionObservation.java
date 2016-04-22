package model;

import javax.persistence.*;

/**
 * Created by Zach Zundel on 20.04.2016.
 */

@Entity
public class HerbivoreCollectionObservation {
    @Id
    int id;

    @ManyToOne
    HerbivoreVoucher voucher;
    int herbivores;
    int herbivoresTotal;
    String family;

    public HerbivoreCollectionObservation(int id, HerbivoreVoucher voucher, int herbivores, int herbivoresTotal, String family) {
        this.id = id;
        this.voucher = voucher;
        this.herbivores = herbivores;
        this.herbivoresTotal = herbivoresTotal;
        this.family = family;
    }

    public HerbivoreCollectionObservation() {
        this.id = 0;
        this.voucher = null;
        this.herbivores = 0;
        this.herbivoresTotal = 0;
        this.family = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public HerbivoreVoucher getVoucher() {
        return voucher;
    }

    public void setVoucher(HerbivoreVoucher voucher) {
        this.voucher = voucher;
    }

    public int getHerbivores() {
        return herbivores;
    }

    public void setHerbivores(int herbivores) {
        this.herbivores = herbivores;
    }

    public int getHerbivoresTotal() {
        return herbivoresTotal;
    }

    public void setHerbivoresTotal(int herbivoresTotal) {
        this.herbivoresTotal = herbivoresTotal;
    }

    public String getFamily() {
        return family;
    }

    public void setFamily(String family) {
        this.family = family;
    }
}
