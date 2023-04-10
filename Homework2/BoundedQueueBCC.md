# Homework 2: Input Space Partitioning for BoundedQueue

Derive input space partitioning test inputs for the BoundedQueue class with the following method signatures:

- BoundedQueue(self, capacity) # The Maximum number of elements
- enqueue(self, o)
- dequeue(self)
- is_empty(self)
- is_full(self)

Assume the usual semantics for a queue with a fixed, maximal capacity. Try to keep your partitioning simple -- choose a small number of partitions and blocks.

#### (a) List all of the input variables, including the (abstract) state variables.

|    Method    |     Params     | Returns |    Values    |  Exception   | Ch ID |    Characteristic     | Covered by |
| :----------: | :------------: | :-----: | :----------: | :----------: | :---: | :-------------------: | :--------: |
| BoundedQueue | state, integer |         |              |              |  C1   |     capacity >= 0     |            |
|              |                |         |              |  ValueError  |       |                       |     C1     |
|   enqueue    | state, object  |         |              |              |  C2   | input non null object |            |
|              |                |         |              |  TypeError   |       |                       |     C2     |
|              |                |         |              | RuntimeError |       |                       |     C4     |
|   dequeue    |     state      | object  | object, null |              |       |                       |   C2, C3   |
|              |                |         |              | RuntimeError |       |                       |     C3     |
|   is_empty   |     state      | boolean | true, false  |              |  C3   |    queue is empty     |            |
|   is_full    |     state      | boolean | true, false  |              |  C4   |     queue is full     |            |

#### (b) Define the characteristics of the input variables. Make sure you cover all input variables.

| Ch ID |    Characteristic     | BoundedQueue | enqueue | dequeue | is_empty | is_full |
| :---: | :-------------------: | :----------: | :-----: | :-----: | :------: | :-----: |
|  C1   |     capacity >= 0     |      v       |    v    |    v    |    v     |    v    |
|  C2   | input non null object |              |    v    |    v    |          |         |
|  C3   |    queue is empty     |              |         |    v    |    v     |         |
|  C4   |     queue is full     |              |    v    |         |          |    v    |

#### (c) Partition the characteristics into blocks. Designate one block in each partition as the "Base" block.

|    Method    | Characteristic | Base  |  Test Requirements   | Infeasible TRs | Revised TRs | # TRs |
| :----------: | :------------: | :---: | :------------------: | :------------: | :---------: | :---: |
| BoundedQueue |       C1       |   T   |        {T, F}        |                |             |   2   |
|   enqueue    |    C1 C2 C4    |  TTF  | {TTF, FTF, TFF, TTT} |      FTF       | FTF -> FFF  |   4   |
|   dequeue    |    C1 C2 C3    |  TTF  | {TTF, FTF, TFF, TTT} |      FTF       | FTF -> FFF  |   4   |
|   is_empty   |     C1 C3      |  TT   |     {TT, FT, TF}     |       FT       |  FT -> FF   |   3   |
|   is_f_ull   |     C1 C4      |  TT   |     {TT, FT, TF}     |       FT       |  FT -> FF   |   3   |

#### (d) Define values for each block.

|    Method    |  C1   |  C2   |  C3   |  C4   | Values                                       |
| :----------: | :---: | :---: | :---: | :---: | :------------------------------------------- |
| BoundedQueue |   T   |       |       |       | BoundedQueue(0)                              |
|              |   F   |       |       |       | BoundedQueue(-1)                             |
|   enqueue    |   T   |   T   |       |   F   | BoundedQueue(1), enqueue("obj1")             |
|              |   F   |   F   |       |   F   | BoundedQueue(-1), enqueue("obj1")            |
|              |   T   |   F   |       |   F   | BoundedQueue(1), enqueue(None)               |
|              |   T   |   T   |       |   T   | BoundedQueue(0), enqueue("obj1")             |
|   dequeue    |   T   |   T   |   F   |       | BoundedQueue(1), enqueue("obj1"), dequeue()  |
|              |   F   |   F   |   F   |       | BoundedQueue(-1), enqueue("obj1"), dequeue() |
|              |   T   |   F   |   F   |       | BoundedQueue(1), enqueue(None), dequeue()    |
|              |   T   |   T   |   T   |       | BoundedQueue(1), dequeue()                   |
|   is_empty   |   T   |       |   T   |       | BoundedQueue(0), is_empty()                  |
|              |   F   |       |   F   |       | BoundedQueue(-1), is_empty()                 |
|              |   T   |       |   F   |       | BoundedQueue(1), enqueue("obj1"), is_empty() |
|   is_full    |   T   |       |       |   T   | BoundedQueue(0), is_full()                   |
|              |   F   |       |       |   F   | BoundedQueue(-1), is_full()                  |
|              |   T   |       |       |   F   | BoundedQueue(1), is_full()                   |
    

#### (e) Define a test set that satisfies Base Choice Coverage (BCC). Write your tests with the values from the previous step. Be sure to include the test oracles.

Check `./BoundedQueueTest.py`
