#!/bin/bash
cd orgChartApi
mkdir -p build && cd build
cmake .. && make

if [ $? -ne 0 ]; then
  echo "❌ Build Failed"
  cat CMakeFiles/*.log > ../logs/build_logs.txt
  exit 1
else
  echo "✅ Build Succeeded"
  ./runTests
fi
