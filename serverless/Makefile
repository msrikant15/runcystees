# Makefile for lambda serverless functions

ROOT := .
include $(ROOT)/make-include.mk

lambda:
	$(PYTHON) create_serverless.py

clean:
	rm -f showTeeDesc.zip
	rm -f showTeeReviews.zip
	rm -f writeReview.zip
