""" trigger/02000355_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_actor(triggerId=299, visible=True, initialSequence='Dead_Idle_A')
        create_monster(spawnIds=[2101,2102,2103,2104,2105,2106,2107,2108], arg2=False)
        set_effect(triggerIds=[600], visible=False)
        set_effect(triggerIds=[699], visible=False)
        set_mesh(triggerIds=[3999], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3900], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808], visible=False, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[7001], isEnable=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        set_effect(triggerIds=[699], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 카드반교체()

state.DungeonStart = DungeonStart


class 카드반교체(state.State):
    def on_enter(self):
        set_actor(triggerId=299, visible=False, initialSequence='Dead_Idle_A')
        create_monster(spawnIds=[2097], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카드반대사01()


class 카드반대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        set_conversation(type=2, spawnId=24001705, script='$02000355_BF__MAIN__0$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카트반이동()


class 카트반이동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7001], isEnable=True)
        set_mesh(triggerIds=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=False, arg3=0, arg4=0, arg5=0)
        select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        move_npc(spawnId=2097, patrolName='MS2PatrolData2097_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            set_mesh(triggerIds=[3900], visible=False, arg3=0, arg4=0, arg5=0)
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            select_camera(triggerId=301, enable=False)
            show_guide_summary(entityId=20003552, textId=20003552, duration=4000)
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            return 카트반소멸()


class 카트반소멸(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            create_monster(spawnIds=[2099], arg2=False)
            destroy_monster(spawnIds=[2097])
            return 종료체크()


class 종료체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099]):
            return 종료연출시작()


class 종료연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 카드반대사02()


class 카드반대사02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        set_conversation(type=2, spawnId=24001705, script='$02000355_BF__MAIN__1$', arg4=4)
        set_skip(state=연출종료2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출종료2()


class 연출종료2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            dungeon_clear()
            set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808], visible=True, arg3=0, arg4=50, arg5=2)
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            return 종료()


class 종료(state.State):
    pass


