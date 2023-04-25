FILE = problem2.c

valgrind:
	gcc $(FILE)
	./a.out
	valgrind --tool=memcheck ./a.out


ASan:
	gcc -fsanitize=address $(FILE)
	ASAN_OPTIONS=detect_stack_use_after_return=1 ./a.out