import time
import types
from ..events import Event
from inac8hr.anim.sequences import SceneSequence, ControlSequenceGroup, ControlSequence
from inac8hr.anim.easing import EasingBase, LinearEase


class AnimatorBase():

    def __init__(self, duration=1, animation: EasingBase=LinearEase):
        """
            Takes duration in seconds
        """
        self.duration = duration
        self.start_time = time.time()
        self.elapsed = 0
        self.repeat = "cycling"
        self.__animating__ = False

    def get_elapsed(self):
        """
            in seconds
        """
        self.elapsed = time.time() - self.start_time
        return self.elapsed

    def ended(self):
        return self.get_elapsed() >= self.duration


class SceneControlAnimator(AnimatorBase):
    def __init__(self, duration=1, sequences=[]):
        super().__init__()
        self.start_time = time.time()
        self.animations = []
        self.sequences = []
        self.__current_sequence__ = 0

    def add_sequence(self, seq):
        self.sequences.append(seq)
    
    def subscribe_to_sequence(self, sequence, fname: str,
                              handlerfn: types.MethodType):
        setattr(sequence, fname, handlerfn)

    def start(self):
        if len(self.sequences) > 0:
            self.__animating__ = True

    @property
    def current_sequence(self):
        return self.sequences[self.__current_sequence__]
  
    def ended(self):
        return self.get_elapsed() >= self.current_sequence.duration

    def next(self):
        self.__current_sequence__ += 1

    def update(self):
        if self.__animating__:
            alpha_time = self.get_elapsed()
            if not self.ended():
                self.current_sequence.animate(alpha_time)
            else:
                self.current_sequence.end()
                self.__animating__ = False
                if self.current_sequence.start_behaviour == SceneSequence.TIME_CONTROLLED and self.__current_sequence__ != len(self.sequences) - 1:
                    self.__animating__ = True
                    self.start_time = time.time()
                    self.next()


class ControlAnimator(AnimatorBase):
    TIME_DOMAIN = 1
    FRAME_DOMAIN = 2

    def __init__(self, duration=1, sequences=[]):
        super().__init__()
        self.start_time = time.time()
        self.domain = ControlAnimator.TIME_DOMAIN
        self.sequence_groups = []
        self.animated = Event(self)
        self.__current_group__ = 0
        self.time_per_frame = 1/60
        self.__elapsed__ = 0

    def add_sequence(self, seq: ControlSequence):
        """
            Adds an animation sequence of a control to the end of the animation list

            Args:
                seq (ControlSequence): The given sequence
        """
        if self.__animating__:
            return

        if len(self.sequence_groups) == 0:
            seq_group = ControlSequenceGroup(seq.duration)
            seq_group.add_sequence(seq)
            self.sequence_groups.append(seq_group)
        else:
            if seq.timing_start == ControlSequence.WITH_PREVIOUS:
                self.sequence_groups[-1].add_sequence(seq)
            else:
                seq_group = ControlSequenceGroup(seq.duration)
                seq_group.add_sequence(seq)
                self.sequence_groups.append(seq_group)

    def subscribe_to_sequence(self, sequence, fname: str,
                              handlerfn: types.MethodType):
        setattr(sequence, fname, handlerfn)

    def start(self):
        if len(self.sequence_groups) > 0:
            self.__animating__ = True
            self.start_time = time.time()

    def reset(self):
        self.__animating__ = False
        self.__current_group__ = 0
        self.sequence_groups.clear()

    @property
    def current_group(self):
        return self.sequence_groups[self.__current_group__]

    def get_elapsed(self):
        if self.domain == ControlAnimator.TIME_DOMAIN:
            return super().get_elapsed()
        else:
            
            return self.__elapsed__

    def ended(self):
        return self.get_elapsed() >= self.current_group.duration

    def next(self):
        self.__current_group__ += 1

    def update(self):
        if self.__animating__:
            if self.domain == ControlAnimator.FRAME_DOMAIN:
                self.__elapsed__ += self.time_per_frame
            alpha_time = self.get_elapsed()
            if not self.ended():
                self.current_group.animate(alpha_time)
                self.animated(self.current_group)
            else:
                self.current_group.end()
                self.__animating__ = False
                if self.__current_group__ != len(self.sequence_groups) - 1:                  
                    self.__animating__ = True
                    if self.domain == FRAME_DOMAIN:
                        self.__elapsed__ = 0
                    self.start_time = time.time()
                    self.next()
                else:
                    self.sequence_groups.clear()
