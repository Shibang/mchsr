from entity import Buff, Stats

# TODO: AV events like action advance


class BaseHP(Buff):
    """Buffs the base_hp of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's base_hp.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's base_hp.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates base_hp of Entity's Stats based on value"""
        stats.base_hp += value

    def remove(stats: Stats):
        """Updates base_hp of Entity's Stats based on value"""
        stats.base_hp -= value


class FlatHP(Buff):
    """Buffs the flat_hp of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's flat_hp.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's flat_hp.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates flat_hp of Entity's stats based on value"""
        stats.flat_hp += value

    def remove(stats: Stats):
        """Updates flat_hp of Entity's Stats based on value"""
        stats.flat_hp -= value


class BuffHP(Buff):
    """Buffs the buff_hp of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_hp.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_hp.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_hp of Entity's stats based on value"""
        stats.buff_hp += value

    def remove(stats: Stats):
        """Updates buff_hp of Entity's Stats based on value"""
        stats.buff_hp -= value


class BaseATK(Buff):
    """Buffs the base_atk of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's base_atk.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's base_atk.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates base_atk of Entity's Stats based on value"""
        stats.base_atk += value

    def remove(stats: Stats):
        """Updates base_atk of Entity's Stats based on value"""
        stats.base_atk -= value


class FlatATK(Buff):
    """Buffs the flat_atk of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's flat_atk.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's flat_atk.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates flat_atk of Entity's stats based on value"""
        stats.flat_atk += value

    def remove(stats: Stats):
        """Updates flat_atk of Entity's Stats based on value"""
        stats.flat_atk -= value


class BuffATK(Buff):
    """Buffs the buff_atk of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_atk.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_atk.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_atk of Entity's stats based on value"""
        stats.buff_atk += value

    def remove(stats: Stats):
        """Updates buff_atk of Entity's Stats based on value"""
        stats.buff_atk -= value


class BaseDFD(Buff):
    """Buffs the base_dfd of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's base_dfd.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's base_dfd.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates base_dfd of Entity's Stats based on value"""
        stats.base_dfd += value

    def remove(stats: Stats):
        """Updates base_dfd of Entity's Stats based on value"""
        stats.base_dfd -= value


class FlatDFD(Buff):
    """Buffs the flat_dfd of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's flat_dfd.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's flat_dfd.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates flat_dfd of Entity's stats based on value"""
        stats.flat_dfd += value

    def remove(stats: Stats):
        """Updates flat_dfd of Entity's Stats based on value"""
        stats.flat_dfd -= value


class BuffDFD(Buff):
    """Buffs the buff_dfd of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_dfd.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_dfd.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_dfd of Entity's stats based on value"""
        stats.buff_dfd += value

    def remove(stats: Stats):
        """Updates buff_dfd of Entity's Stats based on value"""
        stats.buff_dfd -= value


class BaseSPD(Buff):
    """Buffs the base_spd of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's base_spd.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's base_spd.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates base_spd of Entity's Stats based on value"""
        stats.base_spd += value

    def remove(stats: Stats):
        """Updates base_spd of Entity's Stats based on value"""
        stats.base_spd -= value


class FlatSPD(Buff):
    """Buffs the flat_spd of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's flat_spd.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's flat_spd.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates flat_spd of Entity's stats based on value"""
        stats.flat_spd += value

    def remove(stats: Stats):
        """Updates flat_spd of Entity's Stats based on value"""
        stats.flat_spd -= value


class BuffSPD(Buff):
    """Buffs the buff_spd of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_spd.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_spd.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_spd of Entity's stats based on value"""
        stats.buff_spd += value

    def remove(stats: Stats):
        """Updates buff_spd of Entity's Stats based on value"""
        stats.buff_spd -= value


class BaseTaunt(Buff):
    """Buffs the base_taunt of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's base_taunt.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's base_taunt.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates base_taunt of Entity's Stats based on value"""
        stats.base_taunt += value

    def remove(stats: Stats):
        """Updates base_taunt of Entity's Stats based on value"""
        stats.base_taunt -= value


class BuffTaunt(Buff):
    """Buffs the buff_taunt of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_taunt.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_taunt.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_taunt of Entity's stats based on value"""
        stats.buff_taunt += value

    def remove(stats: Stats):
        """Updates buff_taunt of Entity's Stats based on value"""
        stats.buff_taunt -= value


class BaseCRate(Buff):
    """Buffs the base_crate of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's base_crate.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's base_crate.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates base_crate of Entity's Stats based on value"""
        stats.base_crate += value

    def remove(stats: Stats):
        """Updates base_crate of Entity's Stats based on value"""
        stats.base_crate -= value


