""" trigger/52000086_qd/50001540.xml """
from common import *
import state


class 퀘스트체크50100300_1(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50100300], questStates=[3]):
            return None # Missing State: 던전종료
        if quest_user_detected(boxIds=[199], questIds=[50100300], questStates=[2]):
            return None # Missing State: 던전종료
        if quest_user_detected(boxIds=[199], questIds=[50100300], questStates=[1]):
            return 대기()


class 퀘스트체크50100310_1(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50100310], questStates=[3]):
            return None # Missing State: 던전종료
        if quest_user_detected(boxIds=[199], questIds=[50100310], questStates=[2]):
            return None # Missing State: 던전종료
        if quest_user_detected(boxIds=[199], questIds=[50100310], questStates=[1]):
            return 대기()


class 퀘스트체크50100311_1(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50100311], questStates=[3]):
            return None # Missing State: 던전종료
        if quest_user_detected(boxIds=[199], questIds=[50100311], questStates=[2]):
            return None # Missing State: 던전종료
        if quest_user_detected(boxIds=[199], questIds=[50100311], questStates=[1]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_actor(triggerId=4002, visible=True, initialSequence='Closed') # IronDoor_Stage02
        set_actor(triggerId=4003, visible=True, initialSequence='Closed') # IronDoor_Stage03
        set_actor(triggerId=4004, visible=True, initialSequence='Closed') # IronDoor_Stage04
        set_actor(triggerId=4005, visible=True, initialSequence='Closed') # IronDoor_Stage05
        select_camera(triggerId=300, enable=True)
        set_mesh(triggerIds=[3005,3006,3007,3008,3009,3010,3011,3012], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3102,3103,3104,3105], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3160,3161,3162,3163,3164], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=True, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1001,1002,1003], arg2=False)
        remove_buff(boxId=199, skillId=70000115)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        move_user(mapId=52000086, portalId=99)
        set_skip(state=연출종료)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 에르다대사01()


class 에르다대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000086_QD__50001540__0$', align='Right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에르다대사02()


class 에르다대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000086_QD__50001540__1$', align='Right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 설눈이대사01()


class 설눈이대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000086_QD__50001540__2$', align='right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 비에른대사01()


class 비에른대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=304, enable=True)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__50001540__3$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 설눈이대사02()


class 설눈이대사02(state.State):
    def on_enter(self):
        select_camera(triggerId=305, enable=True)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A')
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000086_QD__50001540__4$', align='right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 비에른방향전환()


class 비에른방향전환(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000086_QD__50001540__5$', align='right', duration=2000)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 비에른공격()


class 비에른공격(state.State):
    def on_enter(self):
        select_camera(triggerId=306, enable=True)
        set_npc_emotion_sequence(spawnId=1003, sequenceName='Attack_01_D')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000086_QD__50001540__6$', align='right', duration=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 설눈이스턴()


class 설눈이스턴(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        set_npc_emotion_loop(spawnId=1001, sequenceName='Stun_A', duration=1E+12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에르다대사03()


class 에르다대사03(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000086_QD__50001540__7$', align='right', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 비에른대사02()


class 비에른대사02(state.State):
    def on_enter(self):
        select_camera(triggerId=307, enable=True)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__50001540__8$', align='left', duration=4000)
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000086_QD__50001540__9$', align='right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 비에른대사03()


class 비에른대사03(state.State):
    def on_enter(self):
        select_camera(triggerId=308, enable=True)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003B')
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__50001540__10$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에르다대사04()


class 에르다대사04(state.State):
    def on_enter(self):
        select_camera(triggerId=309, enable=True)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002A')
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000086_QD__50001540__11$', align='Right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에르다대사05()


class 에르다대사05(state.State):
    def on_enter(self):
        select_camera(triggerId=310, enable=True)
        set_npc_emotion_loop(spawnId=1002, sequenceName='AttackReady_01_A', duration=1E+12)
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000086_QD__50001540__12$', align='Right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_skip()
        destroy_monster(spawnIds=[1001,1002,1003])
        create_monster(spawnIds=[1004,1005], arg2=False)
        set_npc_emotion_loop(spawnId=1004, sequenceName='Stun_A', duration=1E+12)
        set_npc_emotion_loop(spawnId=1005, sequenceName='AttackReady_01_A', duration=1E+12)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        add_buff(boxIds=[199], skillId=70000115, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차게이트1()


class 차게이트1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)
        show_guide_summary(entityId=25200861, textId=25200861, duration=3500)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 차게이트2()


class 차게이트2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2002], arg2=False)
        set_actor(triggerId=4002, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3102], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2002]):
            return 차게이트3()


class 차게이트3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2003], arg2=False)
        set_actor(triggerId=4003, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3103], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2003]):
            return 차게이트4()


class 차게이트4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2004], arg2=False)
        set_actor(triggerId=4004, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3104], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2004]):
            return 감지대기()


class 감지대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1006], arg2=False)
        set_actor(triggerId=4005, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3105], visible=False, arg3=0, arg4=0, arg5=0)
        show_guide_summary(entityId=25200862, textId=25200862, duration=3500)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 차연출시작2()


class 차연출시작2(state.State):
    def on_enter(self):
        set_skip(state=차연출종료2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=311, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 비에른대사04()


class 비에른대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__50001540__13$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 비에른대사05()


class 비에른대사05(state.State):
    def on_enter(self):
        select_camera(triggerId=312, enable=True)
        move_npc(spawnId=1006, patrolName='MS2PatrolData_1006A')
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__50001540__14$', align='left', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 차연출종료2()


class 차연출종료2(state.State):
    def on_enter(self):
        set_skip()
        set_portal(portalId=91, visible=False, enabled=False, minimapVisible=False)
        destroy_monster(spawnIds=[1006])
        create_monster(spawnIds=[2099], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        add_buff(boxIds=[199], skillId=70000115, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 종료()


class 종료(state.State):
    pass


