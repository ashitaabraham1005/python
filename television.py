# television.py

class Television:
    ''' Television class is a simple class
    __status: bool = False
    __muted: bool = False
    '''
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
        Initializes the television with power off, channel 0 and volume 0.
        '''

        # Instance variables (private)
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''
        Toggles the power on or off.
        '''
        self.__status = not self.__status

    def mute(self):
        '''
        Mutes the television.
        '''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        '''
        Increases the channel by 1.
        '''
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        '''
        Decreases the channel by 1.
        '''
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self):
        '''
        Increases the volume by 1.
        '''
        if self.__status:
            self.__muted = False  # Unmute if volume is adjusted
            self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)

    def volume_down(self):
        '''
        Decreases the volume by 1.
        '''
        if self.__status:
            self.__muted = False  # Unmute if volume is adjusted
            self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)

    def __str__(self):
        '''
        Returns a string representation of the television.
        '''
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
