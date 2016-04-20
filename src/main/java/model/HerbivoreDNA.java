package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class HerbivoreDNA {
    String DNA;
    HerbivoreVoucher voucher;

    public HerbivoreDNA(String DNA, HerbivoreVoucher voucher) {
        this.DNA = DNA;
        this.voucher = voucher;
    }

    public HerbivoreDNA() {
        this.DNA = null;
        this.voucher = null;
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
