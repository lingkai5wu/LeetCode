package daily;

public class No622 {
    public static void main(String[] args) {
        MyCircularQueue circularQueue = new MyCircularQueue(6); // 设置长度
        System.out.println(circularQueue.enQueue(6)); // 返回 true
        System.out.println(circularQueue.Rear()); // 返回 6
        System.out.println(circularQueue.Rear()); // 返回 6
    }
}

class MyCircularQueue {
    private int front;
    private int rear;
    private final int capacity;
    private final int[] elements;

    public MyCircularQueue(int k) {
        front = rear = 0;
        capacity = k + 1;
        elements = new int[capacity];
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        elements[rear] = value;
        rear = (rear + 1) % capacity;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        front = (front + 1) % capacity;
        return true;
    }

    public int Front() {
        if (isEmpty()) {
            return -1;
        }
        return elements[front];
    }

    public int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return elements[(rear - 1 + capacity) % capacity];
    }

    public boolean isEmpty() {
        return front == rear;
    }

    public boolean isFull() {
        return ((rear + 1) % capacity) == front;
    }
}