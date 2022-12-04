""" trigger/02020112_bf/room3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteDead', value=1):
            return 종료2(self.ctx)
        if self.all_of():
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020112_BF__ROOM3__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteDead', value=1):
            return 종료2(self.ctx)
        if self.wait_tick(waitTick=3000):
            return 격리(self.ctx)


class 격리(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2020112, portalId=6, triggerId=932, count=1)
        self.set_timer(timerId='1', seconds=20, interval=1, vOffset=-40)
        self.set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727], visible=True, arg3=0, delay=0, scale=3)
        self.set_mesh(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827], visible=False, arg3=0, delay=0, scale=3)
        self.create_monster(spawnIds=[181], animationEffect=False)
        self.create_monster(spawnIds=[182], animationEffect=False)
        self.create_monster(spawnIds=[183], animationEffect=False)
        self.set_event_ui(type=1, arg2='$02020112_BF__ROOM3__1$', arg3='5000', arg4='932')
        self.add_buff(boxIds=[941], skillId=70002106, level=1, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteDead', value=1):
            return 종료2(self.ctx)
        if self.monster_dead(boxIds=[181,182,183]):
            return 구출(self.ctx)
        if self.wait_tick(waitTick=20000):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[941], skillId=70002107, level=1, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteDead', value=1):
            return 종료2(self.ctx)
        if self.true():
            return 종료(self.ctx)


class 구출(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2020112, portalId=5, boxId=941)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteDead', value=1):
            return 종료2(self.ctx)
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[181,182,183])
        self.move_user(mapId=2020112, portalId=5, boxId=941)
        self.set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727], visible=False, arg3=0, delay=30, scale=3)
        self.set_mesh(triggerIds=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827], visible=True, arg3=0, delay=30, scale=3)
        self.reset_timer(timerId='1')


class 종료2(trigger_api.Trigger):
    pass


initial_state = 대기
