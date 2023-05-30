import mchsr.entity
import random


def calculate_damage(
    source: mchsr.entity.Entity, target: mchsr.entity.Entity, is_crit: bool = False
) -> float:
    """Calculates damage dealt from source to target

    Args:
        source: Source dealing damage to target.
        target: Target taking damage from source.

    Returns:
        The expected damage taken, ignoring crits
    """

    # Calculate Base DMG
    base_dmg = (
        skill_multiplier + source.stats.buff_emul
    ) * scaling_attribute + source.stats.flat_dmg
    # Calculate DMG% Multiplier
    dmg_mul = 1 + source.stats.buff_dmg
    # Calculate DEF of target, note DEF Reduction inside buff_dfd
    target_dfd = (
        target.base_dfd * (1 + target.buff_dfd - source.buff_dpen) + target.flat_dfd
    )
    if target_dfd < 0:
        target_dfd = 0
    # Calculate DEF Multiplier
    def_mul = 1 - (target_dfd / (target_dfd + 20 + 10 * source.level))
    # Calculate RES Multiplier
    res_mul = 1 + source.buff_rpen - target.base_res
    if res_mul < 0.1:
        res_mul = 0.1
    if res_mul > 2.0:
        res_mul = 2.0
    # Calculate DMG Taken Multiplier
    tdmg_mul = 1 + target.buff_tdmg
    if tdmg_mul > 3.5:
        tdmg_mul = 3.5
    # Calculate Universal DMG Reduction Multiplier
    # TODO(any): buff_rdmg is multiplicative scaling, might need fix
    rdmg_mul = 1 - (1 - target.base_rdmg) * (1 - target.buff_rdmg)
    # Calculate Weaken Multiplier
    weak_mul = 1 - source.buff_weak
    # Calculate Outgoing DMG
    out_dmg = base_dmg * dmg_mul * def_mul * res_mul * tdmg_mul * rdmg_mul * weak_mul
    # Increase by critical damage multiplier, if crit
    if is_crit:
        out_dmg *= source.cdmg
    return out_dmg


# TODO(any): Perhaps need a crit resolver instead of random number approach


def is_crit(source: mchsr.entity.Entity, target: mchsr.entity.Entity) -> bool:
    """Calculates whether the current event should be considered a crit

    Args:
        source: Source dealing damage to target.
        target: Target taking damage from source.

    Returns:
        Whether the attack should be considered a crit
    """
    # Calculate crit occuring using random generator
    return random.random() <= source.stats.crate


class Take(mchsr.entity.Event):
    """Represents entity taking damage, often triggered by Deal / Crit Events

    Arguments:
        source: Event leading to current Event.
        damage: Calculated damage to be dealt to Entity.
    """

    def __init__(
        self, entity: mchsr.entity.Entity, source: mchsr.entity.Event, damage: float
    ):
        """Initializes the instance based on provided values

        Args:
            entity: Entity executing the current Event.
            source: Event leading to current Event.
            damage: Calculated damage to be dealt to Entity.
        """
        self.source = source
        self.damage = damage
        super().__init__(entity)

    def execute(self, scheduler):
        """Executes the event on the provided scheduler

        Args:
            scheduler: Scheduler executing current Event.
        """
        entity.curr_hp -= damage
        if entity.curr_hp < 0:
            entity.curr_hp = 0


class Crit(mchsr.entity.Event):
    """Represents critical damage occuring, often triggered by Deal Event

    Arguments:
        source: Event leading to current Event.
        damage: Calculated damage to be dealt to Entity, before crit.
    """

    def __init__(
        self,
        entity: mchsr.entity.Entity,
        select_event,
        skill_multiplier: float,
        scaling_attribute: float,
    ):
        """Initializes the instance based on provided values

        Args:
            entity: Entity executing the current Event.
            select_event: Event selecting target(s) for Damage Event.
            skill_multiplier: Float for skill multiplier in Damage calculation.
            scaling_attribute: Float for scaling attribute in Damage calc.
        """
        self.select_event = select_event
        self.skill_multiplier = skill_multiplier
        self.scaling_attribute = scaling_attribute
        super().__init__(entity)

    def execute(self, scheduler):
        """Executes the event on the provided scheduler

        Args:
            scheduler: Scheduler executing current Event.
        """
        out_dmg = calculate_damage(entity, target, True)
        # Resolve damage taken event
        damage_taken_event = Take(target, self, out_dmg)
        scheduler.resolve(damage_taken_event)


class Deal(mchsr.entity.Event):
    """Represents an entity dealing damage to a target in the Simulation

    Arguments:
        select_event: Event selecting target(s) for Damage Event
        skill_multiplier: Float for skill multiplier in Damage calculation
        scaling_attribute: Float for scaling attribute in Damage calculation
    """

    def __init__(
        self,
        entity: mchsr.entity.Entity,
        select_event,
        skill_multiplier: float,
        scaling_attribute: float,
    ):
        """Initializes the instance based on provided values

        Args:
            entity: Entity executing the current Event.
            select_event: Event selecting target(s) for Damage Event.
            skill_multiplier: Float for skill multiplier in Damage calculation.
            scaling_attribute: Float for scaling attribute in Damage calc.
        """
        self.select_event = select_event
        self.skill_multiplier = skill_multiplier
        self.scaling_attribute = scaling_attribute
        super().__init__(entity)

    def execute(self, scheduler):
        """Executes the event on the provided scheduler

        Args:
            scheduler: Scheduler executing current Event.
        """
        # For each target attacked, calculate damage and resolve
        for target in select_event.targets:
            # If Crit, resolve using Crit Event
            if is_crit(entity, target):
                crit_event = Crit(
                    entity, select_event, skill_multiplier, scaling_attribute
                )
                scheduler.resolve(crit_event)
            else:
                out_dmg = calculate_damage(entity, target)
                # Resolve damage taken event
                damage_taken_event = Take(target, self, out_dmg)
                scheduler.resolve(damage_taken_event)

        print("dmg done")
