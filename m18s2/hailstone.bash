#!/bin/bash
for i in {1..1000}; do
	echo -n $i " "
	./hailstone5.py $i | grep steps
done
