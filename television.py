
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self):
        if self.__status:
            up = self.__channel + 1
            if up > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel = up

    def channel_down(self):
        if self.__status:
            down = self.__channel - 1
            if down < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel = down

    def volume_up(self):
        self.__muted = False
        if self.__status:
            up = self.__volume + 1
            if up > self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME
            else:
                self.__volume = up

    def volume_down(self):
        self.__muted = False
        if self.__status:
            down = self.__volume - 1
            if down < self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume = down

    def __str__(self):
        if self.__muted:
            volume = self.MIN_VOLUME
        else:
            volume = self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}."