class FlatCRate(Buff):
    """Buffs the buff_crate of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_crate.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_crate.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_crate of Entity's stats based on value"""
        stats.flat_crate += value

    def remove(stats: Stats):
        """Updates buff_crate of Entity's Stats based on value"""
        stats.flat_crate -= value


class BaseCDMG(Buff):
    """Buffs the base_cdmg of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's base_cdmg.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's base_cdmg.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates base_cdmg of Entity's Stats based on value"""
        stats.base_cdmg += value

    def remove(stats: Stats):
        """Updates base_cdmg of Entity's Stats based on value"""
        stats.base_cdmg -= value


class FlatCDMG(Buff):
    """Buffs the buff_cdmg of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_cdmg.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_cdmg.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_cdmg of Entity's stats based on value"""
        stats.flat_cdmg += value

    def remove(stats: Stats):
        """Updates buff_cdmg of Entity's Stats based on value"""
        stats.flat_cdmg -= value


class BuffNRG(Buff):
    """Buffs the buff_nrg of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_nrg.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_nrg.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_nrg of Entity's stats based on value"""
        stats.buff_nrg += value

    def remove(stats: Stats):
        """Updates buff_nrg of Entity's Stats based on value"""
        stats.buff_nrg -= value


class BuffEHR(Buff):
    """Buffs the buff_ehr of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_ehr.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_ehr.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_ehr of Entity's stats based on value"""
        stats.buff_ehr += value

    def remove(stats: Stats):
        """Updates buff_ehr of Entity's Stats based on value"""
        stats.buff_ehr -= value


class BuffRES(Buff):
    """Buffs the buff_res of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_res.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_res.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_res of Entity's stats based on value"""
        stats.buff_res += value

    def remove(stats: Stats):
        """Updates buff_res of Entity's Stats based on value"""
        stats.buff_res -= value


class BuffDMG(Buff):
    """Buffs the buff_dmg of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_dmg.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_dmg.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_dmg of Entity's stats based on value"""
        stats.buff_dmg += value

    def remove(stats: Stats):
        """Updates buff_dmg of Entity's Stats based on value"""
        stats.buff_dmg -= value


class FlatDMG(Buff):
    """Buffs the flat_dmg of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's flat_dmg.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's flat_dmg.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates flat_dmg of Entity's stats based on value"""
        stats.flat_dmg += value

    def remove(stats: Stats):
        """Updates flat_dmg of Entity's Stats based on value"""
        stats.flat_dmg -= value


class BuffEMul(Buff):
    """Buffs the buff_emul of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_emul.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_emul.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_emul of Entity's stats based on value"""
        stats.buff_emul += value

    def remove(stats: Stats):
        """Updates buff_emul of Entity's Stats based on value"""
        stats.buff_emul -= value


class BuffRPen(Buff):
    """Buffs the buff_rpen of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_rpen.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_rpen.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_rpen of Entity's stats based on value"""
        stats.buff_rpen += value

    def remove(stats: Stats):
        """Updates buff_rpen of Entity's Stats based on value"""
        stats.buff_rpen -= value


class BuffDPen(Buff):
    """Buffs the buff_dpen of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_dpen.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_dpen.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_dpen of Entity's stats based on value"""
        stats.buff_dpen += value

    def remove(stats: Stats):
        """Updates buff_dpen of Entity's Stats based on value"""
        stats.buff_dpen -= value


class BuffRDMG(Buff):
    """Buffs the buff_rdmg of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_rdmg.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_rdmg.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_rdmg of Entity's stats based on value"""
        stats.buff_rdmg += value

    def remove(stats: Stats):
        """Updates buff_rdmg of Entity's Stats based on value"""
        stats.buff_rdmg -= value


class BuffTDMG(Buff):
    """Buffs the buff_tdmg of an Entity's Stats

    Arguments:
        value: Float used to alter the entity's buff_tdmg.
    """

    def __init__(
        self,
        value: Float,
        source: Event = None,
        dispellable: bool = True,
        turns: Int | None = None,
    ):
        """Initializes the instance based on provided values

        Args:
            source: Event that resulted in the buff.
            value: Float used to alter the entity's buff_tdmg.
            dispellable: Boolean for whether the buff can be dispelled.
            turns: If provided, Int for number of turns left on buff.
        """
        self.value = value
        super().__init__(source, dispellable, turns)

    def apply(stats: Stats):
        """Updates buff_tdmg of Entity's stats based on value"""
        stats.buff_tdmg += value

    def remove(stats: Stats):
        """Updates buff_tdmg of Entity's Stats based on value"""
        stats.buff_tdmg -= value
