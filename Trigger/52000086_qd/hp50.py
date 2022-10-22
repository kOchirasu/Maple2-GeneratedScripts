""" trigger/52000086_qd/hp50.xml """
from common import *
import state


class 퀘스트체크50100300_2(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50100300], questStates=[3]):
            return 던전종료()
        if quest_user_detected(boxIds=[199], questIds=[50100300], questStates=[2]):
            return 던전종료()
        if quest_user_detected(boxIds=[199], questIds=[50100300], questStates=[1]):
            return 대기()


class 퀘스트체크50100310_2(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50100310], questStates=[3]):
            return 던전종료()
        if quest_user_detected(boxIds=[199], questIds=[50100310], questStates=[2]):
            return 던전종료()
        if quest_user_detected(boxIds=[199], questIds=[50100310], questStates=[1]):
            return 대기()


class 퀘스트체크50100311_2(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50100311], questStates=[3]):
            return 던전종료()
        if quest_user_detected(boxIds=[199], questIds=[50100311], questStates=[2]):
            return 던전종료()
        if quest_user_detected(boxIds=[199], questIds=[50100311], questStates=[1]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=False)
        set_visible_breakable_object(triggerIds=[4000], arg2=False)
        set_portal(portalId=91, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_value(key='hp50', value=1):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[1007,1008], arg2=False)
        move_user(mapId=52000086, portalId=30)
        select_camera(triggerId=313, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에르다등장()


class 에르다등장(state.State):
    def on_enter(self):
        set_skip(state=연출종료)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera(triggerId=314, enable=True)
        move_npc(spawnId=1008, patrolName='MS2PatrolData_1008A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에르다대사01()


class 에르다대사01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__0$', align='right', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 비에른대사01()


class 비에른대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=315, enable=True)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__1$', align='left', duration=3000)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__2$', align='left', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에르다대사02()


class 에르다대사02(state.State):
    def on_enter(self):
        select_camera(triggerId=316, enable=True)
        visible_my_pc(isVisible=False) # 캐릭터 숨김
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__3$', align='right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 비에른대사02()


class 비에른대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__4$', align='left', duration=4000)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__5$', align='left', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 비에른접근()


class 비에른접근(state.State):
    def on_enter(self):
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1006B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에르다대사03()


class 에르다대사03(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True) # 캐릭터 보임
        select_camera(triggerId=317, enable=True)
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__6$', align='right', duration=4000)
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__7$', align='right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 비에른대사03()


class 비에른대사03(state.State):
    def on_enter(self):
        select_camera(triggerId=318, enable=True)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__8$', align='left', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에르다대사04()


class 에르다대사04(state.State):
    def on_enter(self):
        select_camera(triggerId=317, enable=True)
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__9$', align='right', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 비에른대사04()


class 비에른대사04(state.State):
    def on_enter(self):
        select_camera(triggerId=312, enable=True)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__10$', align='right', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 비에른대사05()


class 비에른대사05(state.State):
    def on_enter(self):
        select_camera(triggerId=318, enable=True)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__11$', align='left', duration=4000)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__12$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 에르다대사05()


class 에르다대사05(state.State):
    def on_enter(self):
        select_camera(triggerId=317, enable=True)
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__13$', align='right', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에르다대사06()


class 에르다대사06(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1008])
        set_visible_breakable_object(triggerIds=[4000], arg2=True)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__14$', align='left', duration=2000)
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__15$', align='right', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 에르다대사07()


class 에르다대사07(state.State):
    def on_enter(self):
        select_camera(triggerId=319, enable=True)
        create_monster(spawnIds=[1009], arg2=False)
        set_visible_breakable_object(triggerIds=[4000], arg2=False)
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__16$', align='right', duration=3000)
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__17$', align='right', duration=5000)
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__18$', align='right', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return 에르다이동()


