import mchsr.entity


class Basic:
    """Basic Event scheduler, for resolving events"""

    ##
    ## Initalization
    ##

    def __init__(self):
        """Initializes the instance based on provided values

        Args:
            entity: Entity executing the current Event.
        """
        self.entity = entity

    ##
    ## Abstract Requirements
    ##

    @abstractmethod
    def resolve(self, event: mcshr.entity.Event):
        """Executes the event on the provided scheduler immediately

        Basic scheduler simply passes event to all buffs to resolve conditional
        buffs due to event starting, executes the event on itself, then passes
        the events to all buffs again to resolve conditional buffs altering due
        to event ending. Fairly unoptimal approach due to having to go through
        every buff on each iteration.

        Args:
            event: Event to immediately execute on the scheduler
        """

        # TODO: Optimize conditional searching

        # Resolve all conditional buffs on this entity due to event start
        for conditional in event.entity.buffs:
            try:
                conditinal.event_start(self, event.entity.stats)
            except:
                continue

        # Immediately execute the provided event
        event.execute(self)

        # Resolve all conditional buffs on this entity due to event end
        for conditional in event.entity.buffs:
            try:
                conditinal.event_end(self, event.entity.stats)
            except:
                continue
