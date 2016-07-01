package main;

import model.Extraction;
import model.ExtractionWeight;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class HibernateUtil {

    private static SessionFactory sessionFactory;

    public static void persistExtraction(Extraction extraction) {
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();
        session.saveOrUpdate(extraction);
        tx.commit();
        session.close();

    }

    public static SessionFactory getSessionFactory() {
        return sessionFactory;
    }

    public static void closeSessionFactory() {
        sessionFactory.close();
    }

    public static void persistExtractionWeights(ExtractionWeight... weights) {
        Session session = sessionFactory.openSession();
        for(ExtractionWeight weight : weights) {
            if(weight.getWeight() == -1) {
                weight.setWeight(0);
            }
            Transaction tx = session.beginTransaction();
            session.saveOrUpdate(weight);
            tx.commit();
        }
        session.close();
    }

    public static void init() {
        try {
            // Create the SessionFactory from hibernate.cfg.xml
            sessionFactory = new Configuration().configure().buildSessionFactory();
        } catch (Throwable ex) {
            // Make sure you log the exception, as it might be swallowed
            System.err.println("Initial SessionFactory creation failed." + ex);
            throw new ExceptionInInitializerError(ex);
        }
    }
}