""" trigger/02100009_bf/main.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 타이머설정(self.ctx)


class 타이머설정(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=True)
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)
        self.set_timer(timerId='10000', seconds=300, startDelay=1, interval=1, vOffset=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 성공(self.ctx)
        if self.time_expired(timerId='10000'):
            return 실패(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='10000')


class 성공(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 성공_2(self.ctx)

    def on_exit(self):
        self.set_event_ui(type=1, arg2='$02100009_BF__text__0$', arg3='4000')


class 성공_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5500):
            self.dungeon_clear()
            return 성공_3(self.ctx)

    def on_exit(self):
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)


class 성공_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=50000230, level=1, isPlayer=False, isSkillSet=False)
        self.destroy_monster(spawnIds=[-1])
        self.set_achievement(triggerId=9900, type='trigger', achieve='Find02100009')
        self.set_event_ui(type=7, arg2='$02100009_BF__MAIN__1$', arg3='2000', arg4='0')
        self.set_achievement(triggerId=9900, type='trigger', achieve='02100009_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.dungeon_clear()
            return 종료(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=50000230, level=1, isPlayer=False, isSkillSet=False)
        self.set_event_ui(type=5, arg2='$02100009_BF__MAIN__0$', arg3='2000', arg4='0')
        self.destroy_monster(spawnIds=[-1])
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 유저감지
