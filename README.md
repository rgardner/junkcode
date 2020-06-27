# Bob Gardner's Junkcode

This repo stores a collection of small algorithms, scripts, proof-of-concepts,
or just miscellaneous code I've written over the years (submodules may belong
to others).

I was inspired by a blog post or talk sometime in university to start this, but
I don't remember the source. From searching online, maybe it was [this talk by
Andrew Tridgell](https://www.samba.org/ftp/tridge/talks/junkcode.pdf).

## Getting Started

### Prerequisites

1. Optional, set up a Python virtual environment
2. Install the [Invoke](https://www.pyinvoke.org/) task runner
   `pip install invoke`
3. Run `invoke setup`

### Usage

```sh
# See available tasks
invoke --list
# Run on all projects
invoke setup test format lint
```
