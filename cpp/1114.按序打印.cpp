class Foo {
public:
    std::mutex mutex1, mutex2;
    Foo() {
        mutex1.lock();
        mutex2.lock();
    }

    void first(function<void()> printFirst) {
        
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        mutex1.unlock();
    }

    void second(function<void()> printSecond) {
        mutex1.lock();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        mutex2.unlock();
    }

    void third(function<void()> printThird) {
        mutex2.lock();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }

};