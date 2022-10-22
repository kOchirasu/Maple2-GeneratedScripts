""" trigger/02000297_bf/main2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002,1003,1004], arg2=False)
        destroy_monster(spawnIds=[1005])
        destroy_monster(spawnIds=[1006])
        destroy_monster(spawnIds=[1007])
        set_mesh(triggerIds=[107], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBarrier
        set_mesh(triggerIds=[31000,31001,31002,31003,31004,31005], visible=True, arg3=0, arg4=0, arg5=0) # Stairs
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[107], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleBarrier
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=888888, enable=True)
        move_npc(spawnId=1004, patrolName='MS2PatrolData1')
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 레논01()


class 레논01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000064, script='$02000297_BF__MAIN2__0$', arg4=2)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 벨라01()


class 벨라01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000057, script='$02000297_BF__MAIN2__1$', arg4=3)
        set_conversation(type=2, spawnId=11000057, script='$02000297_BF__MAIN2__2$', arg4=3)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9925):
            return 벨라02()


class 벨라02(state.State):
    def on_enter(self):
        move_npc(spawnId=1002, patrolName='MS2PatrolData3')
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 레논02()


class 레논02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000064, script='$02000297_BF__MAIN2__3$', arg4=2)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 레논03()

    def on_exit(self):
        set_cinematic_ui(type=4)


class 레논03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1004])
        destroy_monster(spawnIds=[1001])
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 블랙01()


class 블랙01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=1003, patrolName='MS2PatrolData0')
        set_conversation(type=2, spawnId=11000006, script='$02000297_BF__MAIN2__4$', arg4=2)
        set_conversation(type=2, spawnId=11000006, script='$02000297_BF__MAIN2__5$', arg4=2)
        set_conversation(type=2, spawnId=11000057, script='$02000297_BF__MAIN2__6$', arg4=3)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 카메라복귀()


class 카메라복귀(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1002])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=888888, enable=False)
        set_mesh(triggerIds=[107], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBarrier
        set_mesh(triggerIds=[31000,31001,31002,31003,31004,31005], visible=False, arg3=0, arg4=0, arg5=0) # Stairs
        create_monster(spawnIds=[6200], arg2=False)
        destroy_monster(spawnIds=[1003])
        destroy_monster(spawnIds=[1002])
        destroy_monster(spawnIds=[1001])
        destroy_monster(spawnIds=[1004])
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=True)
        create_monster(spawnIds=[1008], arg2=False)
        set_user_value(triggerId=999991, key='BattleStart', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[6200]):
            return 엔딩연출1()


class 엔딩연출1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31000,31001,31002,31003,31004,31005], visible=True, arg3=0, arg4=0, arg5=0) # Stairs

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 엔딩연출()


class 엔딩연출(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=888888, enable=True)
        destroy_monster(spawnIds=[1006])
        create_monster(spawnIds=[1007], arg2=False)
        move_npc(spawnId=1007, patrolName='MS2PatrolData5')
        set_skip(state=연출종료2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 블랙03()


class 블랙03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000006, script='$02000297_BF__MAIN2__7$', arg4=3)
        set_conversation(type=2, spawnId=11000064, script='$02000297_BF__MAIN2__8$', arg4=3)
        set_conversation(type=2, spawnId=11000006, script='$02000297_BF__MAIN2__9$', arg4=3)
        set_skip(state=연출종료2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11101):
            return 연출종료2()


class 연출종료2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_skip()
        select_camera(triggerId=888888, enable=False)
        destroy_monster(spawnIds=[1005])
        destroy_monster(spawnIds=[1008])
        destroy_monster(spawnIds=[1007])
        set_achievement(triggerId=9001, type='trigger', achieve='ClearKatramusSecond')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


