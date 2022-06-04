#!/usr/bin/env python
import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--path", type=str,
                    required=True,
                    help='path to the .csv')

parser.add_argument("-x", type=str,
                    required=True,
                    help='x axis column name')

parser.add_argument("-y", type=str,
                    required=True,
                    help='y axis column name')

parser.add_argument("--kind", type=str,
                    default="scatter")

if __name__ == '__main__':
    args = parser.parse_args()

    df = pd.read_csv(args.path)

    df.plot(x=args.x,
            y=args.y,
            title=args.y,
            xlabel=args.x,
            ylabel=args.y,
            kind=args.kind)

    plt.show()