import mchsr.entity


class Ally(mchsr.entity.Entity):
    """Represents an entity (often user controlled) allied with user"""

    ##
    ## Abstract Requirements
    ##

    @abstractmethod
    def basic(self, selector) -> mchsr.events.attack.Basic:
        """Represents the basic usage of the Ally

        Basic action of the Ally. This property should be an Event that can be
        resolved on the Scheduler.

        Args:
            selector: Selector to aid selection of targets.
        """
        pass

    @abstractmethod
    def skill(self, selector, sp: int = 1) -> mchsr.events.attack.Skill:
        """Represents the skill usage of the Ally

        Skill action of the Ally. This property should be an Event that can be
        resolved on the Scheduler.

        Args:
            selector: Selector to aid selection of targets.
            sp: Number of skill points available, for multi-sp skills.
        """
        pass

    @abstractmethod
    def ult(self, selector) -> mchsr.events.attack.Ult:
        """Represents the ult usage of the Ally

        Ult action of the Ally. This property should be an Event that can be
        resolved on the Scheduler.

        Args:
            selector: Selector to aid selection of targets.
        """
        pass

    ##
    ## Supporting Methods
    ##

    # TODO: util.Controller

    def act(self, controller):
        """Standard method of resolving actions for characters

        Simple approach to resolving actions of any character using controller.
        Complex characters may require a custom act override for this, but such
        characters should be extremely rare. See Conditional Buffs for complex
        resolutions depending on Events.

        Args:
            controller: Controller to resolve choosing between multiple actions
        """
        # Check if controller considers ult available for usage
        use_ult = controller.ult_available(entity)
        # Resolve ult usage if ult is allowed to be used
        if use_ult:
            controller.scheduler.resolve(self.ult())

        # If entities' turn, use a basic / skill then maybe ult
        if controller.is_turn(entity):
            # Calculate the number of skill points ally is allowed to use
            sp = controller.sp_available(entity)
            # If skill_points > 0, ally should use skill point allocated
            event = self.skill(sp) if sp > 0 else self.basic()
            # Resolve event for ally
            controller.scheduler.resolve(event)

            # Check if controller considers ult available for usage
            use_ult = controller.ult_available(entity)
            # Resolve ult usage if ult is allowed to be used
            if use_ult:
                controller.scheduler.resolve(self.ult())


# TODO: think enemies need action queue for freeze. maybe all entities do?

def Enemy(mchsr.entity.Entity):
    """Represents an Entity that is not an Ally"""

    ##
    ## Initalization
    ##

    def __init__(
        self, elem_weak=list, elem_strong=list, stats: mchsr.entity.Stats = None, buffs: list = []
    ):
        """Initializes the instance based on provided values

        Args:
            elem_weak: List of Elements entity weak to
            elem_strong: List of Elements entity stronger against
            stats: Stats for the entity, if entity has base stats
            buffs: List of initial buffs applied
        """
        # Enemies have common stats modifications
        if stats:
            # Resolve typical enemy element resistance
            stats.base_res += 0.2
            for elem in elem_weak:
                stats.elem_res[elem] -= 0.2
            for elem in elem_strong:
                stats.elem_res[elem] += 0.2
            # Resolve toughness reduction
            stats.base_rdmg += 0.1
        # Entity initialization
        super().__init__(stats, buffs)
