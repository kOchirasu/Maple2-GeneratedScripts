""" trigger/02000380_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class idle(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001064], state=2)
        set_actor(triggerId=4001, visible=True, initialSequence='ry_functobj_door_A01_Off')
        set_actor(triggerId=4003, visible=True, initialSequence='ry_functobj_door_A01_On')
        set_actor(triggerId=4007, visible=True, initialSequence='ry_functobj_door_A01_On')
        set_mesh(triggerIds=[2001,2002,2003,2004], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2005,2006,2007,2008], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2010,2011,2012], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2020,2021,2022,2023], visible=True, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_mesh(triggerIds=[2001,2002,2003,2004], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Start()

state.DungeonStart = DungeonStart


class Start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8001,8002,8003], returnView=True)
        create_monster(spawnIds=[101])
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__0$', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=11001836, script='$02000380_BF__MAIN__1$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Start_02()


class Start_02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__2$', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=11001836, script='$02000380_BF__MAIN__3$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Start_03()


class Start_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Start_03_02()


class Start_03_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003801, textId=20003801, duration=5000)
        set_mesh(triggerIds=[2001,2002,2003,2004], visible=False, arg3=0, arg4=10, arg5=10)
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__4$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Start_04()


class Start_04(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2202')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[101]):
            return Start_05()


class Start_05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__5$', arg4=3, arg5=0)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2203')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Start_06()


class Start_06(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__6$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Start_07()


class Start_07(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__7$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Start_08()


class Start_08(state.State):
    def on_enter(self):
        show_guide_summary(entityId=110, textId=40009, duration=5000) # 포탈 이용하세요
        set_mesh(triggerIds=[2010,2011,2012], visible=False, arg3=0, arg4=10, arg5=10)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return Portal_10()
        """
        <condition name="랜덤조건" arg1="33">
            <transition state="Portal_11" />
        </condition>
        """


class Portal_10(state.State):
    def on_enter(self):
        set_actor(triggerId=4001, visible=True, initialSequence='ry_functobj_door_A01_On')
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Start_09()


class Portal_11(state.State):
    def on_enter(self):
        set_actor(triggerId=4001, visible=True, initialSequence='ry_functobj_door_A01_On')
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Start_09()


class Portal_12(state.State):
    def on_enter(self):
        set_actor(triggerId=4001, visible=True, initialSequence='ry_functobj_door_A01_On')
        set_portal(portalId=12, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Start_09()


class Start_09(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__8$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='1', value=1):
            return Start_09_02()
        """
        <condition name="!유저를감지했으면" arg1="710">
            <transition state="Start_09_02" />
        </condition>
        """


class Start_09_02(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return Round_2_03()

    def on_exit(self):
        set_mesh(triggerIds=[2005,2006,2007,2008], visible=False, arg3=0, arg4=0, arg5=10)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=True, enabled=False, minimapVisible=False)


class Round_2_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Round_2_03()


class Round_2_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__9$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round_2_04()


class Round_2_04(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2205')
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__10$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round_2_05()


class Round_2_05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round_2_06()


class Round_2_06(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2207')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=705, spawnIds=[101]):
            return Round_2_08()


class Round_2_08(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__12$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round_2_09()


class Round_2_09(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__13$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round_2_10()


class Round_2_10(state.State):
    def on_enter(self):
        show_guide_summary(entityId=110, textId=40009, duration=5000) # 포탈 이용하세요
        set_mesh(triggerIds=[2013,2014,2015], visible=False, arg3=0, arg4=10, arg5=10)

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Portal_22()


class Portal_21(state.State):
    def on_enter(self):
        set_actor(triggerId=4004, visible=True, initialSequence='ry_functobj_door_A01_On')
        set_portal(portalId=21, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Round_2_11()


class Portal_22(state.State):
    def on_enter(self):
        set_actor(triggerId=4004, visible=True, initialSequence='ry_functobj_door_A01_On')
        set_portal(portalId=22, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Round_2_11()


class Round_2_11(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__14$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return Round_2_12()
        """
        <condition name="!유저를감지했으면" arg1="710">
            <transition state="Round_2_12" />
        </condition>
        """


class Round_2_12(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return Round_3_02()

    def on_exit(self):
        set_mesh(triggerIds=[2005,2006,2007,2008], visible=False, arg3=0, arg4=0, arg5=10)
        set_portal(portalId=21, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=22, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=23, visible=True, enabled=False, minimapVisible=False)


class Round_3_02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2208')
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__15$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round_3_03()


class Round_3_03(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2208')
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__16$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=706, spawnIds=[101]):
            return Round_3_04()


class Round_3_04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__17$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Clear()


class Clear(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003802, textId=20003802) # 포탈 이용하세요
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[199])
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return end()


class end(state.State):
    pass


