""" trigger/02020061_bf/battle_3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='BossClear', value=0)
        set_user_value(triggerId=99990013, key='BossClear', value=0)
        set_user_value(triggerId=99990013, key='BombPhase', value=0)
        set_user_value(triggerId=99990009, key='BossObjectStart', value=0)
        set_user_value(triggerId=99990010, key='BossObjectStart', value=0)
        set_user_value(triggerId=99990011, key='BossObjectStart', value=0)
        set_user_value(triggerId=99990012, key='BossObjectStart', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='BossPhase', value=1):
            return 보스_추가대사()


class 보스_추가대사(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020061_BF__BATTLE_3__0$')
            return 보스랜덤픽()


class 보스랜덤픽(state.State):
    def on_enter(self):
        add_buff(boxIds=[9002], skillId=70002371, level=1, arg5=False) # <유저 웨폰 오브젝트 떨구기>

    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return 보스소환1()
        if random_condition(rate=16):
            return 보스소환2()
        if random_condition(rate=17):
            return 보스소환3()
        if random_condition(rate=16):
            return 보스소환4()
        if random_condition(rate=17):
            return 보스소환5()
        if random_condition(rate=17):
            return 보스소환6()


class 보스소환1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[921], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BossPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[921]):
            return 보스군단_클리어()
        if all_of():
            return 보스_무적페이즈()


class 보스소환2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[922], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BossPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[922]):
            return 보스군단_클리어()
        if all_of():
            return 보스_무적페이즈()


class 보스소환3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[923], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BossPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[923]):
            return 보스군단_클리어()
        if all_of():
            return 보스_무적페이즈()


class 보스소환4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[924], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BossPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[924]):
            return 보스군단_클리어()
        if all_of():
            return 보스_무적페이즈()


class 보스소환5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[925], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BossPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[925]):
            return 보스군단_클리어()
        if all_of():
            return 보스_무적페이즈()


class 보스소환6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[926], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BossPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[926]):
            return 보스군단_클리어()
        if all_of():
            return 보스_무적페이즈()


class 보스_무적페이즈(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020061_BF__BATTLE_3__1$', arg3='5000')
        create_monster(spawnIds=[711,712,713,714], arg2=False)
        set_user_value(triggerId=99990009, key='BossObjectStart', value=1)
        set_user_value(triggerId=99990010, key='BossObjectStart', value=1)
        set_user_value(triggerId=99990011, key='BossObjectStart', value=1)
        set_user_value(triggerId=99990012, key='BossObjectStart', value=1)
        set_user_value(triggerId=99990013, key='BombPhase', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='BossPhase', value=2):
            return 대기()
        if all_of():
            return 보스군단_클리어()
        if wait_tick(waitTick=5000):
            return 보스_무적페이즈_대사1()


class 보스_무적페이즈_대사1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020061_BF__BATTLE_3__2$')

    def on_tick(self) -> state.State:
        if user_value(key='BossPhase', value=2):
            return 대기()
        if all_of():
            return 보스군단_클리어()
        if wait_tick(waitTick=5000):
            return 보스_무적페이즈_대사2()


class 보스_무적페이즈_대사2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020061_BF__BATTLE_3__3$')

    def on_tick(self) -> state.State:
        if user_value(key='BossPhase', value=2):
            return 대기()
        if all_of():
            return 보스군단_클리어()


class 보스군단_클리어(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='BossClear', value=1)
        set_user_value(triggerId=99990013, key='BossClear', value=1)
        set_user_value(triggerId=99990013, key='BombPhase', value=0)
        set_user_value(triggerId=99990009, key='BossObjectStart', value=0)
        set_user_value(triggerId=99990010, key='BossObjectStart', value=0)
        set_user_value(triggerId=99990011, key='BossObjectStart', value=0)
        set_user_value(triggerId=99990012, key='BossObjectStart', value=0)


