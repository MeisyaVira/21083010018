#!/bin/bash

read n
if ! ((n % 5)); then
    echo "$n divisible by 5."
fi
