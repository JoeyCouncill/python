
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        This function sets the default instance variables
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self):
        """
        This function turns the television on or off
        :return:
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        """
        This function mutes or unmutes the television when it's on
        :return:
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self):
        """
        This function increases the channel value when the television is on
        :return:
        """
        if self.__status:
            up: int = self.__channel + 1
            if up > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel = up

    def channel_down(self):
        """
        This function decreases the channel value when the television is on
        :return:
        """
        if self.__status:
            down: int = self.__channel - 1
            if down < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel = down

    def volume_up(self):
        """
        This function increases the volume of the television when it's on
        :return:
        """
        self.__muted = False
        if self.__status:
            up: int = self.__volume + 1
            if up > self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME
            else:
                self.__volume = up

    def volume_down(self):
        """
        This function decreases the volume of the television when it's on
        :return:
        """
        self.__muted = False
        if self.__status:
            down: int = self.__volume - 1
            if down < self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume = down

    def __str__(self) -> str:
        """
        :return: a string containing the tvs status, channel, and volume

        """
        if self.__muted:
            volume = self.MIN_VOLUME
        else:
            volume = self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}."
