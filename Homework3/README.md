
## (a) Draw control flow graphs for all the methods in “Stutter.py”.

Please refer to [Figma](https://www.figma.com/file/wPFlYmCzdQ8XQCkJRHxnNi/Control-Flow-Graph?node-id=0-1&t=8WBDeGVSzS4cO5Ps-0)

## (b) List all the call sites.

| index |    caller    |       callee       |                    callsite                     |
| :---: | :----------: | :----------------: | :---------------------------------------------: |
|   1   |     main     |    Stutter.stut    |              Stutter.stut(inFile)               |
|   2   | Stutter.stut | Stutter.isDelimit  |              Stutter.isDelimit(c)               |
|   3   | Stutter.stut | Stutter.checkDupes | Stutter.checkDupes(linecnt) in inner while loop |
|   4   | Stutter.stut | Stutter.checkDupes | Stutter.checkDupes(linecnt) in outer while loop |

## (c) List all coupling du-pairs for each call site.

1. DU pairs of call site 1:
   1. (main, `inFile = sys.stdin` in no-file case) —— (Stutter.stut, `inLine = inFile.readline()`)
   2. (main, `inFile = sys.stdin` in no-file-name case) —— (Stutter.stut, `inLine = inFile.readline()`)
   3. (main, `inFile = myFile`) —— (Stutter.stut, `inLine = inFile.readline()`)

2. DU pairs of call site 2:
   1. (Stutter.stut, `c = inLine[i]`) —— (Stutter.isDelimit, `if C == Stutter.delimits[i]`)

3. DU pairs of call site 3:
   1. (Stutter.stut, `linecnt = 1`) —— (Stutter.checkDupes, `print('Repeated word on line ', line, ': ', Stutter.prevWord, ' ', Stutter.curWord, sep='')`)
   2. (Stutter.stut, `linecnt += 1`) —— (Stutter.checkDupes, `print('Repeated word on line ', line, ': ', Stutter.prevWord, ' ', Stutter.curWord, sep='')`)

4. DU pairs of call site 4:
   1. (Stutter.stut, `linecnt = 1`) —— (Stutter.checkDupes, `print('Repeated word on line ', line, ': ', Stutter.prevWord, ' ', Stutter.curWord, sep='')`)
   2. (Stutter.stut, `linecnt += 1`) —— (Stutter.checkDupes, `print('Repeated word on line ', line, ': ', Stutter.prevWord, ' ', Stutter.curWord, sep='')`)


## (d) Create test data to satisfy All-Coupling Uses Coverage for “Stutter.py“. (Informally, to cover all coupling du-pairs in (c).)

Test Cases 1, covers 1-1, 2-1, 3-2

``` sh
python3 Stutter.py

apple,apple,
```

Test Cases 2, covers 1-2, 2-1, 4-1

``` sh
python3 Stutter.py ""
apple,apple
```

Test Cases 3, covers 1-3, 2-1, 3-1

``` sh
python3 Stutter.py testData.txt
# The contents of testData.txt is:
# apple,apple,
```

Test Cases 4, covers 1-1, 2-1, 4-2

``` sh
python3 Stutter.py

apple,apple
```
