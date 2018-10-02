# Slotted ALOHA simulator

Demonstrates the slot efficiency of the slotted ALOHA protocol.

## Getting started

### Overview

#### Rules

* Nodes transimit new packets according to a Poisson process and retransmit packets after some random time if collision is detected
* Time is slotted, and a packet can only be transmitted at the beginning of the slot
* After transmitting a packet, the node transmits a new packet after a random time offset, regardless of whether the transmission was successful or not
* The random time offset follows the uniform distribution within [0, W)

#### What to simulate

* Simulates N senders for 100,000 time slots
* The slot efficiency is defined as `# of successful slots / # of total slots`
    * `successful slot` means that there is one and only one transmitted packet in the slot
    * No transmission or two or more transmission in a slot is considered not successful
* Implements the slotted ALOHA simulation
* Plots the slot efficiency graph while varying the number of nodes `N` from 1 to 32, with the `window size` 8, 16, 32

### Program Flow

```txt
Each node has a ttl field, to determine its transmission point
```

### Development Environment

```bash
$ uname -a
Linux ubuntu 4.15.0-29-generic #31~16.04.1-Ubuntu SMP Wed Jul 18 08:54:04 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

$ python --version
Python 2.7.12
```

### Prerequisites

To successfully build and run the program, make sure you have the right packages.

```python
import random
import matplotlib.pyplot as plt
```

Install with the following commands.

```bash
sudo apt-get install python-matplotlib
```

## Running the program

### Build

It's a python script. No building required.

### Run

Format

```bash
python aloha.py
```

## Acknowledgements

* [ALOHAnet](https://en.wikipedia.org/wiki/ALOHAnet)
* [Difference between the pure and slotted ALOHA](https://techdifferences.com/difference-between-pure-aloha-and-slotted-aloha.html)

## Authors

* **James Sung** - *Initial work* - [sjkywalker](https://github.com/sjkywalker)
* Copyright © 2018 James Sung. All rights reserved.
