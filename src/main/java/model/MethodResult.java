package model;

/**
 * Created by Zach Zundel on 20.04.2016.
 */
public class MethodResult {
    Method method;
    String metric;
    float measurement;

    public MethodResult(Method method, String metric, float measurement) {
        this.method = method;
        this.metric = metric;
        this.measurement = measurement;
    }

    public MethodResult() {
        this.method = null;
        this.metric = null;
        this.measurement = 0;
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
