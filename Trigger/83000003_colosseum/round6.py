""" trigger/83000003_colosseum/round6.xml """
from common import *
import state


#  6라운드 오필리아 
class 대기(state.State):
    def on_enter(self):
        set_sound(triggerId=11000, arg2=False)
        set_sound(triggerId=11001, arg2=False)
        set_sound(triggerId=12000, arg2=False)
        set_sound(triggerId=12001, arg2=False)
        set_sound(triggerId=13000, arg2=False)
        set_sound(triggerId=13001, arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='StartRound6', value=1):
            return 시작딜레이()


class 시작딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 라운드조건체크()


class 라운드조건체크(state.State):
    def on_tick(self) -> state.State:
        if dungeon_round_require(round=6):
            side_npc_talk(type='talk', npcId=11004288, illust='nagi_normal', script='$83000002_COLOSSEUM__ROUND6__0$', duration=5000)
            return 라운드대기()
        if true():
            side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND6__1$', duration=3000)
            debug_string(string='던전 요구 아이템 점수를 달성 못해 실패 처리 됩니다.')
            return FailRound()


class 라운드대기(state.State):
    def on_enter(self):
        set_sound(triggerId=11000, arg2=True)
        set_sound(triggerId=11001, arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            side_npc_talk(type='cutin', illust='Ophelia_normal', duration=3000)
            show_round_ui(round=6, duration=3000)
            return 몬스터스폰대기()


class 몬스터스폰대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터스폰()


class 몬스터스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[106], arg2=False)
        add_buff(boxIds=[106], skillId=69000501, level=1, arg4=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        show_count_ui(text='$83000002_COLOSSEUM__ROUND6__2$', count=3, soundType=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 전투시작()


class 전투시작(state.State):
    def on_enter(self):
        lock_my_pc(isLock=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 스폰대사()


class 스폰대사(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=106, msg='$83000002_COLOSSEUM__ROUND6__3$', duration=3000)
        set_timer(timerId='LimitTimer', seconds=120, clearAtZero=True)
        set_npc_duel_hp_bar(isOpen=True, spawnId=[106], durationTick=120000, npcHpStep=10)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106]):
            add_balloon_talk(spawnId=106, msg='$83000002_COLOSSEUM__ROUND6__4$', duration=3000)
            set_npc_duel_hp_bar(isOpen=False, spawnId=[106])
            return ClearRoundDelay()
        if time_expired(timerId='LimitTimer'):
            side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND6__5$', duration=3000)
            destroy_monster(spawnIds=[106])
            set_npc_duel_hp_bar(isOpen=False, spawnId=[106])
            return FailRoundDelay()
        if user_detected(boxIds=[902]):
            side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND6__6$', duration=3000)
            destroy_monster(spawnIds=[106])
            set_npc_duel_hp_bar(isOpen=False, spawnId=[106])
            return FailRoundDelay()
        if not user_detected(boxIds=[904]):
            side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND6__7$', duration=3000)
            destroy_monster(spawnIds=[106])
            set_npc_duel_hp_bar(isOpen=False, spawnId=[106])
            return FailRoundDelay()


class ClearRoundDelay(state.State):
    def on_enter(self):
        lock_my_pc(isLock=True)
        set_sound(triggerId=12000, arg2=True)
        set_sound(triggerId=12001, arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            add_buff(boxIds=[904], skillId=69000503, level=1, arg4=False, arg5=False)
            set_event_ui(type=3, arg2='$83000002_COLOSSEUM__ROUND6__8$', arg3='3000')
            return ClearRound()


class FailRoundDelay(state.State):
    def on_enter(self):
        set_sound(triggerId=13000, arg2=True)
        set_sound(triggerId=13001, arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=5, arg2='$83000002_COLOSSEUM__ROUND6__9$', arg3='3000')
            return FailRound()


class ClearRound(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user_to_pos(pos=[300,-225,1500], rot=[0,0,270])
            side_npc_talk(type='talk', npcId=11004288, illust='nagi_normal', script='$83000002_COLOSSEUM__ROUND6__10$', duration=3000)
            set_user_value(triggerId=900001, key='StartRound6', value=2)
            return 이동대기()


class 이동대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            move_user_path(patrolName='MS2PatrolData_01')
            return 대기()


class FailRound(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=900001, key='StartRound6', value=3)
            return 대기()

