import pytest
from television import *


class Test:

    def setup_method(self):
        self.tv_1 = Television()

    def teardown_method(self):
        del self.tv_1

    def test_power(self):
        assert self.tv_1.power() is None

    def test_mute(self):
        assert self.tv_1.mute() is None

    def test_channel_up(self):
        assert self.tv_1.channel_up() is None

    def test_channel_down(self):
        assert self.tv_1.channel_down() is None

    def test_volume_up(self):
        assert self.tv_1.volume_up() is None

    def test_volume_down(self):
        assert self.tv_1.volume_down() is None

    def test_str(self):
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0.'



