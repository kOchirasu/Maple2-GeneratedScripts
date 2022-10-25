""" trigger/52000076_qd/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001], animationEffect=False)
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
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=11, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001901.xml')
        self.set_onetime_effect(id=12, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001902.xml')
        self.set_onetime_effect(id=13, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001903.xml')
        self.set_onetime_effect(id=14, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001904.xml')
        self.set_onetime_effect(id=15, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001905.xml')
        self.set_onetime_effect(id=16, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001906.xml')
        self.set_onetime_effect(id=17, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001907.xml')
        self.set_onetime_effect(id=18, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001908.xml')
        self.set_onetime_effect(id=19, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001909.xml')
        self.set_onetime_effect(id=20, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001910.xml')
        self.set_user_value(key='saveEveIntheDark', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100]):
            return CheckQuestCondition(self.ctx)


class CheckQuestCondition(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[100], questIds=[40002688], questStates=[1]):
            return DungeonReady(self.ctx)
        if self.quest_user_detected(boxIds=[100], questIds=[40002688], questStates=[2]):
            return QuestOnGoing01(self.ctx)
        if self.wait_tick(waitTick=2000):
            return DungeonReady(self.ctx)


# 다음 맵 이동
class QuestOnGoing01(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000076, portalId=30, boxId=100)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return QuestOnGoing02(self.ctx)


class QuestOnGoing02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=320, enable=True)
        self.create_monster(spawnIds=[1310,1410], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return QuestOnGoing03(self.ctx)


class QuestOnGoing03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return EveTalk30(self.ctx)


# 던전 진행
class DungeonReady(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return DungeonStart(self.ctx)


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
        self.create_monster(spawnIds=[2002], animationEffect=False)

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
        self.create_monster(spawnIds=[1021], animationEffect=False)

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
            self.create_monster(spawnIds=[2003], animationEffect=False)
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
        self.create_monster(spawnIds=[1022], animationEffect=False)

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
            self.create_monster(spawnIds=[2004], animationEffect=False)
            return 진행11(self.ctx)


class 진행11(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[131]):
            return 진행11몬스터(self.ctx)


class 진행11몬스터(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2004, patrolName='MS2PatrolData2004_A')
        self.create_monster(spawnIds=[1023], animationEffect=False)

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
            self.create_monster(spawnIds=[2005], animationEffect=False)
            return 진행13(self.ctx)


class 진행13(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[133]):
            return 진행13몬스터(self.ctx)


class 진행13몬스터(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2005, patrolName='MS2PatrolData2005_A')
        self.create_monster(spawnIds=[1024], animationEffect=False)

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
            self.create_monster(spawnIds=[2007], animationEffect=False)
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
        self.set_scene_skip(state=카드반연출종료, action='nextState')
        self.set_effect(triggerIds=[602], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=302, enable=True)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카드반대사01(self.ctx)


class 카드반대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__5$', arg4=3)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카드반대사02(self.ctx)


class 카드반대사02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__6$', arg4=4)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 레논대사05(self.ctx)


class 레논대사05(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=303, enable=True)
        self.set_conversation(type=2, spawnId=11000064, script='$02000349_BF__MAIN__7$', arg4=4)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카드반대사03(self.ctx)


class 카드반대사03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__8$', arg4=6)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 카드반대사04(self.ctx)


class 카드반대사04(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__9$', arg4=8)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 카드반대사05(self.ctx)


class 카드반대사05(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.create_monster(spawnIds=[1025,1026], animationEffect=False)
        self.set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__10$', arg4=7)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 카드반연출종료(self.ctx)


class 카드반연출종료(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.show_guide_summary(entityId=20003502, textId=20003502, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.destroy_monster(spawnIds=[1025,1026])
        self.destroy_monster(spawnIds=[1099])
        self.set_agent(triggerIds=[901], visible=False)
        self.set_agent(triggerIds=[902], visible=False)
        self.set_agent(triggerIds=[903], visible=False)
        self.set_agent(triggerIds=[904], visible=False)
        self.destroy_monster(spawnIds=[2007])
        self.create_monster(spawnIds=[2006], animationEffect=False)
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
            return BossBattleStart01(self.ctx)


# Boss 전투 개시
class BossBattleStart01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1025,1026], animationEffect=False)
        self.create_monster(spawnIds=[1099], animationEffect=False)
        self.set_agent(triggerIds=[901], visible=True)
        self.set_agent(triggerIds=[902], visible=True)
        self.set_agent(triggerIds=[903], visible=True)
        self.set_agent(triggerIds=[904], visible=True)
        self.set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], visible=False, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='saveEveIntheDark', value=1):
            return BossNpcChange01(self.ctx)
        if self.monster_dead(boxIds=[1099]):
            return BossNpcChange01(self.ctx)


class BossNpcChange01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_agent(triggerIds=[901], visible=False)
        self.set_agent(triggerIds=[902], visible=False)
        self.set_agent(triggerIds=[903], visible=False)
        self.set_agent(triggerIds=[904], visible=False)
        self.set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return BossNpcChange02(self.ctx)


class BossNpcChange02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1025,1026,1099,2006])
        self.move_user(mapId=52000076, portalId=20, boxId=100)
        self.create_monster(spawnIds=[1200,1300], animationEffect=False)
        self.select_camera(triggerId=310, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return BossNpcChange03(self.ctx)


class BossNpcChange03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawnId=1200, sequenceName='Attack_Idle_A', duration=15000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return BossNpcChange04(self.ctx)


class BossNpcChange04(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=311, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return EveEnter01(self.ctx)


class EveEnter01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1400], animationEffect=False)
        self.move_npc(spawnId=1400, patrolName='MS2PatrolData_1400')
        self.select_camera(triggerId=312, enable=True)
        self.set_conversation(type=1, spawnId=1400, script='$52000076_QD__MAIN__0$', arg4=4, arg5=2)
        self.set_scene_skip(state=EvilKatvanLeave04, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return EveEnter02(self.ctx)


class EveEnter02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=313, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return EveEnter03(self.ctx)


class EveEnter03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1300, patrolName='MS2PatrolData_1300')
        self.move_user_path(patrolName='MS2PatrolData_1000')
        self.set_conversation(type=1, spawnId=1300, script='$52000076_QD__MAIN__1$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=0, script='$52000076_QD__MAIN__2$', arg4=2, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return EveEnter04(self.ctx)


class EveEnter04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=11, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001901.xml')
        self.set_conversation(type=1, spawnId=1200, script='$52000076_QD__MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EveTalk01(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=11, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001901.xml')


class EveTalk01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=314, enable=True)
        self.add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__4$', duration=5000, align='center')
        self.set_npc_emotion_sequence(spawnId=1400, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EveTalk01Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return EveTalk01Skip(self.ctx)


class EveTalk01Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1400, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EveTalk02(self.ctx)


class EveTalk02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__5$', duration=5000, align='center')
        self.set_npc_emotion_sequence(spawnId=1400, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EveTalk02Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return EveTalk02Skip(self.ctx)


class EveTalk02Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1400, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LennonTalk01(self.ctx)


class LennonTalk01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__6$', arg4=5) # 레논
        self.set_npc_emotion_sequence(spawnId=1300, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="LennonTalk01Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return LennonTalk01Skip(self.ctx)


class LennonTalk01Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1300, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LennonTurnAround01(self.ctx)


class LennonTurnAround01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=315, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LennonTurnAround02(self.ctx)


class LennonTurnAround02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1300, patrolName='MS2PatrolData_1301')
        self.move_npc(spawnId=1400, patrolName='MS2PatrolData_1401')
        self.move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return LennonTalk02(self.ctx)


class LennonTalk02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1300, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__7$', arg4=5) # 레논

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return LennonTalk02Skip(self.ctx)


class LennonTalk02Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1300, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EvilKatvanTalk01(self.ctx)


class EvilKatvanTalk01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=12, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001902.xml')
        self.set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__8$', arg4=7) # 흑화카트반
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk01Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return EvilKatvanTalk01Skip(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=12, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001902.xml')


class EvilKatvanTalk01Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.true():
            return EvilKatvanTalk02(self.ctx)


class EvilKatvanTalk02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=13, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001903.xml')
        self.set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__9$', arg4=7) # 흑화카트반
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk02Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return EvilKatvanTalk02Skip(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=13, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001903.xml')


class EvilKatvanTalk02Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.true():
            return EvilKatvanTalk03(self.ctx)


class EvilKatvanTalk03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=14, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001904.xml')
        self.set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__10$', arg4=6) # 흑화카트반
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk03Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return EvilKatvanTalk03Skip(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=14, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001904.xml')


class EvilKatvanTalk03Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return EveWalkFront01(self.ctx)


class EveWalkFront01(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')
        self.move_npc(spawnId=1400, patrolName='MS2PatrolData_1402')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return EveTalk10(self.ctx)


class EveTalk10(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1400, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__11$', duration=5000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk10Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return EveTalk10Skip(self.ctx)


class EveTalk10Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EveTalk11(self.ctx)

    def on_exit(self):
        self.set_npc_emotion_sequence(spawnId=1400, sequenceName='Idle_A')


class EveTalk11(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1400, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__12$', duration=7000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk11Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return EveTalk11Skip(self.ctx)


class EveTalk11Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EveTalk12(self.ctx)

    def on_exit(self):
        self.set_npc_emotion_sequence(spawnId=1400, sequenceName='Idle_A')


class EveTalk12(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1400, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11000523, script='$52000076_QD__MAIN__13$', arg4=5) # 이브

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return EveTalk12Skip(self.ctx)


class EveTalk12Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EvilKatvanTalk10(self.ctx)

    def on_exit(self):
        self.set_npc_emotion_sequence(spawnId=1400, sequenceName='Idle_A')


class EvilKatvanTalk10(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=15, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001905.xml')
        self.set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__14$', arg4=6) # 흑화카트반
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk10Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return EvilKatvanTalk10Skip(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=15, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001905.xml')


class EvilKatvanTalk10Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LennonTalk10(self.ctx)


class LennonTalk10(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')
        self.move_npc(spawnId=1300, patrolName='MS2PatrolData_1302')
        self.set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__15$', arg4=3) # 레논

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return LennonTalk10Skip(self.ctx)


class LennonTalk10Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>
        self.select_camera(triggerId=316, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return EvilKatvanTalk20(self.ctx)


class EvilKatvanTalk20(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=16, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001906.xml')
        self.set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__16$', arg4=5) # 흑화카트반
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk20Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return EvilKatvanTalk20Skip(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=16, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001906.xml')


class EvilKatvanTalk20Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EvilKatvanTalk21(self.ctx)

    def on_exit(self):
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')


class EvilKatvanTalk21(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=17, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001907.xml')
        self.set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__17$', arg4=6) # 흑화카트반
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk21Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return EvilKatvanTalk21Skip(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=17, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001907.xml')


class EvilKatvanTalk21Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EvilKatvanTalk22(self.ctx)

    def on_exit(self):
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')


class EvilKatvanTalk22(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=18, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001908.xml')
        self.set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__18$', arg4=5) # 흑화카트반

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return EvilKatvanTalk22Skip(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=18, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001908.xml')


class EvilKatvanTalk22Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>
        self.select_camera(triggerId=317, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LennonTalk20(self.ctx)


class LennonTalk20(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1300, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__19$', arg4=4) # 레논

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return LennonTalk20Skip(self.ctx)


class LennonTalk20Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1300, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EvilKatvanTalk30(self.ctx)


class EvilKatvanTalk30(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1200, patrolName='MS2PatrolData_1200')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return EvilKatvanTalk31(self.ctx)


class EvilKatvanTalk31(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=19, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001909.xml')
        self.set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__20$', arg4=9) # 흑화카트반
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk31Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return EvilKatvanTalk31Skip(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=19, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001909.xml')


class EvilKatvanTalk31Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EvilKatvanTalk32(self.ctx)


class EvilKatvanTalk32(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001910.xml')
        self.set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__21$', arg4=6) # 흑화카트반
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return EvilKatvanTalk32Skip(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=20, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001910.xml')


class EvilKatvanTalk32Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EvilKatvanLeave01(self.ctx)


class EvilKatvanLeave01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1200, patrolName='MS2PatrolData_1201')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return EvilKatvanLeave02(self.ctx)


class EvilKatvanLeave02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1200])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return EvilKatvanLeave03(self.ctx)


class EvilKatvanLeave03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1300, patrolName='MS2PatrolData_1303')
        self.set_conversation(type=1, spawnId=1300, script='$52000076_QD__MAIN__22$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return EvilKatvanLeave04(self.ctx)


class EvilKatvanLeave04(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return PositionArrange01(self.ctx)


class PositionArrange01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1200,1300,1400])
        self.move_user(mapId=52000076, portalId=30, boxId=100)
        self.create_monster(spawnIds=[1310,1410], animationEffect=False)
        self.select_camera(triggerId=320, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PositionArrange02(self.ctx)


class PositionArrange02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return LennonTalk30(self.ctx)


class LennonTalk30(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=EveTalk31Skip, action='nextState')
        self.set_npc_emotion_sequence(spawnId=1310, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__23$', arg4=5) # 레논

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return LennonTalk30Skip(self.ctx)


class LennonTalk30Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1310, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LennonTalk31(self.ctx)


class LennonTalk31(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1310, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__24$', arg4=5) # 레논

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return LennonTalk31Skip(self.ctx)


class LennonTalk31Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1310, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EveTalk20(self.ctx)


class EveTalk20(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1410, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__25$', duration=6000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk20Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return EveTalk20Skip(self.ctx)


class EveTalk20Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1410, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EveTalk21(self.ctx)


class EveTalk21(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1410, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__26$', duration=6000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk21Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return EveTalk21Skip(self.ctx)


class EveTalk21Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1410, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LennonTalk40(self.ctx)


class LennonTalk40(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1310, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__27$', arg4=6) # 레논

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return LennonTalk40Skip(self.ctx)


class LennonTalk40Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1310, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EveTalk30(self.ctx)


class EveTalk30(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1410, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__28$', duration=3000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk30Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EveTalk30Skip(self.ctx)


class EveTalk30Skip(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1410, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>
        self.select_camera(triggerId=321, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return EveTalk31(self.ctx)


class EveTalk31(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__29$', duration=5000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk31Skip"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return EveTalk31Skip(self.ctx)


class EveTalk31Skip(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return QuestComplete01(self.ctx)


class QuestComplete01(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=100, type='trigger', achieve='saveEveIntheDark')
        self.set_effect(triggerIds=[6205], visible=True)
        self.set_mesh(triggerIds=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=True, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=2, visible=True, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return QuestComplete02(self.ctx)


class QuestComplete02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.reset_camera(interpolationTime=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[100], questIds=[40002688], questStates=[2]):
            return QuestComplete03(self.ctx)


class QuestComplete03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1310, patrolName='MS2PatrolData_1304')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GotoTria01(self.ctx)


class GotoTria01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=1310, script='$52000076_QD__MAIN__30$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GotoTria02(self.ctx)


class GotoTria02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1410, patrolName='MS2PatrolData_1403')
        self.move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return GotoTria03(self.ctx)


class GotoTria03(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1310,1410])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GotoTria04(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class GotoTria04(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000050, portalId=1, boxId=100)


initial_state = 대기
