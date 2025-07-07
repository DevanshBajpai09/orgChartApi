#!/bin/bash
lcov --directory . --capture --output-file coverage.info
genhtml coverage.info --output-directory ../coverage
xdg-open ../coverage/index.html

