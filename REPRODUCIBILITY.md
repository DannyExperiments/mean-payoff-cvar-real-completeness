# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay checks 9,826 multiplication tails, 27,000 common-level padding identities, 8,771 binary emission marginal vectors, and 4,200 hinge identities. The grids include ties and endpoints. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/tail-multiplication-explorer.zip) and open index.html to rotate the payoff bars and vary the product inputs. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font parameters. [Build the paper](paper/BUILD.md).
