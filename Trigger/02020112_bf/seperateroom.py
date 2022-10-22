""" trigger/02020112_bf/seperateroom.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827], visible=True, arg3=0, arg4=0, arg5=0)
        set_user_value(triggerId=99990013, key='Extinction', value=0)
        set_user_value(triggerId=99990014, key='Extinction', value=0)
        set_user_value(triggerId=99990015, key='Extinction', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Start', value=1):
            return 시작()


class 시작(state.State):
    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=70, spawnId=191, isRelative=True):
            return 격리조치_1_준비()


class 격리조치_1_준비(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990013, key='Extinction', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Start', value=2):
            return 종료()
        if check_npc_hp(compare='lowerEqual', value=45, spawnId=191, isRelative=True):
            return 격리조치_2_준비()


class 격리조치_2_준비(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990014, key='Extinction', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Start', value=2):
            return 종료()
        if check_npc_hp(compare='lowerEqual', value=20, spawnId=191, isRelative=True):
            return 격리조치_2_준비()


class 격리조치_3_준비(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990015, key='Extinction', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Start', value=2):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[181,182,183])
        reset_timer(timerId='1')
        reset_timer(timerId='2')
        reset_timer(timerId='3')
        set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727], visible=False, arg3=0, arg4=0, arg5=3)
        set_mesh(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827], visible=True, arg3=0, arg4=0, arg5=3)