class 에르다이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1009, patrolName='MS2PatrolData_1009A')
        select_camera(triggerId=320, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에르다대사08()


class 에르다대사08(state.State):
    def on_enter(self):
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1007A')
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__19$', align='right', duration=4000)
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__20$', align='right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_skip()
        visible_my_pc(isVisible=True) # 캐릭터 숨김
        set_ai_extra_data(key='getBack', value=1)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[1007,1008,1009])
        create_monster(spawnIds=[2098], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        add_buff(boxIds=[199], skillId=70000115, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 비에른사망대기()


class 비에른사망대기(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099]):
            return 사망연출대기()


class 사망연출대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 사망연출시작()


class 사망연출시작(state.State):
    def on_enter(self):
        move_user(mapId=52000086, portalId=40)
        destroy_monster(spawnIds=[2099])
        destroy_monster(spawnIds=[2098])
        create_monster(spawnIds=[1101,1102], arg2=False)
        set_npc_emotion_loop(spawnId=1102, sequenceName='Stun_A', duration=1E+12)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 에드다이동02()


class 에드다이동02(state.State):
    def on_enter(self):
        set_skip(state=사망연출종료)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera(triggerId=321, enable=True)
        move_npc(spawnId=1101, patrolName='MS2PatrolData_1101A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에르다대사10()


class 에르다대사10(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__21$', align='right', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 비에른대사10()


class 비에른대사10(state.State):
    def on_enter(self):
        select_camera(triggerId=322, enable=True)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__22$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에르다대사11()


class 에르다대사11(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__23$', align='right', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 비에른대사11()


class 비에른대사11(state.State):
    def on_enter(self):
        select_camera(triggerId=323, enable=True)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__24$', align='left', duration=4000)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__25$', align='left', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 비에른대사12()


class 비에른대사12(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__26$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에르다대사12()


class 에르다대사12(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__27$', align='right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 비에른대사13()


class 비에른대사13(state.State):
    def on_enter(self):
        select_camera(triggerId=322, enable=True)
        set_npc_emotion_loop(spawnId=1102, sequenceName='Idle_A', duration=1E+12)
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__28$', align='left', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 비에른대사14()


class 비에른대사14(state.State):
    def on_enter(self):
        select_camera(triggerId=324, enable=True)
        move_npc(spawnId=1102, patrolName='MS2PatrolData_1102A')
        add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__29$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에드다이동03()


class 에드다이동03(state.State):
    def on_enter(self):
        select_camera(triggerId=325, enable=True)
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__30$', align='right', duration=3000)
        # <action name="NPC를이동시킨다" arg1="1101" arg2="MS2PatrolData_1101B" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC말풍선대사()


class PC말풍선대사(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000086_QD__HP50__31$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 에르다대사13()


class 에르다대사13(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__32$', align='right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에르다대사13To1()


class 에르다대사13To1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__33$', align='right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에르다대사14()


class 에르다대사14(state.State):
    def on_enter(self):
        select_camera(triggerId=321, enable=True)
        # <action name="대화를설정한다" arg1="2" arg2="11003074" arg3="미안하지만 지금은… 생각을 좀 정리하고 싶으니 혼자 있게 해 다오. 부탁이다." arg4="4" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에드다마저이동()


class 에드다마저이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # <action name="NPC를이동시킨다" arg1="1101" arg2="MS2PatrolData_1101C" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 사망연출종료()


class 사망연출종료(state.State):
    def on_enter(self):
        set_skip()
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[1101,1102])
        create_monster(spawnIds=[10000,10001,10002])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        set_achievement(triggerId=199, type='trigger', achieve='snowkingbjorn')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 던전종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_portal(portalId=91, visible=False, enabled=False, minimapVisible=False)
        move_user(mapId=52000086, portalId=30)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 던전종료1()


class 던전종료1(state.State):
    def on_enter(self):
        set_actor(triggerId=4002, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3102], visible=False, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=4002, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3102], visible=False, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=4003, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3103], visible=False, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=4004, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3104], visible=False, arg3=0, arg4=0, arg5=0)
        set_breakable(triggerIds=[4000], enabled=False)
        set_visible_breakable_object(triggerIds=[4000], arg2=False)
        move_user(mapId=52000086, portalId=30)
        destroy_monster(spawnIds=[1101,1102])
        create_monster(spawnIds=[10000,10001,10002])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


