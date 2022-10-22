""" trigger/02000471_bf/magic_02.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040315, key='10002020clear', value=0)
        set_user_value(triggerId=2040317, key='10002020clear', value=0)
        set_user_value(triggerId=2040322, key='10002020clear', value=0)
        set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799], visible=False, arg3=0, arg4=200, arg5=35)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002020], arg2=0):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7002], visible=False)
        set_mesh(triggerIds=[1102], visible=False, arg3=0, arg4=200, arg5=15)
        set_mesh(triggerIds=[1202], visible=True, arg3=0, arg4=200, arg5=15)
        create_monster(spawnIds=[202], arg2=False)
        add_buff(boxIds=[202], skillId=70002011, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[202]):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040315, key='10002020clear', value=1)
        set_user_value(triggerId=2040317, key='10002020clear', value=1)
        set_user_value(triggerId=2040322, key='10002020clear', value=1)
        set_achievement(triggerId=712, type='trigger', achieve='Hauntedmansion')
        create_monster(spawnIds=[1121,1122], arg2=False)
        set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799], visible=True, arg3=0, arg4=200, arg5=35)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Event_02_b()


class Event_02_b(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1122, script='$02000471_BF__MAGIC_02__0$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=1121, script='$02000471_BF__MAGIC_02__1$', arg4=3, arg5=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Event_02_c()


class Event_02_c(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799], visible=False, arg3=0, arg4=200, arg5=35)
        destroy_monster(spawnIds=[1121,1122])


