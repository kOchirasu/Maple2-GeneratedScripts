""" trigger/52000076_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)
        set_actor(triggerId=201, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=202, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=203, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=204, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=205, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=206, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=207, visible=True, initialSequence='Idle_A')
        set_interact_object(triggerIds=[10000806], state=2)
        set_interact_object(triggerIds=[10000806], state=2)
        set_interact_object(triggerIds=[10000807], state=2)
        set_interact_object(triggerIds=[10000808], state=2)
        set_interact_object(triggerIds=[10000809], state=2)
        set_interact_object(triggerIds=[10000810], state=2)
        set_interact_object(triggerIds=[10000811], state=2)
        set_interact_object(triggerIds=[10000812], state=2)
        set_mesh(triggerIds=[39101,39102,39103,39104,39105,39106], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[600], visible=False) # fog 500
        set_effect(triggerIds=[601], visible=False) # fog 1000
        set_effect(triggerIds=[602], visible=False) # fog 1500
        set_effect(triggerIds=[6101], visible=False)
        set_effect(triggerIds=[6102], visible=False)
        set_effect(triggerIds=[6103], visible=False)
        set_effect(triggerIds=[6104], visible=False)
        set_effect(triggerIds=[6105], visible=False)
        set_effect(triggerIds=[6106], visible=False)
        set_effect(triggerIds=[6107], visible=False)
        set_effect(triggerIds=[6108], visible=False)
        set_effect(triggerIds=[6201], visible=False)
        set_effect(triggerIds=[6202], visible=False)
        set_effect(triggerIds=[6203], visible=False)
        set_effect(triggerIds=[6204], visible=False)
        set_effect(triggerIds=[6205], visible=False)
        set_skill(triggerIds=[701], isEnable=False)
        set_skill(triggerIds=[702], isEnable=False)
        set_skill(triggerIds=[703], isEnable=False)
        set_skill(triggerIds=[704], isEnable=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_agent(triggerIds=[901], visible=True)
        set_agent(triggerIds=[902], visible=True)
        set_agent(triggerIds=[903], visible=True)
        set_agent(triggerIds=[904], visible=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=11, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001901.xml')
        set_onetime_effect(id=12, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001902.xml')
        set_onetime_effect(id=13, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001903.xml')
        set_onetime_effect(id=14, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001904.xml')
        set_onetime_effect(id=15, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001905.xml')
        set_onetime_effect(id=16, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001906.xml')
        set_onetime_effect(id=17, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001907.xml')
        set_onetime_effect(id=18, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001908.xml')
        set_onetime_effect(id=19, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001909.xml')
        set_onetime_effect(id=20, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001910.xml')
        set_user_value(key='saveEveIntheDark', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return CheckQuestCondition()


class CheckQuestCondition(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[100], questIds=[40002688], questStates=[1]):
            return DungeonReady()
        if quest_user_detected(boxIds=[100], questIds=[40002688], questStates=[2]):
            return QuestOnGoing01()
        if wait_tick(waitTick=2000):
            return DungeonReady()


#  다음 맵 이동 
class QuestOnGoing01(state.State):
    def on_enter(self):
        move_user(mapId=52000076, portalId=30, boxId=100)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return QuestOnGoing02()


class QuestOnGoing02(state.State):
    def on_enter(self):
        select_camera(triggerId=320, enable=True)
        create_monster(spawnIds=[1310,1410], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return QuestOnGoing03()


class QuestOnGoing03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EveTalk30()


#  던전 진행 
class DungeonReady(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return state.DungeonStart()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='KatvanIntroMovie.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 진행01벽제거()

state.DungeonStart = DungeonStart


class 진행01벽제거(state.State):
    def on_enter(self):
        set_actor(triggerId=201, visible=False, initialSequence='Idle_A')
        set_interact_object(triggerIds=[10000806], state=1)
        show_guide_summary(entityId=20003492, textId=20003492)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000806], arg2=0):
            hide_guide_summary(entityId=20003492)
            set_mesh(triggerIds=[39101], visible=False, arg3=0, arg4=0, arg5=0)
            return 진행01몬스터()


class 진행01몬스터(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002,1003], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1101]):
            return 진행01오브젝트()


class 진행01오브젝트(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003496, textId=20003496)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_actor(triggerId=202, visible=False, initialSequence='Idle_A')
        set_interact_object(triggerIds=[10000807], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000807], arg2=0):
            hide_guide_summary(entityId=20003496)
            return 진행02몬스터()


class 진행02몬스터(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[39102], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1004,1005,1006], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1102]):
            return 진행02오브젝트()


class 진행02오브젝트(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003497, textId=20003497)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_actor(triggerId=203, visible=False, initialSequence='Idle_A')
        set_interact_object(triggerIds=[10000808], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000808], arg2=0):
            hide_guide_summary(entityId=20003497)
            return 진행03몬스터()


class 진행03몬스터(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[39103], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1007,1008,1009], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1103]):
            return 진행04오브젝트()


class 진행04오브젝트(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003498, textId=20003498)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_actor(triggerId=204, visible=False, initialSequence='Idle_A')
        set_interact_object(triggerIds=[10000809], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000809], arg2=0):
            hide_guide_summary(entityId=20003498)
            return 진행04몬스터()


class 진행04몬스터(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[39104], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1010,1011,1012], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1104]):
            return 진행05오브젝트()


class 진행05오브젝트(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003499, textId=20003499)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_actor(triggerId=205, visible=False, initialSequence='Idle_A')
        set_interact_object(triggerIds=[10000810], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000810], arg2=0):
            hide_guide_summary(entityId=20003499)
            return 진행05몬스터()


class 진행05몬스터(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[39105], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1013,1014,1015], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1105]):
            return 진행06오브젝트()


class 진행06오브젝트(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003500, textId=20003500)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_actor(triggerId=206, visible=False, initialSequence='Idle_A')
        set_interact_object(triggerIds=[10000811], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000811], arg2=0):
            set_achievement(triggerId=100, type='trigger', achieve='rescue_boroboro')
            hide_guide_summary(entityId=20003500)
            return 진행06몬스터()


class 진행06몬스터(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[39106], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1016,1017,1018,1019,1020], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1106]):
            return 레논오브젝트()


class 레논오브젝트(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003495, textId=20003495)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_actor(triggerId=207, visible=False, initialSequence='Idle_A')
        set_interact_object(triggerIds=[10000812], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000812], arg2=0):
            destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
            hide_guide_summary(entityId=20003495)
            return 레논구출()


class 레논구출(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        set_skip(state=레논구출종료)
        destroy_monster(spawnIds=[2001])
        create_monster(spawnIds=[2002], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 레논대사01()


class 레논대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6101], visible=True)
        set_conversation(type=2, spawnId=11000064, script='$02000349_BF__MAIN__3$', arg4=3)
        set_skip(state=레논구출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 레논대사02()


class 레논대사02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6102], visible=True)
        set_conversation(type=2, spawnId=11000064, script='$02000349_BF__MAIN__4$', arg4=3)
        set_skip(state=레논구출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 레논구출종료()


class 레논구출종료(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> state.State:
        if true():
            return 진행07()


class 진행07(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)
        move_npc(spawnId=2002, patrolName='MS2PatrolData2002_AB')
        show_guide_summary(entityId=20003501, textId=20003501, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=127, spawnIds=[2002]):
            return 진행07몬스터()


class 진행07몬스터(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1021], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1021]):
            return 진행08()


class 진행08(state.State):
    def on_enter(self):
        move_npc(spawnId=2002, patrolName='MS2PatrolData2002_C')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=128, spawnIds=[2002]):
            set_skill(triggerIds=[701], isEnable=True)
            set_effect(triggerIds=[6201], visible=True)
            destroy_monster(spawnIds=[2002])
            create_monster(spawnIds=[2003], arg2=False)
            return 진행09()


class 진행09(state.State):
    def on_enter(self):
        move_npc(spawnId=2002, patrolName='MS2PatrolData2002_C')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[129]):
            return 진행09몬스터()


class 진행09몬스터(state.State):
    def on_enter(self):
        move_npc(spawnId=2003, patrolName='MS2PatrolData2003_A')
        create_monster(spawnIds=[1022], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1022]):
            return 진행10()


class 진행10(state.State):
    def on_enter(self):
        move_npc(spawnId=2003, patrolName='MS2PatrolData2003_B')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=130, spawnIds=[2003]):
            set_skill(triggerIds=[702], isEnable=True)
            set_effect(triggerIds=[6202], visible=True)
            destroy_monster(spawnIds=[2003])
            create_monster(spawnIds=[2004], arg2=False)
            return 진행11()


class 진행11(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[131]):
            return 진행11몬스터()


class 진행11몬스터(state.State):
    def on_enter(self):
        move_npc(spawnId=2004, patrolName='MS2PatrolData2004_A')
        create_monster(spawnIds=[1023], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1023]):
            return 진행12()


class 진행12(state.State):
    def on_enter(self):
        move_npc(spawnId=2004, patrolName='MS2PatrolData2004_B')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=132, spawnIds=[2004]):
            set_skill(triggerIds=[703], isEnable=True)
            set_effect(triggerIds=[6203], visible=True)
            destroy_monster(spawnIds=[2004])
            create_monster(spawnIds=[2005], arg2=False)
            return 진행13()


class 진행13(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[133]):
            return 진행13몬스터()


class 진행13몬스터(state.State):
    def on_enter(self):
        move_npc(spawnId=2005, patrolName='MS2PatrolData2005_A')
        create_monster(spawnIds=[1024], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1024]):
            return 진행14()


class 진행14(state.State):
    def on_enter(self):
        move_npc(spawnId=2005, patrolName='MS2PatrolData2005_B')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=134, spawnIds=[2005]):
            set_skill(triggerIds=[704], isEnable=True)
            set_effect(triggerIds=[6204], visible=True)
            destroy_monster(spawnIds=[2005])
            create_monster(spawnIds=[2007], arg2=False)
            return 진행15()


class 진행15(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[135]):
            return 카트반연출딜레이()


class 카트반연출딜레이(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1099], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카드반연출시작()


class 카드반연출시작(state.State):
    def on_enter(self):
        set_scene_skip(state=카드반연출종료, arg2='nextState')
        set_effect(triggerIds=[602], visible=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=302, enable=True)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카드반대사01()


class 카드반대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__5$', arg4=3)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카드반대사02()


class 카드반대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__6$', arg4=4)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 레논대사05()


class 레논대사05(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)
        set_conversation(type=2, spawnId=11000064, script='$02000349_BF__MAIN__7$', arg4=4)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카드반대사03()


class 카드반대사03(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__8$', arg4=6)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 카드반대사04()


class 카드반대사04(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__9$', arg4=8)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 카드반대사05()


class 카드반대사05(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        create_monster(spawnIds=[1025,1026], arg2=False)
        set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__10$', arg4=7)
        # <action name="스킵을설정한다" arg1="카드반연출종료" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 카드반연출종료()


class 카드반연출종료(state.State):
    def on_enter(self):
        set_scene_skip()
        show_guide_summary(entityId=20003502, textId=20003502, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        destroy_monster(spawnIds=[1025,1026])
        destroy_monster(spawnIds=[1099])
        set_agent(triggerIds=[901], visible=False)
        set_agent(triggerIds=[902], visible=False)
        set_agent(triggerIds=[903], visible=False)
        set_agent(triggerIds=[904], visible=False)
        destroy_monster(spawnIds=[2007])
        create_monster(spawnIds=[2006], arg2=False)
        select_camera_path(pathIds=[302], returnView=True)

    def on_tick(self) -> state.State:
        if true():
            return 진행16()


class 진행16(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=302, enable=False)
        select_camera(triggerId=303, enable=False)
        move_npc(spawnId=2006, patrolName='MS2PatrolData2006_A')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=136, spawnIds=[2006]):
            return BossBattleStart01()


#  Boss 전투 개시 
class BossBattleStart01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1025,1026], arg2=False)
        create_monster(spawnIds=[1099], arg2=False)
        set_agent(triggerIds=[901], visible=True)
        set_agent(triggerIds=[902], visible=True)
        set_agent(triggerIds=[903], visible=True)
        set_agent(triggerIds=[904], visible=True)
        set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], visible=False, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if user_value(key='saveEveIntheDark', value=1):
            return BossNpcChange01()
        if monster_dead(boxIds=[1099]):
            return BossNpcChange01()


class BossNpcChange01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_agent(triggerIds=[901], visible=False)
        set_agent(triggerIds=[902], visible=False)
        set_agent(triggerIds=[903], visible=False)
        set_agent(triggerIds=[904], visible=False)
        set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BossNpcChange02()


class BossNpcChange02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1025,1026,1099,2006])
        move_user(mapId=52000076, portalId=20, boxId=100)
        create_monster(spawnIds=[1200,1300], arg2=False)
        select_camera(triggerId=310, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BossNpcChange03()


class BossNpcChange03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_loop(spawnId=1200, sequenceName='Attack_Idle_A', duration=15000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BossNpcChange04()


class BossNpcChange04(state.State):
    def on_enter(self):
        select_camera(triggerId=311, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return EveEnter01()


class EveEnter01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1400], arg2=False)
        move_npc(spawnId=1400, patrolName='MS2PatrolData_1400')
        select_camera(triggerId=312, enable=True)
        set_conversation(type=1, spawnId=1400, script='$52000076_QD__MAIN__0$', arg4=4, arg5=2)
        set_scene_skip(state=EvilKatvanLeave04, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return EveEnter02()


class EveEnter02(state.State):
    def on_enter(self):
        select_camera(triggerId=313, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EveEnter03()


class EveEnter03(state.State):
    def on_enter(self):
        move_npc(spawnId=1300, patrolName='MS2PatrolData_1300')
        move_user_path(patrolName='MS2PatrolData_1000')
        set_conversation(type=1, spawnId=1300, script='$52000076_QD__MAIN__1$', arg4=2, arg5=2)
        set_conversation(type=1, spawnId=0, script='$52000076_QD__MAIN__2$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return EveEnter04()


class EveEnter04(state.State):
    def on_enter(self):
        set_onetime_effect(id=11, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001901.xml')
        set_conversation(type=1, spawnId=1200, script='$52000076_QD__MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EveTalk01()

    def on_exit(self):
        set_onetime_effect(id=11, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001901.xml')


class EveTalk01(state.State):
    def on_enter(self):
        select_camera(triggerId=314, enable=True)
        add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__4$', duration=5000, align='center')
        set_npc_emotion_sequence(spawnId=1400, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EveTalk01Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EveTalk01Skip()


class EveTalk01Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1400, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EveTalk02()


class EveTalk02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__5$', duration=5000, align='center')
        set_npc_emotion_sequence(spawnId=1400, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EveTalk02Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EveTalk02Skip()


class EveTalk02Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1400, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LennonTalk01()


class LennonTalk01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__6$', arg4=5) # 레논
        set_npc_emotion_sequence(spawnId=1300, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="LennonTalk01Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return LennonTalk01Skip()


class LennonTalk01Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1300, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LennonTurnAround01()


class LennonTurnAround01(state.State):
    def on_enter(self):
        select_camera(triggerId=315, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LennonTurnAround02()


class LennonTurnAround02(state.State):
    def on_enter(self):
        move_npc(spawnId=1300, patrolName='MS2PatrolData_1301')
        move_npc(spawnId=1400, patrolName='MS2PatrolData_1401')
        move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return LennonTalk02()


class LennonTalk02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1300, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__7$', arg4=5) # 레논

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LennonTalk02Skip()


class LennonTalk02Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1300, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EvilKatvanTalk01()


class EvilKatvanTalk01(state.State):
    def on_enter(self):
        set_onetime_effect(id=12, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001902.xml')
        set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__8$', arg4=7) # 흑화카트반
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk01Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return EvilKatvanTalk01Skip()

    def on_exit(self):
        set_onetime_effect(id=12, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001902.xml')


class EvilKatvanTalk01Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if true():
            return EvilKatvanTalk02()


class EvilKatvanTalk02(state.State):
    def on_enter(self):
        set_onetime_effect(id=13, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001903.xml')
        set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__9$', arg4=7) # 흑화카트반
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk02Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return EvilKatvanTalk02Skip()

    def on_exit(self):
        set_onetime_effect(id=13, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001903.xml')


class EvilKatvanTalk02Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if true():
            return EvilKatvanTalk03()


class EvilKatvanTalk03(state.State):
    def on_enter(self):
        set_onetime_effect(id=14, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001904.xml')
        set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__10$', arg4=6) # 흑화카트반
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk03Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return EvilKatvanTalk03Skip()

    def on_exit(self):
        set_onetime_effect(id=14, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001904.xml')


class EvilKatvanTalk03Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return EveWalkFront01()


class EveWalkFront01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')
        move_npc(spawnId=1400, patrolName='MS2PatrolData_1402')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EveTalk10()


class EveTalk10(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1400, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__11$', duration=5000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk10Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EveTalk10Skip()


class EveTalk10Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EveTalk11()

    def on_exit(self):
        set_npc_emotion_sequence(spawnId=1400, sequenceName='Idle_A')


class EveTalk11(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1400, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__12$', duration=7000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk11Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return EveTalk11Skip()


class EveTalk11Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EveTalk12()

    def on_exit(self):
        set_npc_emotion_sequence(spawnId=1400, sequenceName='Idle_A')


class EveTalk12(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1400, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11000523, script='$52000076_QD__MAIN__13$', arg4=5) # 이브

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EveTalk12Skip()


class EveTalk12Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EvilKatvanTalk10()

    def on_exit(self):
        set_npc_emotion_sequence(spawnId=1400, sequenceName='Idle_A')


class EvilKatvanTalk10(state.State):
    def on_enter(self):
        set_onetime_effect(id=15, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001905.xml')
        set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__14$', arg4=6) # 흑화카트반
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk10Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return EvilKatvanTalk10Skip()

    def on_exit(self):
        set_onetime_effect(id=15, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001905.xml')


class EvilKatvanTalk10Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LennonTalk10()


class LennonTalk10(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')
        move_npc(spawnId=1300, patrolName='MS2PatrolData_1302')
        set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__15$', arg4=3) # 레논

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return LennonTalk10Skip()


class LennonTalk10Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>
        select_camera(triggerId=316, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EvilKatvanTalk20()


class EvilKatvanTalk20(state.State):
    def on_enter(self):
        set_onetime_effect(id=16, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001906.xml')
        set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__16$', arg4=5) # 흑화카트반
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk20Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EvilKatvanTalk20Skip()

    def on_exit(self):
        set_onetime_effect(id=16, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001906.xml')


class EvilKatvanTalk20Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EvilKatvanTalk21()

    def on_exit(self):
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')


class EvilKatvanTalk21(state.State):
    def on_enter(self):
        set_onetime_effect(id=17, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001907.xml')
        set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__17$', arg4=6) # 흑화카트반
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk21Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return EvilKatvanTalk21Skip()

    def on_exit(self):
        set_onetime_effect(id=17, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001907.xml')


class EvilKatvanTalk21Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EvilKatvanTalk22()

    def on_exit(self):
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')


class EvilKatvanTalk22(state.State):
    def on_enter(self):
        set_onetime_effect(id=18, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001908.xml')
        set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__18$', arg4=5) # 흑화카트반

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EvilKatvanTalk22Skip()

    def on_exit(self):
        set_onetime_effect(id=18, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001908.xml')


class EvilKatvanTalk22Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>
        select_camera(triggerId=317, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LennonTalk20()


class LennonTalk20(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1300, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__19$', arg4=4) # 레논

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LennonTalk20Skip()


class LennonTalk20Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1300, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EvilKatvanTalk30()


class EvilKatvanTalk30(state.State):
    def on_enter(self):
        move_npc(spawnId=1200, patrolName='MS2PatrolData_1200')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EvilKatvanTalk31()


class EvilKatvanTalk31(state.State):
    def on_enter(self):
        set_onetime_effect(id=19, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001909.xml')
        set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__20$', arg4=9) # 흑화카트반
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')
        # <action name="스킵을설정한다" arg1="EvilKatvanTalk31Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return EvilKatvanTalk31Skip()

    def on_exit(self):
        set_onetime_effect(id=19, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001909.xml')


class EvilKatvanTalk31Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EvilKatvanTalk32()


class EvilKatvanTalk32(state.State):
    def on_enter(self):
        set_onetime_effect(id=20, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001910.xml')
        set_conversation(type=2, spawnId=24001705, script='$52000076_QD__MAIN__21$', arg4=6) # 흑화카트반
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return EvilKatvanTalk32Skip()

    def on_exit(self):
        set_onetime_effect(id=20, enable=False, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001910.xml')


class EvilKatvanTalk32Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1200, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EvilKatvanLeave01()


class EvilKatvanLeave01(state.State):
    def on_enter(self):
        move_npc(spawnId=1200, patrolName='MS2PatrolData_1201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return EvilKatvanLeave02()


class EvilKatvanLeave02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1200])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return EvilKatvanLeave03()


class EvilKatvanLeave03(state.State):
    def on_enter(self):
        move_npc(spawnId=1300, patrolName='MS2PatrolData_1303')
        set_conversation(type=1, spawnId=1300, script='$52000076_QD__MAIN__22$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EvilKatvanLeave04()


class EvilKatvanLeave04(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PositionArrange01()


class PositionArrange01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1200,1300,1400])
        move_user(mapId=52000076, portalId=30, boxId=100)
        create_monster(spawnIds=[1310,1410], arg2=False)
        select_camera(triggerId=320, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PositionArrange02()


class PositionArrange02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return LennonTalk30()


class LennonTalk30(state.State):
    def on_enter(self):
        set_scene_skip(state=EveTalk31Skip, arg2='nextState')
        set_npc_emotion_sequence(spawnId=1310, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__23$', arg4=5) # 레논

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LennonTalk30Skip()


class LennonTalk30Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1310, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LennonTalk31()


class LennonTalk31(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1310, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__24$', arg4=5) # 레논

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LennonTalk31Skip()


class LennonTalk31Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1310, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EveTalk20()


class EveTalk20(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1410, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__25$', duration=6000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk20Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return EveTalk20Skip()


class EveTalk20Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1410, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EveTalk21()


class EveTalk21(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1410, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__26$', duration=6000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk21Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return EveTalk21Skip()


class EveTalk21Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1410, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LennonTalk40()


class LennonTalk40(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1310, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11000064, script='$52000076_QD__MAIN__27$', arg4=6) # 레논

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return LennonTalk40Skip()


class LennonTalk40Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1310, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EveTalk30()


class EveTalk30(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1410, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__28$', duration=3000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk30Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EveTalk30Skip()


class EveTalk30Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1410, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>
        select_camera(triggerId=321, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return EveTalk31()


class EveTalk31(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000523, illustId='Eve_serious', msg='$52000076_QD__MAIN__29$', duration=5000, align='center')
        # <action name="스킵을설정한다" arg1="EveTalk31Skip"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EveTalk31Skip()


class EveTalk31Skip(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestComplete01()


class QuestComplete01(state.State):
    def on_enter(self):
        set_achievement(triggerId=100, type='trigger', achieve='saveEveIntheDark')
        set_effect(triggerIds=[6205], visible=True)
        set_mesh(triggerIds=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=True, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=2, visible=True, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestComplete02()


class QuestComplete02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        reset_camera(interpolationTime=1)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[100], questIds=[40002688], questStates=[2]):
            return QuestComplete03()


class QuestComplete03(state.State):
    def on_enter(self):
        move_npc(spawnId=1310, patrolName='MS2PatrolData_1304')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GotoTria01()


class GotoTria01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1310, script='$52000076_QD__MAIN__30$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GotoTria02()


class GotoTria02(state.State):
    def on_enter(self):
        move_npc(spawnId=1410, patrolName='MS2PatrolData_1403')
        move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GotoTria03()


class GotoTria03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1310,1410])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GotoTria04()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class GotoTria04(state.State):
    def on_enter(self):
        move_user(mapId=63000050, portalId=1, boxId=100)


