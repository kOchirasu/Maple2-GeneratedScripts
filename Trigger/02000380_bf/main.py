""" trigger/02000380_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001064], state=2)
        self.set_actor(triggerId=4001, visible=True, initialSequence='ry_functobj_door_A01_Off')
        self.set_actor(triggerId=4003, visible=True, initialSequence='ry_functobj_door_A01_On')
        self.set_actor(triggerId=4007, visible=True, initialSequence='ry_functobj_door_A01_On')
        self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2005,2006,2007,2008], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2010,2011,2012], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2020,2021,2022,2023], visible=True, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=701, boxId=1):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8001,8002,8003], returnView=True)
        self.create_monster(spawnIds=[101])
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__0$', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=11001836, script='$02000380_BF__MAIN__1$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Start_02(self.ctx)


class Start_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__2$', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=11001836, script='$02000380_BF__MAIN__3$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Start_03(self.ctx)


class Start_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Start_03_02(self.ctx)


class Start_03_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003801, textId=20003801, duration=5000)
        self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=False, arg3=0, delay=10, scale=10)
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__4$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Start_04(self.ctx)


class Start_04(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[101]):
            return Start_05(self.ctx)


class Start_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__5$', arg4=3, arg5=0)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Start_06(self.ctx)


class Start_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__6$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Start_07(self.ctx)


class Start_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__7$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Start_08(self.ctx)


class Start_08(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=110, textId=40009, duration=5000) # 포탈 이용하세요
        self.set_mesh(triggerIds=[2010,2011,2012], visible=False, arg3=0, delay=10, scale=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=33):
            return Portal_10(self.ctx)
        """
        <condition name="랜덤조건" arg1="33">
            <transition state="Portal_11" />
        </condition>
        """


class Portal_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4001, visible=True, initialSequence='ry_functobj_door_A01_On')
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Start_09(self.ctx)


class Portal_11(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4001, visible=True, initialSequence='ry_functobj_door_A01_On')
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Start_09(self.ctx)


class Portal_12(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4001, visible=True, initialSequence='ry_functobj_door_A01_On')
        self.set_portal(portalId=12, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Start_09(self.ctx)


class Start_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__8$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=1, value=1):
            return Start_09_02(self.ctx)
        """
        <condition name="!유저를감지했으면" arg1="710">
            <transition state="Start_09_02" />
        </condition>
        """


class Start_09_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=703, boxId=1):
            return Round_2_03(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[2005,2006,2007,2008], visible=False, arg3=0, delay=0, scale=10)
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13, visible=True, enable=False, minimapVisible=False)


class Round_2_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Round_2_03(self.ctx)


class Round_2_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__9$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round_2_04(self.ctx)


class Round_2_04(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2205')
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__10$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round_2_05(self.ctx)


class Round_2_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round_2_06(self.ctx)


class Round_2_06(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2207')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=705, spawnIds=[101]):
            return Round_2_08(self.ctx)


class Round_2_08(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__12$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round_2_09(self.ctx)


class Round_2_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__13$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round_2_10(self.ctx)


class Round_2_10(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=110, textId=40009, duration=5000) # 포탈 이용하세요
        self.set_mesh(triggerIds=[2013,2014,2015], visible=False, arg3=0, delay=10, scale=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Portal_22(self.ctx)


class Portal_21(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4004, visible=True, initialSequence='ry_functobj_door_A01_On')
        self.set_portal(portalId=21, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Round_2_11(self.ctx)


class Portal_22(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4004, visible=True, initialSequence='ry_functobj_door_A01_On')
        self.set_portal(portalId=22, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Round_2_11(self.ctx)


class Round_2_11(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__14$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return Round_2_12(self.ctx)
        """
        <condition name="!유저를감지했으면" arg1="710">
            <transition state="Round_2_12" />
        </condition>
        """


class Round_2_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=703, boxId=1):
            return Round_3_02(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[2005,2006,2007,2008], visible=False, arg3=0, delay=0, scale=10)
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=22, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=23, visible=True, enable=False, minimapVisible=False)


class Round_3_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2208')
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__15$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round_3_03(self.ctx)


class Round_3_03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2208')
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__16$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=706, spawnIds=[101]):
            return Round_3_04(self.ctx)


class Round_3_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000380_BF__MAIN__17$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Clear(self.ctx)


class Clear(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003802, textId=20003802) # 포탈 이용하세요
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[199])
        self.set_portal(portalId=5, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
