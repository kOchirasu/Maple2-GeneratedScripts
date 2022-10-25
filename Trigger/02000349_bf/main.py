""" trigger/02000349_bf/main.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001])
        self.set_actor(triggerId=201, visible=True, initialSequence='Idle_A')
        self.set_actor(triggerId=202, visible=True, initialSequence='Idle_A')
        self.set_actor(triggerId=203, visible=True, initialSequence='Idle_A')
        self.set_actor(triggerId=204, visible=True, initialSequence='Idle_A')
        self.set_actor(triggerId=205, visible=True, initialSequence='Idle_A')
        self.set_actor(triggerId=206, visible=True, initialSequence='Idle_A')
        self.set_actor(triggerId=207, visible=True, initialSequence='Idle_A')
        self.set_interact_object(triggerIds=[10000806], state=2)
        self.set_interact_object(triggerIds=[10000806], state=2)
        self.set_interact_object(triggerIds=[10000807], state=2)
        self.set_interact_object(triggerIds=[10000808], state=2)
        self.set_interact_object(triggerIds=[10000809], state=2)
        self.set_interact_object(triggerIds=[10000810], state=2)
        self.set_interact_object(triggerIds=[10000811], state=2)
        self.set_interact_object(triggerIds=[10000812], state=2)
        self.set_interact_object(triggerIds=[13000014], state=2)
        self.set_mesh(triggerIds=[39101,39102,39103,39104,39105,39106], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[600], visible=False) # fog 500
        self.set_effect(triggerIds=[601], visible=False) # fog 1000
        self.set_effect(triggerIds=[602], visible=False) # fog 1500
        self.set_effect(triggerIds=[6101], visible=False)
        self.set_effect(triggerIds=[6102], visible=False)
        self.set_effect(triggerIds=[6103], visible=False)
        self.set_effect(triggerIds=[6104], visible=False)
        self.set_effect(triggerIds=[6105], visible=False)
        self.set_effect(triggerIds=[6106], visible=False)
        self.set_effect(triggerIds=[6107], visible=False)
        self.set_effect(triggerIds=[6108], visible=False)
        self.set_effect(triggerIds=[6201], visible=False)
        self.set_effect(triggerIds=[6202], visible=False)
        self.set_effect(triggerIds=[6203], visible=False)
        self.set_effect(triggerIds=[6204], visible=False)
        self.set_effect(triggerIds=[6205], visible=False)
        self.set_skill(triggerIds=[701], enable=False)
        self.set_skill(triggerIds=[702], enable=False)
        self.set_skill(triggerIds=[703], enable=False)
        self.set_skill(triggerIds=[704], enable=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_agent(triggerIds=[901], visible=True)
        self.set_agent(triggerIds=[902], visible=True)
        self.set_agent(triggerIds=[903], visible=True)
        self.set_agent(triggerIds=[904], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='KatvanIntroMovie.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 진행01벽제거(self.ctx)


class 진행01벽제거(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=False, initialSequence='Idle_A')
        self.set_interact_object(triggerIds=[10000806], state=1)
        self.show_guide_summary(entityId=20003492, textId=20003492)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000806], stateValue=0):
            self.hide_guide_summary(entityId=20003492)
            self.set_mesh(triggerIds=[39101], visible=False, arg3=0, delay=0, scale=0)
            return 진행01몬스터(self.ctx)


class 진행01몬스터(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001,1002,1003], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1101]):
            return 진행01오브젝트(self.ctx)


class 진행01오브젝트(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003496, textId=20003496)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(triggerId=202, visible=False, initialSequence='Idle_A')
        self.set_interact_object(triggerIds=[10000807], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000807], stateValue=0):
            self.hide_guide_summary(entityId=20003496)
            return 진행02몬스터(self.ctx)


class 진행02몬스터(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[39102], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1004,1005,1006], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1102]):
            return 진행02오브젝트(self.ctx)


class 진행02오브젝트(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003497, textId=20003497)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(triggerId=203, visible=False, initialSequence='Idle_A')
        self.set_interact_object(triggerIds=[10000808], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000808], stateValue=0):
            self.hide_guide_summary(entityId=20003497)
            return 진행03몬스터(self.ctx)


class 진행03몬스터(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[39103], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1007,1008,1009], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1103]):
            return 진행04오브젝트(self.ctx)


class 진행04오브젝트(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003498, textId=20003498)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(triggerId=204, visible=False, initialSequence='Idle_A')
        self.set_interact_object(triggerIds=[10000809], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000809], stateValue=0):
            self.hide_guide_summary(entityId=20003498)
            return 진행04몬스터(self.ctx)


class 진행04몬스터(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[39104], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1010,1011,1012], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1104]):
            return 진행05오브젝트(self.ctx)


class 진행05오브젝트(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003499, textId=20003499)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(triggerId=205, visible=False, initialSequence='Idle_A')
        self.set_interact_object(triggerIds=[10000810], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000810], stateValue=0):
            self.hide_guide_summary(entityId=20003499)
            return 진행05몬스터(self.ctx)


class 진행05몬스터(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[39105], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1013,1014,1015], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1105]):
            return 진행06오브젝트(self.ctx)


class 진행06오브젝트(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003500, textId=20003500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(triggerId=206, visible=False, initialSequence='Idle_A')
        self.set_interact_object(triggerIds=[10000811], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000811], stateValue=0):
            self.set_achievement(triggerId=100, type='trigger', achieve='rescue_boroboro')
            self.hide_guide_summary(entityId=20003500)
            return 진행06몬스터(self.ctx)


class 진행06몬스터(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[39106], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1016,1017,1018,1019,1020], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1106]):
            return 레논오브젝트(self.ctx)


class 레논오브젝트(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003495, textId=20003495)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(triggerId=207, visible=False, initialSequence='Idle_A')
        self.set_interact_object(triggerIds=[10000812], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000812], stateValue=0):
            self.destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
            self.hide_guide_summary(entityId=20003495)
            return 레논구출(self.ctx)


class 레논구출(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.set_skip(state=레논구출종료)
        self.destroy_monster(spawnIds=[2001])
        self.create_monster(spawnIds=[2002])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 레논대사01(self.ctx)


class 레논대사01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6101], visible=True)
        self.set_conversation(type=2, spawnId=11000064, script='$02000349_BF__MAIN__3$', arg4=3)
        self.set_skip(state=레논구출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 레논대사02(self.ctx)


class 레논대사02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6102], visible=True)
        self.set_conversation(type=2, spawnId=11000064, script='$02000349_BF__MAIN__4$', arg4=3)
        self.set_skip(state=레논구출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 레논구출종료(self.ctx)


class 레논구출종료(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 진행07(self.ctx)


class 진행07(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData2002_AB')
        self.show_guide_summary(entityId=20003501, textId=20003501, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=127, spawnIds=[2002]):
            return 진행07몬스터(self.ctx)


class 진행07몬스터(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1021])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1021]):
            return 진행08(self.ctx)


class 진행08(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData2002_C')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=128, spawnIds=[2002]):
            self.set_skill(triggerIds=[701], enable=True)
            self.set_effect(triggerIds=[6201], visible=True)
            self.destroy_monster(spawnIds=[2002])
            self.create_monster(spawnIds=[2003])
            return 진행09(self.ctx)


class 진행09(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData2002_C')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[129]):
            return 진행09몬스터(self.ctx)


class 진행09몬스터(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2003, patrolName='MS2PatrolData2003_A')
        self.create_monster(spawnIds=[1022])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1022]):
            return 진행10(self.ctx)


class 진행10(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2003, patrolName='MS2PatrolData2003_B')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=130, spawnIds=[2003]):
            self.set_skill(triggerIds=[702], enable=True)
            self.set_effect(triggerIds=[6202], visible=True)
            self.destroy_monster(spawnIds=[2003])
            self.create_monster(spawnIds=[2004])
            return 진행11(self.ctx)


class 진행11(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[131]):
            return 진행11몬스터(self.ctx)


class 진행11몬스터(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2004, patrolName='MS2PatrolData2004_A')
        self.create_monster(spawnIds=[1023])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1023]):
            return 진행12(self.ctx)


class 진행12(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2004, patrolName='MS2PatrolData2004_B')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=132, spawnIds=[2004]):
            self.set_skill(triggerIds=[703], enable=True)
            self.set_effect(triggerIds=[6203], visible=True)
            self.destroy_monster(spawnIds=[2004])
            self.create_monster(spawnIds=[2005])
            return 진행13(self.ctx)


class 진행13(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[133]):
            return 진행13몬스터(self.ctx)


class 진행13몬스터(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2005, patrolName='MS2PatrolData2005_A')
        self.create_monster(spawnIds=[1024])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1024]):
            return 진행14(self.ctx)


class 진행14(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2005, patrolName='MS2PatrolData2005_B')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=134, spawnIds=[2005]):
            self.set_skill(triggerIds=[704], enable=True)
            self.set_effect(triggerIds=[6204], visible=True)
            self.destroy_monster(spawnIds=[2005])
            self.create_monster(spawnIds=[2007])
            return 진행15(self.ctx)


class 진행15(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[135]):
            return 카트반연출딜레이(self.ctx)


class 카트반연출딜레이(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1099], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카드반연출시작(self.ctx)


class 카드반연출시작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=302, enable=True)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카드반대사01(self.ctx)


class 카드반대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__5$', arg4=3)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카드반대사02(self.ctx)


class 카드반대사02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__6$', arg4=4)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 레논대사05(self.ctx)


class 레논대사05(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=303, enable=True)
        self.set_conversation(type=2, spawnId=11000064, script='$02000349_BF__MAIN__7$', arg4=4)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카드반대사03(self.ctx)


class 카드반대사03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__8$', arg4=6)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 카드반대사04(self.ctx)


class 카드반대사04(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__9$', arg4=8)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 카드반대사05(self.ctx)


class 카드반대사05(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.create_monster(spawnIds=[1025,1026], animationEffect=False)
        self.set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__10$', arg4=7)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 카드반연출종료(self.ctx)


class 카드반연출종료(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003502, textId=20003502, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.destroy_monster(spawnIds=[1025,1026])
        self.destroy_monster(spawnIds=[1099])
        self.set_agent(triggerIds=[901], visible=False)
        self.set_agent(triggerIds=[902], visible=False)
        self.set_agent(triggerIds=[903], visible=False)
        self.set_agent(triggerIds=[904], visible=False)
        self.destroy_monster(spawnIds=[2007])
        self.create_monster(spawnIds=[2006])
        self.select_camera_path(pathIds=[302], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 진행16(self.ctx)


class 진행16(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=302, enable=False)
        self.select_camera(triggerId=303, enable=False)
        self.move_npc(spawnId=2006, patrolName='MS2PatrolData2006_A')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=136, spawnIds=[2006]):
            return 진행17(self.ctx)


class 진행17(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1025,1026], animationEffect=False)
        self.create_monster(spawnIds=[1099], animationEffect=False)
        self.set_agent(triggerIds=[901], visible=True)
        self.set_agent(triggerIds=[902], visible=True)
        self.set_agent(triggerIds=[903], visible=True)
        self.set_agent(triggerIds=[904], visible=True)
        self.set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], visible=False, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1099]):
            return 던전종료연출딜레이(self.ctx)


class 던전종료연출딜레이(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2006])
        self.create_monster(spawnIds=[2008])
        self.destroy_monster(spawnIds=[1025,1026])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 던전종료연출종료(self.ctx)


class 던전종료연출종료(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2008, script='$02000349_BF__MAIN__11$', arg4=3)
        self.dungeon_clear()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 포털생성(self.ctx)


class 포털생성(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2008, script='$02000349_BF__MAIN__13$', arg4=4)
        self.move_npc(spawnId=2008, patrolName='MS2PatrolData2008_A')
        self.set_effect(triggerIds=[6205], visible=True)
        # action name="ShowGuideSummary" entityID="20003493" textID="20003493"
        self.set_mesh(triggerIds=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=True, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.destroy_monster(spawnIds=[2008])
            self.hide_guide_summary(entityId=20003493)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
