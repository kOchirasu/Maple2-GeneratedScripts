""" trigger/02100004_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return CheckUser10_GuildRaid()


class CheckUser10_GuildRaid(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=30, clearAtZero=True, display=False, arg5=0)

    def on_tick(self) -> state.State:
        if count_users(boxId=199, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start()
        if count_users(boxId=199, boxId=10, operator='Less'):
            return MaxCount10_Wait()
        if not is_dungeon_room():
            return MaxCount10_Start()


class MaxCount10_Wait(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=3000)

    def on_tick(self) -> state.State:
        if count_users(boxId=199, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start()
        if time_expired(timerId='99'):
            return MaxCount10_Start()
        if wait_tick(waitTick=6000):
            return MaxCount10_Wait()
        if not is_dungeon_room():
            return MaxCount10_Start()


class MaxCount10_Start(state.State):
    def on_enter(self):
        reset_timer(timerId='99')

    def on_tick(self) -> state.State:
        if true():
            return state.DungeonStart()


#  설명문 출력 
class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_intro(text='$02100004_BF__MAIN__0$')
        set_skip(state=Caption01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Caption01Skip()

state.DungeonStart = DungeonStart


class Caption01Skip(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, arg4=0, arg5=0)
        close_cinematic()
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[601], visible=True)
        show_guide_summary(entityId=20002411, textId=20002411)
        set_user_value(triggerId=999993, key='BattleStart', value=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 라운드시작1()


class 라운드시작1(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002411)
        show_count_ui(text='$02100004_BF__MAIN__1$', stage=0, count=3)
        set_user_value(triggerId=999992, key='RoundStart', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드1()


class 라운드1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        set_event_ui(type=0, arg2='1,10')
        set_timer(timerId='1', seconds=20, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작2()
        if time_expired(timerId='1'):
            return 라운드시작2()

    def on_exit(self):
        reset_timer(timerId='1')


class 라운드시작2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_user_value(triggerId=999992, key='RoundStart', value=1)
        show_count_ui(text='$02100004_BF__MAIN__2$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드2()


class 라운드2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_timer(timerId='2', seconds=20, clearAtZero=True, display=True)
        move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        set_event_ui(type=0, arg2='2,10')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작3()
        if time_expired(timerId='2'):
            return 라운드시작3()

    def on_exit(self):
        reset_timer(timerId='2')


class 라운드시작3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_user_value(triggerId=999992, key='RoundStart', value=1)
        show_count_ui(text='$02100004_BF__MAIN__3$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드3()


class 라운드3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_timer(timerId='3', seconds=20, clearAtZero=True, display=True)
        move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        set_event_ui(type=0, arg2='3,10')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작4()
        if time_expired(timerId='3'):
            return 라운드시작4()

    def on_exit(self):
        reset_timer(timerId='3')


class 라운드시작4(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_user_value(triggerId=999992, key='RoundStart', value=1)
        show_count_ui(text='$02100004_BF__MAIN__4$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드4()


class 라운드4(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_timer(timerId='4', seconds=20, clearAtZero=True, display=True)
        move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        set_event_ui(type=0, arg2='4,10')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작5()
        if time_expired(timerId='4'):
            return 라운드시작5()

    def on_exit(self):
        reset_timer(timerId='4')


class 라운드시작5(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_user_value(triggerId=999992, key='RoundStart', value=1)
        show_count_ui(text='$02100004_BF__MAIN__5$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드5()


class 라운드5(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_timer(timerId='5', seconds=20, clearAtZero=True, display=True)
        move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        set_event_ui(type=0, arg2='5,10')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작6()
        if time_expired(timerId='5'):
            return 라운드시작6()

    def on_exit(self):
        reset_timer(timerId='5')


class 라운드시작6(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_user_value(triggerId=999992, key='RoundStart', value=1)
        show_count_ui(text='$02100004_BF__MAIN__6$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드6()


class 라운드6(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_timer(timerId='6', seconds=20, clearAtZero=True, display=True)
        move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        set_event_ui(type=0, arg2='6,10')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작7()
        if time_expired(timerId='6'):
            return 라운드시작7()

    def on_exit(self):
        reset_timer(timerId='6')


class 라운드시작7(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_user_value(triggerId=999992, key='RoundStart', value=1)
        show_count_ui(text='$02100004_BF__MAIN__7$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드7()


class 라운드7(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_timer(timerId='7', seconds=20, clearAtZero=True, display=True)
        move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        set_event_ui(type=0, arg2='7,10')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작8()
        if time_expired(timerId='7'):
            return 라운드시작8()

    def on_exit(self):
        reset_timer(timerId='7')


class 라운드시작8(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_user_value(triggerId=999992, key='RoundStart', value=1)
        show_count_ui(text='$02100004_BF__MAIN__8$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드8()


class 라운드8(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_timer(timerId='8', seconds=20, clearAtZero=True, display=True)
        move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        set_event_ui(type=0, arg2='8,10')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작9()
        if time_expired(timerId='8'):
            return 라운드시작9()

    def on_exit(self):
        reset_timer(timerId='8')


class 라운드시작9(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_user_value(triggerId=999992, key='RoundStart', value=1)
        show_count_ui(text='$02100004_BF__MAIN__9$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드9()


class 라운드9(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_timer(timerId='9', seconds=20, clearAtZero=True, display=True)
        move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        set_event_ui(type=0, arg2='9,10')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=199, spawnIds=[0]):
            return 라운드시작10()
        if time_expired(timerId='9'):
            return 라운드시작10()

    def on_exit(self):
        reset_timer(timerId='9')


class 라운드시작10(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        create_monster(spawnIds=[2000], arg2=True)
        show_count_ui(text='$02100004_BF__MAIN__10$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드10()


class 라운드10(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_timer(timerId='10', seconds=150, clearAtZero=True, display=True)
        move_random_user(mapId=2100004, portalId=99, triggerId=101, count=1)
        set_event_ui(type=0, arg2='10,10')
        set_user_value(triggerId=999995, key='LastRoundStart', value=1) # 트로피 전용

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2000]):
            reset_timer(timerId='10')
            return 성공()
        if time_expired(timerId='10'):
            return 실패()

    def on_exit(self):
        set_event_ui(type=0, arg2='0,0')
        set_user_value(triggerId=999995, key='LastRoundEnd', value=1) # 트로피 전용


class 성공(state.State):
    def on_enter(self):
        set_user_value(triggerId=999993, key='BattleEnd', value=1)
        destroy_monster(spawnIds=[-1])
        set_achievement(triggerId=9900, type='trigger', achieve='Find02100004')
        set_event_ui(type=7, arg2='$02000251_BF__TRIGGER_01_01__0$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            dungeon_clear()
            return 종료()


class 실패(state.State):
    def on_enter(self):
        set_event_ui(type=5, arg2='$02100004_BF__MAIN__11$', arg3='2000', arg4='0')
        set_user_value(triggerId=999993, key='BattleEnd', value=1)
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            dungeon_fail()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


