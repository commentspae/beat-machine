import itertools
import random
from typing import Iterable, Generator, List, T

import numpy as np
from scipy.signal import resample

from beatmachine.effects.base import LoadableEffect, EffectABCMeta
from beatmachine.beats import Beats

class SubstituteBeats(LoadableEffect, metaclass=EffectABCMeta):
    def __init__(self, *, period: int = 1, offset: int = 0, other: List[np.ndarray]):
        self.period = period
        self.offset = offset
        self.other = other

    def __call__(self, beats: List[np.ndarray]) -> Generator[np.ndarray, None, None]:
        for i, beat in enumerate(beats):
            if i < self.offset:
                yield beat
            else:
                if i % self.period == 0 and (i < len(self.other)):
                    yield self.other[i]
                else:
                    yield beat

class WeaveBeats(LoadableEffect, metaclass=EffectABCMeta):
    def __init__(self, *, dst_sr: int, other: Beats):
        other_beats = list(other.beats)
        self.other = [resample(b, (dst_sr * np.shape(b)[0])//other.sr) for b in other_beats]

    def __call__(self, beats: List[np.ndarray]) -> Generator[np.ndarray, None, None]:
        for i, beat in enumerate(beats):
            yield beat
            if i < len(self.other):
                yield self.other[i]
