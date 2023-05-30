from entity import Buff, Event, Stats


class Conditional(Buff):
    """Conditional modifications to an entity for calculations

    Conditional Buffs represent any change that conditionally change an entity's
    calculations. These behave as normal Buffs, but may apply / remove aspects
    to an entity's stats in certain scenarios. These are resolved before / after
    specific Events occur.

    Examples:
        * Lightcone Dance Dance Dance Action Advances after wearer uses ultimate
        * Character Seele's Ultimate at Eidolon 6 deals extra damage on each hit
        * Character Yanqing's Talent removed upon taking damage
        * Relic Set Guard of Wuthering Snow conditionally heals

    Arguments:
       applied: Boolean for whether the current condition is active.
    """

    ##
    ## Initialization
    ##

    def __init__(
        self, source: Event = None, dispellable: bool = True, turns: Int = None
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the Buff being added to entity.
            applied: Boolean for whether the current condition is active.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.trigger = trigger
        self.applied = False
        super().__init__(source, dispellable, turns)

    ##
    ## Abstract Requirements
    ##

    @abstractmethod
    def event_start(self, event: Event, stats: Stats):
        """If Event starting causes condition to be met, applies buff to state

        Args:
            event: Event that lead to conditional query of Buff.
            stats: Stats for the Buff to act upon.
        """
        pass

    @abstractmethod
    def event_end(self, event: Event, stats: Stats):
        """If Event ending causes condition to be lost, removes buff from state

        Args:
            event: Event that lead to conditional query of Buff.
            stats: Stats for the Buff to act upon.
        """
        pass
