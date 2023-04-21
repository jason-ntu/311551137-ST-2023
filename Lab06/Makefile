FILE = problem2.c

valgrind:
	gcc $(FILE)
	./a.out
	valgrind --tool=memcheck ./a.out


ASan:
	gcc -fsanitize=address $(FILE)
	./a.out