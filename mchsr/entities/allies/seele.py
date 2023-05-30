import mchsr.entities.type
import mchsr.entity
import mchsr.buffs.common


class Basic(mchsr.events.attack.Basic):
    """Seele's basic attack event"""

    def execute(scheduler):
        # Select a single enemy using the selector
        select_event = selector.select(entity, 1, False)
        scheduler.resolve_event(select_event)
        # Calculate expected damage and resolve damage dealing event
        damage_event = DamageEvent(entity, select_event, 1.0, entity.stats.atk)
        scheduler.resolve_event(damage_event)


class Skill(mchsr.events.attack.Skill):
    """Seele's skill attack event"""

    def execute(scheduler):
        # Buff speed
        buff_event = BuffEvent(entity, buff.BuffSPD(entity, 0.25, True, 2))
        scheduler.resolve_event(buff_event)
        # Select a single enemy using the selector
        select_event = selector.select(entity, 1, False)
        scheduler.resolve_event(select_event)
        # Calculate expected damage and resolve damage dealing event
        damage_event = DamageEvent(entity, select_event, 2.2, entity.stats.atk)
        scheduler.resolve_event(damage_event)


class Ult(mchsr.events.attack.Ult):
    """Seele's ult attack event"""

    def execute(scheduler):
        # Buff dmg
        buff_event = BuffEvent(entity, buff.BuffDMG(entity, 0.8, True, 1))
        scheduler.resolve_event(buff_event)
        # Select a single enemy using the selector
        select_event = selector.select(entity, 1, False)
        scheduler.resolve_event(select_event)
        # Calculate expected damage and resolve damage dealing event
        damage_event = DamageEvent(entity, select_event, 4.25, entity.stats.atk)
        scheduler.resolve_event(damage_event)


class Seele(mchsr.entities.type.Ally):
    """Seele, the Quantun Hunt 5 Star Character in HSR

    Arguments:
        buffs: List of initial buffs applied
    """

    ##
    ## Initialization
    ##

    def __init__(self, buffs: list = []):
        """Initializes the instance based on provided values

        Args:
            stats: Stats for the entity, if entity has base stats
            buffs: List of initial buffs applied
        """
        # Provide hard-coded stats for level 80
        stats = mchsr.entity.Stats(
            80,
            931,
            640.33,
            363.83,
            115,
            75,
            0.05,
            0.5,
            0,
            0,
            mchsr.entity.Element.Quantum,
        )

        # Provide buffs for all traces of the unit
        crit_buff = mchsr.buffs.common.FlatCDMG(0.053 + 0.08, False)
        atk_buff = mchsr.buffs.common.BuffATK(0.04 + 0.08 + 0.04 + 0.06 + 0.06, False)
        dfd_buff = mchsr.buffs.common.BuffDFD(0.075 + 0.05, False)
        buffs.extend(crit_buff, atk_buff, dfd_buff)

        # TODO: Resurgence conditional buff

        # Entity initialization
        super().__init__(stats, buffs)

    ##
    ## Abstract Implementation
    ##

    def basic(self, selector) -> mchsr.entity.Event:
        return Basic(self, selector)

    def skill(self, selector, sp: int = 1) -> mchsr.entity.Event:
        return Skill(self, selector)

    def ult(self, selector) -> mchsr.entity.Event:
        return Ult(self, selector)
