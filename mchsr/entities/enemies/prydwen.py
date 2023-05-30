import sys
import mchsr.entities.type
import mchsr.buffs.special
import mchsr.events.time

class Decay(mcshr.buffs.special.Conditional):
    """Represents the HP decay of the prydwen theoretical monster

    As the prydwen monster ignores damage and the damage formula is not tuned 
    for such situations, this creates a buff that only reduces the monster's 
    stats at the end of every turn. Due to this occuring at the end of turn,
    resolves slightly different than standard prydwen HP resolution as standard
    is able to add the 75% / 50% / 25% in the middle of a turn. 

    This also resolves the automatic temporary break that occurs at the quarter
    thresholds (75%, 50%, 25%) for 100 av. 
    """

    ##
    ## Initialization
    ##

    def __init__(self, number_cycles : int = 8):
        """Initializes the pyrdwen theoretical monster

        Args:
            number_cycles: Number of cycles prydwen monster will be alive.
        """
        self.max_number_cycles = number_cycles
        self.number_cycles = number_cycles

    ##
    ## Abstract Implementations
    ##

    def apply(self, stats: Stats):
        """Applies specific buff to the state provided"""
        self.applied = true

    def remove(self, stats: Stats):
        """Removes the specific buff from the state provided"""
        self.applied = false

    def event_start(self, event: mchsr.entity.Event, stats: mchsr.entity.Stats):
        """If Event starting causes condition to be met, applies buff to state

        Args:
            event: Event that lead to conditional query of Buff.
            stats: Stats for the Buff to act upon.
        """
        # Ignore all damage taken
        if isinstance(event) == mchsr.events.damage.Take:
            event.damage = 0
            # TODO: Should this be where break resolved?

    def event_end(self, event: mchsr.entity.Event, stats: mchsr.entity.Stats):
        """If Event ending causes condition to be lost, removes buff from state

        Args:
            event: Event that lead to conditional query of Buff.
            stats: Stats for the Buff to act upon.
        """
        # Reduce HP by 1 at end of each turn
        if isinstance(event) == mchsr.events.time.CycleEnd:
            self.number_cycles -= 1
            hp_percent = self.number_cycles / self.max_number_cycles
            stats.curr_hp = stats.max_hp * hp_percent

            # TODO: Figure out how to resolve break at 75%, etc


class Theoretical(mchsr.entity.type.Enemy):
    """Represents the theoretical monster used in pyrdwen's DPS rankings

    Theoretical monster for arbitrary prydwen ranking method. Has unusual Break 
    Bar, no weaknesses, HP that only reduces with fight duration, and very 
    specific stats chosen by Grimro. Useful for looking at a character's DPS in 
    a shared un-optimal situation, allowing comparisons.

    Arguments:
        number_cycles: Number of cycles prydwen monster will be alive.
    """

    def __init__(self, number_cycles : int = 8):
        """Initializes the pyrdwen theoretical monster

        Args:
        """
        # Construct prydwen monster's stats with HP = number_cycles
        self.stats = mchsr.entity.Stats(90, sys.float_info.max, 0, 1000, 0, 0, 0, 0, 0, 0, 0, None) 
        # Create buffs for dealing with special HP reduction 
        decay_buff = Decay(mchsr.events.time.Init(), False)
