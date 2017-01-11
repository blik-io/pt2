from time import sleep, time
from random import random, randint, randrange
from numpy import exp, power
from math import pi, sqrt

from .models import DataPoint, Device

class Parameter():
    #The 720 are still very rude but they make the magic work.
    def __init__(self, typical_value, variance, drift=0):
        self.typical_value = typical_value
        self.variance = variance
        self.drift = drift /720      #only chance if you expect drift

class DeviceLatest():
    def __init__(self, device_id, time_stamp, loc_x, loc_y, loc_z, temp, hum, bar, lux):
        self.device_id = device_id
        self.time_stamp = time_stamp
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.loc_z = loc_z
        self.temp = temp
        self.hum = hum
        self.bar = bar
        self.lux = lux

    def __str__(self):
        return "Device %s at TimeStamp %s." % (self.device_id, self.time_stamp)

    def save(self):
        loc = ",".join([str(int(self.loc_x)), str(int(self.loc_y)), str(int(self.loc_z))])
        newdatapoint = DataPoint(device_id=self.device_id, time_stamp=self.time_stamp, loc=loc, temp=self.temp, hum=self.hum, bar=self.bar, lux=self.lux)
        newdatapoint.save()


#Technically speaking, I need more densities for lux and loc
def gaussian(x, expectation=0, variance=1, normalization=True):
    """Tested Gaussian function."""
    if normalization:
        prefactor = (1. / (2.5066282746310002 * variance))
    else:
        prefactor = 1
    return prefactor * exp( - power(x - expectation , 2.) / (2 * power(variance , 2.)))

def selectstep(typical_value=0, variance=1):
    """Selects a random number on the intervall [(ov-3v), (ov+3v)]."""
    return ((random() - 0.5) * (6. * variance)) + typical_value

def createinitialstep(typical_value, variance):
    """Creates a random initial value based on the typical value."""
    return selectstep(typical_value, variance/3.)

def newstep(oldstep, drift, variance):
    """Creates a new step from the old step, in classical random walk manner."""
    step = (((2*random())-1)*variance)+drift
    return oldstep + step

def basicrandwalk(oldstep):
    step = randint(-1,1)
    return oldstep + step

def cyclecount(intervall=0, cycles=[0]):
    """Counts the number of cycles passed and waits for the time specified in the intervall [in seconds]."""
    sleep(intervall)
    cycles[0] += 1
    return cycles

def errorReporting(err):
    """Reports the Error that occurs."""
    print("An error occured: %s." % err)


def randomizer_main():
    """USER VARIABLES"""
    INTERVALL = 2

    loc_x = Parameter(typical_value=0, variance=10, drift=0)
    loc_y = Parameter(typical_value=0, variance=10, drift=0)
    loc_z = Parameter(typical_value=0, variance=10, drift=0)
    temp = Parameter(typical_value=20, variance=1, drift=0)
    hum = Parameter(typical_value=45, variance=4, drift=0)
    bar = Parameter(typical_value=980, variance=10, drift=0)
    lux = Parameter(typical_value=300, variance=75, drift=0)

    device_list = []
    for device in Device.objects.all():
        device_list.append(device.id)

    device_latest_list = []
    for index in device_list:
        device_latest_list.append(DeviceLatest(device_id=index, time_stamp=0, loc_x=loc_x.typical_value, loc_y=loc_y.typical_value, loc_z=loc_z.typical_value, temp=temp.typical_value, hum=hum.typical_value, bar=bar.typical_value, lux=lux.typical_value))

    try:
        #for i in range(1,10):
        while True:
            for device in device_latest_list:
                device.time_stamp = time()
                device.loc_x = newstep(device.loc_x, loc_x.drift, loc_x.variance)
                device.loc_y = newstep(device.loc_y, loc_y.drift, loc_y.variance)
                device.loc_z = newstep(device.loc_z, loc_z.drift, loc_z.variance)
                device.temp = newstep(device.temp, temp.drift, temp.variance)
                device.hum = newstep(device.hum, hum.drift, hum.variance)
                device.bar = newstep(device.bar, bar.drift, bar.variance)
                device.lux = newstep(device.lux, lux.drift, lux.variance)
                device.save()
            cyclecount(INTERVALL)

    except (KeyboardInterrupt, SystemExit):
        print("\nTerminated by KeyboardInterrupt.")
    except Excepkn.efneftion as err:
        errorReporting(err)
        print("error")
    finally:
        return("The loop ran for %s cycles." % cyclecount()[0])
