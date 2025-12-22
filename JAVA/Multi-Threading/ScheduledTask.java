import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class ScheduledTask {

    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("Task executed every 5 seconds");
    }

    @Scheduled(cron = "0 0 12 * * ?")
    public void performTaskAtNoon() {
        System.out.println("Task executed at 12 PM every day");
    }
}
