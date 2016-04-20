package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class HerbivorePhotos {
    String photoPath;
    HerbivoreVoucher voucher;

    public HerbivorePhotos(String photoPath, HerbivoreVoucher voucher) {
        this.photoPath = photoPath;
        this.voucher = voucher;
    }

    public HerbivorePhotos() {
        this.photoPath = null;
        this.voucher = null;
    }

    public String getPhotoPath() {
        return photoPath;
    }

    public void setPhotoPath(String photoPath) {
        this.photoPath = photoPath;
    }

    public HerbivoreVoucher getVoucher() {
        return voucher;
    }

    public void setVoucher(HerbivoreVoucher voucher) {
        this.voucher = voucher;
    }
}
