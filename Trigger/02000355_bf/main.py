""" trigger/02000355_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=299, visible=True, initialSequence='Dead_Idle_A')
        self.create_monster(spawnIds=[2101,2102,2103,2104,2105,2106,2107,2108], animationEffect=False)
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[699], visible=False)
        self.set_mesh(triggerIds=[3999], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3900], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808], visible=False, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[7001], enable=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.set_effect(triggerIds=[699], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 카드반교체(self.ctx)


class 카드반교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=299, visible=False, initialSequence='Dead_Idle_A')
        self.create_monster(spawnIds=[2097], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카드반대사01(self.ctx)


class 카드반대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[600], visible=True)
        self.set_conversation(type=2, spawnId=24001705, script='$02000355_BF__MAIN__0$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카트반이동(self.ctx)


class 카트반이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[7001], enable=True)
        self.set_mesh(triggerIds=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=False, arg3=0, delay=0, scale=0)
        self.select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=2097, patrolName='MS2PatrolData2097_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            self.set_mesh(triggerIds=[3900], visible=False, arg3=0, delay=0, scale=0)
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            self.select_camera(triggerId=301, enable=False)
            self.show_guide_summary(entityId=20003552, textId=20003552, duration=4000)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            return 카트반소멸(self.ctx)


class 카트반소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            self.create_monster(spawnIds=[2099], animationEffect=False)
            self.destroy_monster(spawnIds=[2097])
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2099]):
            return 종료연출시작(self.ctx)


class 종료연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 카드반대사02(self.ctx)


class 카드반대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[600], visible=True)
        self.set_conversation(type=2, spawnId=24001705, script='$02000355_BF__MAIN__1$', arg4=4)
        self.set_skip(state=연출종료2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출종료2(self.ctx)


class 연출종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            self.dungeon_clear()
            self.set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808], visible=True, arg3=0, delay=50, scale=2)
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
