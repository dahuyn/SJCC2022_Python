import io
import gladysSatellite as satellite
"""
Student: David Huynh
Module: gladysCompute
Description: This module performs the calculations to figure out the distance between the current position (x,y) and destination postion (x,y) using two formulas.
"""
def gpsAverage(x, y):
"""
document your function definition here. what does it do?
"""
"""
delete the remaining code *in this function* and replace it with
your own code. add more code to do what the assignment asks of you.
"""
value = satellite.gpsValue(5, 6, "altitude")
average = value / 2
return average
def distance(current, destination):
"""
document your function definition here. what does it do?
"""
"""
delete the remaining code *in this function* and replace it with
your own code. add more code to do what the assignment asks of you.
"""
distance = gpsAverage(3, 4)
return distance