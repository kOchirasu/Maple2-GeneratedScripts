""" trigger/02000349_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001])
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
        set_interact_object(triggerIds=[13000014], state=2)
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

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return CheckUserCount()


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
        create_monster(spawnIds=[2002])

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
        create_monster(spawnIds=[1021])

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
            create_monster(spawnIds=[2003])
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
        create_monster(spawnIds=[1022])

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
            create_monster(spawnIds=[2004])
            return 진행11()


class 진행11(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[131]):
            return 진행11몬스터()


class 진행11몬스터(state.State):
    def on_enter(self):
        move_npc(spawnId=2004, patrolName='MS2PatrolData2004_A')
        create_monster(spawnIds=[1023])

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
            create_monster(spawnIds=[2005])
            return 진행13()


class 진행13(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[133]):
            return 진행13몬스터()


class 진행13몬스터(state.State):
    def on_enter(self):
        move_npc(spawnId=2005, patrolName='MS2PatrolData2005_A')
        create_monster(spawnIds=[1024])

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
            create_monster(spawnIds=[2007])
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
        set_effect(triggerIds=[602], visible=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=302, enable=True)
        set_skip(state=카드반연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카드반대사01()


class 카드반대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__5$', arg4=3)
        set_skip(state=카드반연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카드반대사02()


class 카드반대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__6$', arg4=4)
        set_skip(state=카드반연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 레논대사05()


class 레논대사05(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)
        set_conversation(type=2, spawnId=11000064, script='$02000349_BF__MAIN__7$', arg4=4)
        set_skip(state=카드반연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카드반대사03()


class 카드반대사03(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__8$', arg4=6)
        set_skip(state=카드반연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 카드반대사04()


class 카드반대사04(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__9$', arg4=8)
        set_skip(state=카드반연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 카드반대사05()


class 카드반대사05(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        create_monster(spawnIds=[1025,1026], arg2=False)
        set_conversation(type=2, spawnId=24001705, script='$02000349_BF__MAIN__10$', arg4=7)
        set_skip(state=카드반연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 카드반연출종료()


class 카드반연출종료(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003502, textId=20003502, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        destroy_monster(spawnIds=[1025,1026])
        destroy_monster(spawnIds=[1099])
        set_agent(triggerIds=[901], visible=False)
        set_agent(triggerIds=[902], visible=False)
        set_agent(triggerIds=[903], visible=False)
        set_agent(triggerIds=[904], visible=False)
        destroy_monster(spawnIds=[2007])
        create_monster(spawnIds=[2006])
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
            return 진행17()


class 진행17(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1025,1026], arg2=False)
        create_monster(spawnIds=[1099], arg2=False)
        set_agent(triggerIds=[901], visible=True)
        set_agent(triggerIds=[902], visible=True)
        set_agent(triggerIds=[903], visible=True)
        set_agent(triggerIds=[904], visible=True)
        set_mesh(triggerIds=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], visible=False, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1099]):
            return 던전종료연출딜레이()


class 던전종료연출딜레이(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2006])
        create_monster(spawnIds=[2008])
        destroy_monster(spawnIds=[1025,1026])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 던전종료연출종료()


class 던전종료연출종료(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2008, script='$02000349_BF__MAIN__11$', arg4=3)
        dungeon_clear()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 포털생성()


class 포털생성(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2008, script='$02000349_BF__MAIN__13$', arg4=4)
        move_npc(spawnId=2008, patrolName='MS2PatrolData2008_A')
        set_effect(triggerIds=[6205], visible=True) # action name="ShowGuideSummary" entityID="20003493" textID="20003493"
        set_mesh(triggerIds=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=True, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            destroy_monster(spawnIds=[2008])
            hide_guide_summary(entityId=20003493)
            return 종료()


class 종료(state.State):
    pass


