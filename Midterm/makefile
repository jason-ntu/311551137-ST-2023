FILE_NAME := course_scheduling_system_test.py
CACHE := ./__pycache__  .coverage ./htmlcov 

.PHONY: clean

run:
	@coverage run -m unittest $(FILE_NAME)

report: run
	@coverage report -m
	@coverage html

clean:
	@$(RM) -r $(CACHE)