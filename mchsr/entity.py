from abc import ABC, abstractmethod
from enum import Enum


class Element(Enum):
    PHYSICAL = 1
    FIRE = 2
    ICE = 3
    LIGHTNING = 4
    WIND = 5
    QUANTUM = 6
    IMAGINARY = 7


# TODO: RES % per element


class Stats:
    """Stats that are associated with an Entity for calculations

    Stats are the critical values for the calculation of an entity's damage,
    AV progression, current hitpoints, etc. These are often modified during
    Sim by the Buff class, which drastically changes the resulting values of
    the stat calculations.

    Attributes:
        level: Int for the level of the entity.
        max_hp: Float for the current max hitpoints of the entity.
        curr_hp: Float for the current hitpoints of the entity.
        base_hp: Float for the base hitpoints of the entity.
        flat_hp: Float for extra flat hitpoints of the entity.
        buff_hp: Float for HP % multiplier of the entity.
        atk: Float for the current attack of the entity.
        base_atk: Float for the base attack value of the entity.
        flat_atk: Float for extra flat attack of the entity.
        buff_atk: Float for ATK % multiplier of the entity.
        dfd: Float for the current defense of the entity.
        base_dfd: Float for the base defense of the entity.
        flat_dfd: Float for extra flat defense of the entity.
        buff_dfd: Float for DEF % multiplier of the entity.
        curr_av: Float for the current AV of the entity.
        spd: Float for the current speed of the entity.
        base_spd: Float for the base speed of the entity.
        flat_spd: Float for extra flat speed of the entity.
        buff_spd: Float for SPD % multiplier of the entity.
        taunt: Float for the current taunt of the entity.
        base_taunt: Float for the base taunt value of the entity.
        buff_taunt: Float for the Taunt % multiplier of the entity.
        crate: Float for the current Critical Hit Rate % of the entity.
        base_crate: Float for the base Critical Hit % of the entity.
        flat_crate: Float for the extra Critical Hit Rate % of the entity.
        cdmg: Float for the current Critical Damage % of the entity.
        base_cdmg: Float for the base Critical Damage % of the entity.
        flat_cdmg: Float for the extra Critical Damage % of the entity.
        base_res: Float for the base RES to all elements of the entity.
        buff_res: Float for the extra Effect Resistance % of the entity.
        buff_nrg: Float for the extra Energy Regeneration % of the entity.
        ehr: Float for the current Effective Hit Rate % of the entity.
        buff_ehr: Float for the extra Effect Hit Rate % of the entity.
        buff_dmg: Float for the DMG % multiplier of the entity.
        flat_dmg: Float for the Flat Damage applied for the entity.
        buff_emul: Float for the Extra Multiplier applied for the entity.
        buff_rpen: Float for the Resistance Penetration % of the entity.
        buff_dpen: Float for the Defense Penetration % of the entity.
        base_rdmg: Float for base Universal DMG Reduction % of the entity.
        buff_rdmg: Float for the Universal Damage Reduction % of the entity.
        buff_tdmg: Float for the Damage Taken Multiplier % of the entity.
        buff_weak: Float for the Weaken % of the entity.
        element: Element (or None) for the entity.
        elem_res: Dict mapping Element to extra RES % for Element of the entity.
    """

    def __init__(
        self,
        level: int,
        base_hp: float,
        base_atk: float,
        base_dfd: float,
        base_spd: float,
        base_taunt: float,
        base_crate: float,
        base_cdmg: float,
        base_res: float,
        base_rdmg: float,
        element: Element = None,
    ):
        """Initialize the instance based on the provided values

        Args:
            level: Int for the level of the entity.
            base_hp: Float for the base hitpoints of the entity.
            base_atk: Float for the base attack value of the entity.
            base_dfd: Float for the base defense of the entity.
            base_spd: Float for the base speed of the entity.
            base_taunt: Float for the base taunt value of the entity.
            base_crate: Float for the base Critical Hit % of the entity.
            base_cdmg: Float for the base Critical Damage % of the entity.
            base_res: Float for the base RES to all elements of the entity.
            base_rdmg: Float for base Universal DMG Reduction % of the entity.
            element: Element for the entity's element, if entity has an element
        """
        self.level = level
        self.curr_hp = base_hp
        self.base_hp = base_hp
        self.flat_hp = 0
        self.buff_hp = 0
        self.base_atk = base_atk
        self.flat_atk = 0
        self.buff_atk = 0
        self.base_dfd = base_dfd
        self.flat_dfd = 0
        self.buff_dfd = 0
        self.curr_av = 10000 / base_spd  # TODO(shi): Is this right time? Buffs
        self.base_spd = base_spd
        self.flat_spd = 0
        self.buff_spd = 0
        self.base_taunt = base_taunt
        self.buff_taunt = 0
        self.base_crate = base_crate
        self.flat_crate = 0
        self.base_cdmg = base_cdmg
        self.flat_cdmg = 0
        self.buff_nrg = 0
        self.ehr = 1
        self.buff_ehr = 0
        self.base_res = base_res
        self.buff_res = 0
        self.buff_dmg = 0
        self.flat_dmg = 0
        self.buff_emul = 0
        self.buff_rpen = 0
        self.buff_dpen = 0
        self.base_rdmg = base_rdmg
        self.buff_rdmg = 0
        self.buff_tdmg = 0
        self.buff_weak = 0
        self.element = element
        elem_res = {i.name: 0 for i in Element}

    @property
    def max_hp(self):
        """Returns the current maximum hitpoints of the entity"""
        return (self.base_hp) * (1 + self.buff_hp) + self.flat_hp

    @property
    def atk(self):
        """Returns the current attack of the entity"""
        return (self.base_atk) * (1 + self.buff_atk) + self.flat_atk

    @property
    def dfd(self):
        """Returns the current defense of the entity"""
        return (self.base_dfd) * (1 + self.buff_dfd) + self.flat_dfd

    @property
    def spd(self):
        """Returns the current speed of the entity"""
        return (self.base_spd) * (1 + self.buff_spd) + self.flat_spd

    @property
    def taunt(self):
        """Returns the current Taunt value of the entity"""
        return (self.base_taunt) * (1 + self.buff_taunt)

    @property
    def crate(self):
        """Returns the current Critical Hit Rate % of the entity"""
        return self.base_crate + self.flat_crate

    @property
    def cdmg(self):
        """Returns the current Critical Damage % of the entity"""
        return 1 + self.base_cdmg + self.flat_cdmg

    @property
    def ehr(self):
        """Returns the current Effective Hit Rate % of the entity"""
        return 1 + self.buff_ehr


