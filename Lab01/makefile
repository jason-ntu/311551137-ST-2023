FILE_NAME := StudentsTest.py
CACHE := ./__pycache__  .coverage ./htmlcov 

.PHONY: clean

run:
	@coverage run -m unittest $(FILE_NAME)

report: .coverage
	@coverage report
	@coverage html

clean:
	@$(RM) -r $(CACHE)