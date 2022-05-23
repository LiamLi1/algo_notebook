package ProducerConsumer;

import java.util.PriorityQueue;
import java.util.Random;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class MainTaskScheduler4 {
    public static void main(String[] args){
        Runnable task = new Runnable(){
            @Override
            public void run(){
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e){
                    e.printStackTrace();
                }
            }
        };

        TaskScheduler4 taskScheduler = new TaskScheduler4();
        for (int i = 0; i < 25; i++){
            Random rand = new Random();
            long waitTime = rand.nextInt(3000);
            taskScheduler.delayRun(waitTime, task);
        }
    }
}


class TaskScheduler4 implements DelayTask4{
    /*
    PriorityQueue<TaskWrapper> pq;

    TaskWrapper -> startTime. pq sorted by startTime.
    private AddTask/PollTask.

    option 1 polling -> not efficient
    option 2 leader follower pattern.
    empty pq, just wait.
    Poll task, if startTime > currentTime,
        if leader is not null, or no task in queue, just await.
        if leader is null, set current thread as leader and awaitNanos(startTime - currentTime)

    Add task, if currentTask == pq.peek(), then set leader as null, signal one waiting thread.
    */

    private PriorityQueue<DelayTaskWrapper> pq;
    private ReentrantLock lock;
    private Condition available;
    private Thread leader;

    public TaskScheduler4(){
        pq = new PriorityQueue<>();
        lock = new ReentrantLock();
        available = lock.newCondition();
        leader = null;
        execute();
    }

    private void execute(){
        Runnable runnable = new Runnable(){
            @Override
            public void run(){
                for (int i = 0; i < 5; i++){
                    DelayTaskWrapper task = pollTask();
                    System.out.println( Thread.currentThread().getName() + " " + task.toString());
                    task.run();
                }
            }
        };
        for (int i = 0; i < 5; i++){
            Thread thread = new Thread(runnable, "Thread" + i);
            thread.start();
        }
    }

    @Override
    public void delayRun(long timeInMillSecondsToDelay, Runnable task){
        DelayTaskWrapper taskWrapper = new DelayTaskWrapper(timeInMillSecondsToDelay, task);
        addTask(taskWrapper);
    }

    private void addTask(DelayTaskWrapper task){
        try {
            lock.lock();
            pq.add(task);
            if (pq.peek() == task){
                // when task is the latest one, reset leader
                leader = null;
                available.signal();
            }
        } finally{
            lock.unlock();
        }
    }

    private DelayTaskWrapper pollTask(){
        try {
            lock.lock();
            for (;;) {
                DelayTaskWrapper first = pq.peek();
                if (first == null) {
                    available.await();
                } else if (leader != null){
                    first = null;
                    available.await();
                } else {
                    long currentTime = System.currentTimeMillis();
                    if (currentTime > first.getStartTime()) {
                        first = null;
                        return pq.poll();
                    }
                    long waitTime = first.getStartTime() - currentTime;
                    first = null;
                    leader = Thread.currentThread();
                    try {
                        available.awaitNanos(waitTime * 1000000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    } finally {
                        leader = null;
                    }
                }
            }
        } catch (InterruptedException e){
            e.printStackTrace();
            return null;
        } finally
         {
             if (leader == null && !pq.isEmpty()){
                 available.signal();
             }
             lock.unlock();
        }
    }
}

class DelayTaskWrapper implements Comparable<DelayTaskWrapper>{
    private long startTime;
    private Runnable task;
    public DelayTaskWrapper(long delayTime, Runnable task) {
        this.task = task;
        startTime = System.currentTimeMillis() + delayTime;
    }

    @Override
    public int compareTo(DelayTaskWrapper task){
        return (int) (this.startTime - task.startTime);
    }

    @Override
    public String toString(){
        return "task startTime:" + this.startTime + " currentTime:" + System.currentTimeMillis();
    }

    public long getStartTime(){
        return this.startTime;
    }

    public void run(){
        task.run();
    }
}

interface DelayTask4{
    public void delayRun(long timeInMillSecondsToDelay, Runnable task);
}