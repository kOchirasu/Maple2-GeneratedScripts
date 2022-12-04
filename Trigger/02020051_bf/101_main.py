""" trigger/02020051_bf/101_main.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 포션사용(self.ctx)


class 포션사용(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=60001, enable=False)
        self.reset_timer(timerId='999')
        self.set_user_value(triggerId=102, key='Timmer', value=2)
        self.set_ambient_light(primary=[198,255,205])
        self.set_directional_light(diffuseColor=[255,234,193], specularColor=[255,255,255])
        self.set_user_value(triggerId=104, key='End', value=2)
        self.set_user_value(triggerId=103, key='Main', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Potion', value=1):
            return 타이머(self.ctx)


class 타이머(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='999', seconds=10, startDelay=1, interval=1)
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', script='$02020051_BF__101_MAIN__0$', duration=5684, voice='ko/Npc/00002201')
        self.remove_buff(boxId=11, skillId=90000900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 페이드아웃(self.ctx)


class 페이드아웃(trigger_api.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='999')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_ambient_light(primary=[102,86,112])
            self.set_directional_light(diffuseColor=[255,234,193], specularColor=[127,91,93])
            return 페이드인(self.ctx)


class 페이드인(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', script='$02020051_BF__101_MAIN__1$', duration=5684, voice='ko/Npc/00002201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 기간티카등장_렌덤조건(self.ctx)


class 기간티카등장_렌덤조건(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=60001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return 기간티카등장_1(self.ctx)
        if self.random_condition(rate=20):
            return 기간티카등장_2(self.ctx)
        if self.random_condition(rate=20):
            return 기간티카등장_3(self.ctx)
        if self.random_condition(rate=20):
            return 기간티카등장_4(self.ctx)
        if self.random_condition(rate=20):
            return 기간티카등장_5(self.ctx)
        if self.random_condition(rate=20):
            return 기간티카등장_6(self.ctx)


class 기간티카등장_1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 기간티카등장_2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 기간티카등장_3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 기간티카등장_4(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1004], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 기간티카등장_5(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1005], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 기간티카등장_6(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1006], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=105, key='Summon_monster', value=1)
        self.set_user_value(triggerId=106, key='Summon_monster_2', value=1)
        self.set_user_value(triggerId=102, key='Timmer', value=1)
        self.set_user_value(triggerId=104, key='End', value=1)
        self.set_event_ui(type=1, arg2='$02020051_BF__101_MAIN__2$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Potion', value=2):
            return 포션사용(self.ctx)


initial_state = 준비
