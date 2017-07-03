#!/bin/bash
celery worker -A evething -B -c 8
