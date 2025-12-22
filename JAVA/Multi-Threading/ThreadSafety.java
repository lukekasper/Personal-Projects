import java.util.concurrent.atomic.AtomicInteger;
// Synchronization
@Service
public class CounterService {
    private int count = 0;
     
    public synchronized void increment() {
        count++;
    }

    public synchronized int getCount() {
        return count;
    }
}


// Atomic Variables
@Service
public class AtomicCounterService {
    private AtomicInteger count = new AtomicInteger(0);

    public void increment() {
        count.incrementAndGet();
    }

    public int getCount() {
        return count.get();
    }
}

// ThreadLocal Variables
public class UserContext {
    private static final ThreadLocal<String> userContext = new ThreadLocal<>();

    public static void setUser(String user) {
        userContext.set(user);
    }

    public static String getUser() {
        return userContext.get();
    }

    public static void clear() {
        userContext.remove();
    }
}

