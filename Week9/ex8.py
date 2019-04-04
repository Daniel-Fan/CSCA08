class LightSwitch:
    '''a class representing the status of LightSwitch is on or off'''

    def __init__(self, status):
        '''(LightSwitch, bool) -> NoneType
        Set a new LightSwitch with the status
        REQ: status is True which means 'on', is False which means 'off'
        '''
        self._status = status

    def turn_on(self):
        '''(LightSwitch) -> NoneType
        Turn on the Switch
        '''
        # only turn on the light when light is off
        if(self._status is False):
            self._status = True

    def turn_off(self):
        '''(LightSwitch) -> NoneType
        Turn off the Switch
        '''
        # only turn off the light when light is on
        if(self._status is True):
            self._status = False

    def flip(self):
        '''(LightSwitch) -> NoneType
        Turn off the Switch when it is on
        Turn on the Switch when it is off
        '''
        # if the Switch is off, turn it on
        # if the Switch is on, turn it off
        self._status = not self._status

    def __str__(self):
        '''(LightSwitch) -> str
        return the status of Light
        '''
        # status is False, result is 'off'
        if(self._status is False):
            result = 'off'
        # status is True, result is 'on'
        elif(self._status is True):
            result = 'on'
        # return the result
        return ('I am ' + result)

    def show_status(self):
        '''(LightSwitch) -> bool
        return the self._status
        '''
        return self._status


class SwitchBoard:
    '''a class representing a board control a number of switchlights'''

    def __init__(self, quantity):
        '''(SwitchBoard, int) -> NoneType
        set the number of switchlight that the SwitchBoard contains
        REQ: the switch need to be 'off' at beginning
        '''
        # set index to 0
        index = 0
        # set the quantity of switches
        self._quantity = quantity
        # set an empty list to store LightSwitch
        self._lightswitch = []
        # the element in list is switchlight
        # every switch in the list need to start at 'off'
        while(index < self._quantity):
            # add the lightswitch to list
            self._lightswitch.append(LightSwitch(False))
            # index increases 1
            index += 1

    def __str__(self):
        '''(SwitchBoard) -> str
        return the integers representing the lights which are on
        '''
        # add the following string
        result = 'The following switches are on: '
        # loop every element in self._lightswitch
        for index in range(0, self._quantity):
            # the LightSwitch is on
            if(self._lightswitch[index].show_status() is True):
                # add the index to string
                result += ' ' + str(index)
        return result

    def which_switch(self):
        '''(SwitchBoard) -> list of int
        return a list of integers representing the switches that are on,
        in order
        '''
        # set a new empty list
        switch_on_list = []
        # loop every element in self._lightswitch
        for index in range(0, self._quantity):
            # the LightSwitch is on
            if(self._lightswitch[index].show_status() is True):
                # add the index to list
                switch_on_list.append(index)
        # return the list
        return switch_on_list

    def flip(self, position):
        '''(SwitchBoard, int) -> NoneType
        flip the state of the n'th lightswitch
        REQ: position need to be between 0 and quantity
        '''
        # use the flip method in lightSwitch to change the status
        # the position is not beyond the quantity
        if(position < self._quantity):
            # flip the lightswitch
            self._lightswitch[position].flip()

    def flip_every(self, gap):
        '''(SwitchBoard, int) -> NoneType
        flip the state of every n'th lightswitch, starting at 0
        REQ: gap need to be between 0 and quantity
        '''
        # set the index to 0
        index = 0
        # loop every gap element in self._lightswitch
        # loop when the index is less than quantity
        while(index < self._quantity):
            # use the flip method in lightSwitch to change the status
            self._lightswitch[index].flip()
            # index increase the amount of gap
            index += gap

    def reset(self):
        '''(SwitchBoard) -> NoneType
        turn all switches off
        '''
        # loop every element in self._lightswitch
        for element in self._lightswitch:
            element.turn_off()

if(__name__ == '__main__'):
    # set a switchboard which has 1024 lightswitch
    switchboard = SwitchBoard(1024)
    switchboard.flip(2)
    print(switchboard)
    # loop from step 1 to 1023
    for step in range(1, 1024):
        # flip every number of step lightswitch
        switchboard.flip_every(step)
    print(switchboard.which_switch())
