import com.testhibernate.dao.TestTableEntity;
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import java.util.Iterator;
import java.util.List;

public class Main {
    private static final SessionFactory ourSessionFactory;

    static {
        try {
            ourSessionFactory = new Configuration().configure().buildSessionFactory();
        } catch (Throwable ex) {
            throw new ExceptionInInitializerError(ex);
        }
    }


    public static void main(final String[] args) throws Exception {

    }


    public static void delete() {
        Session session = ourSessionFactory.openSession();
        Transaction transaction = null;
        try {
            transaction = session.beginTransaction();
            TestTableEntity entity = (TestTableEntity) session.get(TestTableEntity.class, 8);
            session.delete(entity);
            transaction.commit();
        } catch (HibernateException ex) {
            if (transaction != null) {
                transaction.rollback();
            }
            ex.printStackTrace();
        } finally {
            session.close();
        }
    }

    public static void update() {
        Session session = ourSessionFactory.openSession();
        Transaction transaction = null;
        try {
            transaction = session.beginTransaction();
            TestTableEntity testTableEntity = (TestTableEntity) session.get(TestTableEntity.class, 6);
            testTableEntity.setPassword("4008111111");
            session.update(testTableEntity);
            transaction.commit();
        } catch (HibernateException ex) {
            if (transaction != null) {
                transaction.rollback();
            }
            ex.printStackTrace();
        } finally {
            session.close();
        }

    }


    public static void list() {
        Session session = ourSessionFactory.openSession();
        Transaction transaction = null;
        try {
            transaction = session.beginTransaction();
            List testList = session.createQuery("FROM TestTableEntity ").list();
            for (Iterator iterator = testList.iterator(); iterator.hasNext(); ) {
                TestTableEntity testTableEntity = (TestTableEntity) iterator.next();
                System.out.println(testTableEntity.getName());
                System.out.println(testTableEntity.getPassword());
                System.out.println("--------");
            }
            transaction.commit();
        } catch (HibernateException e) {
            if (transaction != null) {
                transaction.rollback();
            }
        } finally {
            session.close();
        }
    }

    public static void insert() {
        for (int i = 0; i < 10; i++) {
            Session session = ourSessionFactory.openSession();
            Transaction transaction = null;
            int id = 0;
            try {
                transaction = session.beginTransaction();
                TestTableEntity entity = new TestTableEntity();
                entity.setName("chenzhicheng" + i);
                entity.setPassword("4008123123");
                id = (Integer) session.save(entity);
                transaction.commit();
            } catch (HibernateException ex) {
                if (transaction != null) {
                    transaction.rollback();
                    ex.printStackTrace();
                }
            } finally {
                session.close();
            }
            System.out.println(id);
        }

    }
}