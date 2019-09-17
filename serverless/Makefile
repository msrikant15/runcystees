# Makefile for lambda serverless functions

ROOT := .
include $(ROOT)/make-include.mk

lambda:
	$(PYTHON) create_serverless.py

clean:
	rm -f showTeeInfo.zip
	rm -f writeReview.zip
