import main.HibernateUtil;
import model.Plant;
import org.hibernate.*;
import org.hibernate.Transaction;


/**
 * Created by Zach Zundel on 4/22/2016.
 */
public class PersistenceTest {
    public static void main(String[] args) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();
        Plant plant = new Plant();
        session.save(plant);
        tx.commit();
        session.close();
    }
}
