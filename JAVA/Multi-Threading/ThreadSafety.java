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
