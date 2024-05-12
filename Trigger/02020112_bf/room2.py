""" trigger/02020112_bf/room2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990015, key='Extinction_2_check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteDead', value=1):
            return 종료2(self.ctx)
        # all_of:  <첫번째 격리조치가 끝난 후에 발동하도록>
        if self.user_value(key='Extinction', value=1) and self.user_value(key='Extinction_1_check', value=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020112_BF__ROOM2__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteDead', value=1):
            return 종료2(self.ctx)
        if self.wait_tick(wait_tick=3000):
            return 격리(self.ctx)


class 격리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=2020112, portal_id=6, box_id=932, count=1)
        self.set_timer(timer_id='1', seconds=20, interval=1, v_offset=-40)
        self.set_mesh(trigger_ids=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727], visible=True, start_delay=0, interval=0, fade=3)
        self.set_mesh(trigger_ids=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827], visible=False, start_delay=0, interval=0, fade=3)
        self.spawn_monster(spawn_ids=[181], auto_target=False)
        self.spawn_monster(spawn_ids=[182], auto_target=False)
        self.spawn_monster(spawn_ids=[183], auto_target=False)
        self.set_event_ui(type=1, arg2='$02020112_BF__ROOM2__1$', arg3='5000', arg4='932')
        self.add_buff(box_ids=[941], skill_id=70002106, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteDead', value=1):
            return 종료2(self.ctx)
        if self.monster_dead(spawn_ids=[181,182,183]):
            return 구출(self.ctx)
        if self.wait_tick(wait_tick=20000):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[941], skill_id=70002107, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteDead', value=1):
            return 종료2(self.ctx)
        return 종료(self.ctx)


class 구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2020112, portal_id=5, box_id=941)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteDead', value=1):
            return 종료2(self.ctx)
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990015, key='Extinction_2_check', value=2)
        self.destroy_monster(spawn_ids=[181,182,183])
        self.move_user(map_id=2020112, portal_id=5, box_id=941)
        self.set_mesh(trigger_ids=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727], visible=False, start_delay=0, interval=30, fade=3)
        self.set_mesh(trigger_ids=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827], visible=True, start_delay=0, interval=30, fade=3)
        self.reset_timer(timer_id='1')


class 종료2(trigger_api.Trigger):
    pass


initial_state = 대기
