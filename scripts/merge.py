# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import os


def merge(output):
    with open(output, 'w', encoding='utf-8') as o:
        for file in os.listdir():
            if file.endswith('.csv') and file != output:
                with open(file, encoding='utf-8') as i:
                    i.readline()    # the first row is the header, skipping
                    for line in i:
                        o.write(line)


if __name__ == '__main__':
    merge('poetry.csv')
