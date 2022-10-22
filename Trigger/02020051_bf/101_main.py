""" trigger/02020051_bf/101_main.xml """
from common import *
import state


class 준비(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 포션사용()


class 포션사용(state.State):
    def on_enter(self):
        set_sound(triggerId=60001, arg2=False)
        reset_timer(timerId='999')
        set_user_value(triggerId=102, key='Timmer', value=2)
        set_ambient_light(primary=[198,255,205])
        set_directional_light(diffuseColor=[255,234,193], specularColor=[255,255,255])
        set_user_value(triggerId=104, key='End', value=2)
        set_user_value(triggerId=103, key='Main', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Potion', value=1):
            return 타이머()


class 타이머(state.State):
    def on_enter(self):
        set_timer(timerId='999', seconds=10, clearAtZero=True, display=True)
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', script='$02020051_BF__101_MAIN__0$', duration=5684, voice='ko/Npc/00002201')
        remove_buff(boxId=11, skillId=90000900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 페이드아웃()


class 페이드아웃(state.State):
    def on_enter(self):
        reset_timer(timerId='999')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_ambient_light(primary=[102,86,112])
            set_directional_light(diffuseColor=[255,234,193], specularColor=[127,91,93])
            return 페이드인()


class 페이드인(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', script='$02020051_BF__101_MAIN__1$', duration=5684, voice='ko/Npc/00002201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 기간티카등장_렌덤조건()


class 기간티카등장_렌덤조건(state.State):
    def on_enter(self):
        set_sound(triggerId=60001, arg2=True)

    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return 기간티카등장_1()
        if random_condition(rate=20):
            return 기간티카등장_2()
        if random_condition(rate=20):
            return 기간티카등장_3()
        if random_condition(rate=20):
            return 기간티카등장_4()
        if random_condition(rate=20):
            return 기간티카등장_5()
        if random_condition(rate=20):
            return 기간티카등장_6()


class 기간티카등장_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 기간티카등장_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 기간티카등장_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1003], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 기간티카등장_4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1004], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 기간티카등장_5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1005], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 기간티카등장_6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1006], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=105, key='Summon_monster', value=1)
        set_user_value(triggerId=106, key='Summon_monster_2', value=1)
        set_user_value(triggerId=102, key='Timmer', value=1)
        set_user_value(triggerId=104, key='End', value=1)
        set_event_ui(type=1, arg2='$02020051_BF__101_MAIN__2$', arg3='4000')

    def on_tick(self) -> state.State:
        if user_value(key='Potion', value=2):
            return 포션사용()


