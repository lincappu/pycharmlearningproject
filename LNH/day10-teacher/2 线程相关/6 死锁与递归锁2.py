lock.release()
lock.release()
释放锁的操作连续执行两次，会触发死锁操作，这个时候就需要 rlock，重入锁，
重入锁：acquire 和 release 的个数一定要一致，成对出现