# Package Container Manager

A Python-based package tracking system built using an object-oriented, sorted linked list architecture. 

## Overview

This project manages a dynamic collection of packages, automatically maintaining them in sorted order by owner name (alphabetically) and secondary sorting by weight. It includes complete data tracking for container size, total weight, unique package IDs, and robust search and removal operations.

## Key Features

- **Sorted Linked List Architecture:** Automatically inserts new packages into their correct sorted position upon addition.
- **Flexible Management:** Supports searching and removing packages by ID, owner, or weight.
- **Clean Documentation:** Fully documented with PEP 8 compliant, academic-style docstrings across all classes and methods.

## Quick Start Example

```python 
from container import Container

# Initialize the container
manager = Container()

# Add packages (automatically sorted by owner and weight)
manager.add_package(Container.Package('Apple', 3))
manager.add_package(Container.Package('Cisco', 8))

# Check container stats
print(f"Total Packages: {manager.get_num_packages()}")
print(f"Total Weight: {manager.get_weight()}")
