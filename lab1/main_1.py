#!/usr/bin/env python
# encoding: utf-8

import xml.etree.ElementTree as ET





for car in carArr:
    print("\n" + "\n" + car.name + "\n")
    for model in car.model:
       print(model)