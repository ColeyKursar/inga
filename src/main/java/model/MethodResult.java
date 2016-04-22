package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

/**
 * Created by Zach Zundel on 20.04.2016.
 */
@Entity
public class MethodResult {
    @Id
    int id;
    @ManyToOne
    Method method;
    String metric;
    float measurement;

    public MethodResult(int id, Method method, String metric, float measurement) {
        this.id = id;
        this.method = method;
        this.metric = metric;
        this.measurement = measurement;
    }

    public MethodResult() {
        this.id = 0;
        this.method = null;
        this.metric = null;
        this.measurement = 0;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Method getMethod() {
        return method;
    }

    public void setMethod(Method method) {
        this.method = method;
    }

    public String getMetric() {
        return metric;
    }

    public void setMetric(String metric) {
        this.metric = metric;
    }

    public float getMeasurement() {
        return measurement;
    }

    public void setMeasurement(float measurement) {
        this.measurement = measurement;
    }
}
