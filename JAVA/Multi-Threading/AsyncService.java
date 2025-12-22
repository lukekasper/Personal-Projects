import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import java.util.concurrent.CompletableFuture;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.task.TaskExecutor;

@Service
public class AsyncService {

    @Async
    public CompletableFuture<String> performAsyncTask() {
        try {
            // Simulate a long-running task
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return CompletableFuture.completedFuture("Task completed");
    }
}


@Service
public class TaskExecutorService {

    @Autowired
    private TaskExecutor taskExecutor;

    public void executeAsyncTask() {
        taskExecutor.execute(() -> {
            System.out.println("Task executed asynchronously using TaskExecutor");
        });
    }
}