class Entity(ABC):
    """Entity to simulate

    Entities represent anything that acts on the Timeline. These are often
    characters and enemies, although other things that act on the Timeline
    like a summon may be represented using an entity with no personal Stats.

    Attributes:
        stats: If not `None`, Stat for the entity's calculations.
        buffs: List of all Buffs applied to current entity.
    """

    ##
    ## Initalization
    ##

    def __init__(self, stats: Stats = None, buffs: list = []):
        """Initializes the instance based on provided values

        Args:
            stats: Stats for the entity, if entity has base stats
            buffs: List of initial buffs applied
        """
        self.stats = stats
        self.buffs = buffs

    ##
    ## Abstract Requirements
    ##

    # TODO: ults not always on own turn, needs another thing for that
    # TODO: controller: util.Controller

    @abstractmethod
    def act(self, controller):
        """Resolves any actions of the entity for current controller state

        Called on the Entity anytime there is a chance for it to execute an
        Event. For allies, this often occurs at the start / end of every turn
        (due to potential ult usage). The controller provided is leveraged for
        choosing which, if multiple actions are available, should be leveraged.
        For instance, a dps-calculation controller may be programmed to ensure
        a specific entity always uses their skill when skill points available.

        Args:
            controller: Controller to resolve choosing between multiple actions
        """
        pass


class Event(ABC):
    """Represents an Entity taking an action in the Simulation

    An Event represents anything related to the behavior of an Entity. Events
    have a set number of targets, which may include the current entity.

    Events often call other Events. For example, a character using a basic skill
    may trigger a damage event. Event-driven approach to these behaviors allows
    for the proper resolution of refreshing buff durations due to re-triggering
    a Buff on a character from the same source, as well as the proper resolution
    of any Conditional Buffs on an entity. Many Conditional Buffs are directly
    tied to a given Event beginning / ending. See buffs.Conditional for more
    info.

    Examples:
        * Entity trying to apply Buff to target(s) (including self)
        * Entity trying to start or end their turn in Simulation
        * Entity trying to resolve damaging target(s)
        * Entity trying to initialize combat state

    Arguments:
        entity: Entity executing the current Event.
    """

    ##
    ## Initalization
    ##

    def __init__(self, entity: Entity):
        """Initializes the instance based on provided values

        Args:
            entity: Entity executing the current Event.
        """
        self.entity = entity

    ##
    ## Abstract Requirements
    ##

    @abstractmethod
    def execute(self, scheduler):
        """Executes the event on the provided scheduler

        Args:
            scheduler: Scheduler executing current Event.
        """
        pass


# TODO: Debuff for negative Buff, due to EHR and debuff immunities?
#       maybe just assume Buffs from allies, Debuffs from enemies


class Buff(ABC):
    """Modifications to an entity for calculations

    Buffs represent any change that would change an entity's calculations.
    Buffs are either dispellable or undispellable (dispellable), and might
    only last for a certain number of entity turns (turns). Buffs can last
    forever (turns = None), until the end of the turn (turns = 0), until the
    end of the next turn (turns = 1), or until the end of the next X turns
    (turns = X).

    For buffs requiring conditions to be met, see buffs.Conditional.

    Examples:
        * Entity's Relics / Minor Traces give unexpiring undispellable Buffs
        * Debuffs applied to an Entity are expiring dispellable Buffs
        * Action Advance is a 0 turn, undispellable Buff
        * Entity's Lightcone is an unexpiring undispellable Buff

    Attributes:
        source: Event that resulted in the buff.
        dispellable: Boolean for whether the buff can be dispelled.
        turns: If not `None`, Int for number of turns left on buff.
    """

    ##
    ## Initialization
    ##

    def __init__(
        self, source: Event = None, dispellable: bool = True, turns: int = None
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.source = source
        self.dispellable = dispellable
        self.turns = turns

    ##
    ## Abstract Requirements
    ##

    @abstractmethod
    def apply(self, stats: Stats):
        """Applies specific buff to the state provided

        Args:
            stats: Stats for the buff to act upon
        """
        pass

    @abstractmethod
    def remove(self, stats: Stats):
        """Removes the specific buff from the state provided

        Args:
            stats: Stats for the buff to act upon
        """
        pass
