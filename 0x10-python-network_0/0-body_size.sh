#!/usr/bin/env bash
curl "$1" -si  | grep -E "Content-Length:\s+(\d*)" | cut -d ' ' -f 2
