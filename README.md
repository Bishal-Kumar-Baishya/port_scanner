# Port scanner

A basic TCP port scanner built with python for network reconnaissance

## How to run
- python network_scan.py

## Enter target IP when prompted
- Scans ports 1 to 1024
- Shows only open ports

## Built with
- Python 3
- socket module
- colorama module
- ThreadPoolExecutor module

## Versions
- version 1 - basic sequential scanner
- version 2 - threaded scanner with error handling
- version 3 - threaded scanner with banner grabbing (identifies services on open ports)
- version 4 - thread pool executor with improved banner grabbing and colorized output

## Features (v4)
- Efficient thread pool (max 200 workers) instead of unlimited threads
- Colored output (green for open, red for errors)
- Sends data to trigger responses from services that require input
- Graceful error handling for timeouts, connection resets, and system limits

## Purpose
Build as part of my cybersecurity learning journey to understand TCP connections and network reconnaissance
