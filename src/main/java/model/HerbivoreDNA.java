package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
@Entity
public class HerbivoreDNA {
    @Id
    int id;
    String DNA;
    @ManyToOne
    HerbivoreVoucher voucher;

    public HerbivoreDNA(int id, String DNA, HerbivoreVoucher voucher) {
        this.id = id;
        this.DNA = DNA;
        this.voucher = voucher;
    }

    public HerbivoreDNA() {
        this.id = 0;
        this.DNA = null;
        this.voucher = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getDNA() {
        return DNA;
    }

    public void setDNA(String DNA) {
        this.DNA = DNA;
    }

    public HerbivoreVoucher getVoucher() {
        return voucher;
    }

    public void setVoucher(HerbivoreVoucher voucher) {
        this.voucher = voucher;
    }
}
