""" trigger/02020112_bf/room1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990014, key='Extinction_1_check', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='EliteDead', value=1):
            return 종료2()
        if user_value(key='Extinction', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020112_BF__ROOM1__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if user_value(key='EliteDead', value=1):
            return 종료2()
        if wait_tick(waitTick=3000):
            return 격리()


class 격리(state.State):
    def on_enter(self):
        move_random_user(mapId=2020112, portalId=6, triggerId=932, count=1)
        set_timer(timerId='1', seconds=20, display=True, arg5=-40)
        set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727], visible=True, arg3=0, arg4=0, arg5=3)
        set_mesh(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827], visible=False, arg3=0, arg4=0, arg5=3)
        create_monster(spawnIds=[181], arg2=False)
        create_monster(spawnIds=[182], arg2=False)
        create_monster(spawnIds=[183], arg2=False)
        set_event_ui(type=1, arg2='$02020112_BF__ROOM1__1$', arg3='5000', arg4='932')
        add_buff(boxIds=[941], skillId=70002106, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if user_value(key='EliteDead', value=1):
            return 종료2()
        if monster_dead(boxIds=[181,182,183]):
            return 구출()
        if wait_tick(waitTick=20000):
            return 소멸()


class 소멸(state.State):
    def on_enter(self):
        add_buff(boxIds=[941], skillId=70002107, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if user_value(key='EliteDead', value=1):
            return 종료2()
        if true():
            return 종료()


class 구출(state.State):
    def on_enter(self):
        move_user(mapId=2020112, portalId=5, boxId=941)

    def on_tick(self) -> state.State:
        if user_value(key='EliteDead', value=1):
            return 종료2()
        if true():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990014, key='Extinction_1_check', value=1)
        destroy_monster(spawnIds=[181,182,183])
        move_user(mapId=2020112, portalId=5, boxId=941)
        set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727], visible=False, arg3=0, arg4=30, arg5=3)
        set_mesh(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827], visible=True, arg3=0, arg4=30, arg5=3)
        reset_timer(timerId='1')


class 종료2(state.State):
    pass


