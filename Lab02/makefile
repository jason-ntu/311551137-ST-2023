FILE_NAME := app_test.py
CACHE := ./__pycache__

.PHONY: clean

run:
	@python3 -m unittest app_test.py 2>/dev/null
	@python3 -m unittest app_test.py -b -v

clean:
	@$(RM) -r $(CACHE)