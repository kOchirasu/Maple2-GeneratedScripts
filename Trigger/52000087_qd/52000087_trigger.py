""" trigger/52000087_qd/52000087_trigger.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[600], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[22651], questIds=[20002266], questStates=[3]):
            return 용무없는유저는아웃()
        if quest_user_detected(boxIds=[22651], questIds=[10002781], questStates=[1]):
            return 카르카르시작()
        if quest_user_detected(boxIds=[22651], questIds=[20002265], questStates=[3]):
            return 완료연출01_20002265()


#  카르카르 연출, 메이플연합 회담씬
class 카르카르시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 진행()


class 진행(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에레브_1()


class 에레브_1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__0$', arg4=3)
        set_skip(state=에레브_1skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에레브_1skip()


class 에레브_1skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 에레브_2()


class 에레브_2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__1$', arg4=5)
        set_skip(state=에레브_2skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에레브_2skip()


class 에레브_2skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 에레브_3()


class 에레브_3(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__2$', arg4=5)
        set_skip(state=에레브_3skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에레브_3skip()


class 에레브_3skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 블랙아이_1()


class 블랙아이_1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000006, script='$52000087_QD__52000087_TRIGGER__3$', arg4=3)
        set_skip(state=블랙아이_1skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 블랙아이_1skip()


class 블랙아이_1skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 블랙아이_1a()


class 블랙아이_1a(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000006, script='$52000087_QD__52000087_TRIGGER__4$', arg4=5)
        set_skip(state=블랙아이_1askip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 블랙아이_1askip()


class 블랙아이_1askip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 프레이_1()


class 프레이_1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000119, script='$52000087_QD__52000087_TRIGGER__5$', arg4=5)
        set_skip(state=프레이_1skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 프레이_1skip()


class 프레이_1skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 구르는천둥_1()


class 구르는천둥_1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001581, script='$52000087_QD__52000087_TRIGGER__6$', arg4=3)
        set_skip(state=구르는천둥_1skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 구르는천둥_1skip()


class 구르는천둥_1skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 알론_1()


class 알론_1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__7$', arg4=3)
        set_skip(state=알론_1skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 알론_1skip()


class 알론_1skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 오스칼_1()


class 오스칼_1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000015, script='$52000087_QD__52000087_TRIGGER__8$', arg4=5)
        set_skip(state=오스칼_1skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 오스칼_1skip()


class 오스칼_1skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 블랙아이_2()


class 블랙아이_2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000006, script='$52000087_QD__52000087_TRIGGER__9$', arg4=5)
        set_skip(state=블랙아이_2skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 블랙아이_2skip()


class 블랙아이_2skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 블랙아이_2a()


class 블랙아이_2a(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000006, script='$52000087_QD__52000087_TRIGGER__10$', arg4=5)
        set_skip(state=블랙아이_2askip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 블랙아이_2askip()


class 블랙아이_2askip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 블랙아이_3()


class 블랙아이_3(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000006, script='$52000087_QD__52000087_TRIGGER__11$', arg4=5)
        set_skip(state=블랙아이_3skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 블랙아이_3skip()


class 블랙아이_3skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 알론_2()


class 알론_2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__12$', arg4=3)
        set_skip(state=알론_2skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 알론_2skip()


class 알론_2skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 에레브_4()


class 에레브_4(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__13$', arg4=5)
        set_skip(state=에레브_4skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에레브_4skip()


class 에레브_4skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 영상준비()


class 영상준비(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_timer(timerId='21', seconds=2)
        select_camera_path(pathIds=[601,602], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        play_scene_movie(fileName='lumieragonhistory.swf', movieId=1)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 알론_3()


class 알론_3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__14$', arg4=5)
        set_skip(state=알론_3skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 알론_3skip()


class 알론_3skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 알론_4()


class 알론_4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__15$', arg4=5)
        set_skip(state=알론_4skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 알론_4skip()


class 알론_4skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 알론_4a()


class 알론_4a(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__16$', arg4=5)
        set_skip(state=알론_4askip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 알론_4askip()


class 알론_4askip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 알론_5()


class 알론_5(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__17$', arg4=5)
        set_skip(state=알론_5skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 알론_5skip()


class 알론_5skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 에레브_5()


class 에레브_5(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__18$', arg4=5)
        set_skip(state=에레브_5skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에레브_5skip()


class 에레브_5skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 에레브_6()


class 에레브_6(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__19$', arg4=5)
        set_skip(state=에레브_6skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에레브_6skip()


class 에레브_6skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칼_1()


class 칼_1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000074, script='$52000087_QD__52000087_TRIGGER__20$', arg4=5)
        set_skip(state=칼_1skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 칼_1skip()


class 칼_1skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 에레브_7()


class 에레브_7(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__21$', arg4=5)
        set_skip(state=에레브_7skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에레브_7skip()


class 에레브_7skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 에레브_8()


class 에레브_8(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__22$', arg4=5)
        set_skip(state=에레브_8skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에레브_8skip()


class 에레브_8skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_achievement(triggerId=22651, type='trigger', achieve='Lumieragon_History')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


#  챕터10 [20002265 새로운 실마리]완료 시 연출, 오르데가 포탈타고 나타남
class 완료연출01_20002265(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_user(mapId=52000087, portalId=10)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 완료연출02_20002265()


class 완료연출02_20002265(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[2002,2003,2004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 완료연출03_20002265()


class 완료연출03_20002265(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        create_monster(spawnIds=[1003], arg2=False) # 오르데
        move_npc(spawnId=1003, patrolName='MS2PatrolData_Start') # 오르데 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 완료연출04_20002265()


class 완료연출04_20002265(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=1003, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 완료연출04_b20002265()


class 완료연출04_b20002265(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003087, script='$52000087_QD__52000087_TRIGGER__23$', arg4=3) # 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료연출04_c20002265()


class 완료연출04_c20002265(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1003, sequenceName='ChatUp_A')
        set_conversation(type=2, spawnId=11003087, script='$52000087_QD__52000087_TRIGGER__24$', arg4=3) # 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료연출05_20002265()


class 완료연출05_20002265(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=2)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_Orde') # 오르데 이동

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[22651], questIds=[20002266], questStates=[3]):
            return 완료연출01_20002266()


#  챕터10 [20002265 새로운 실마리]완료 시 연출 종료, 오르데가 포탈타고 나타남
#  챕터10 [20002266 취향입니다, 존중해주시죠]완료 시 연출, 오르데와 PC가 포탈열고 사라짐
class 완료연출01_난입20002266(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1003], arg2=False) # 오르데

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 완료연출01_20002266()


class 완료연출01_20002266(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000087, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 완료연출02_20002266()


class 완료연출02_20002266(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[2005,2006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 완료연출03_20002266()


class 완료연출03_20002266(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003087, script='$52000087_QD__52000087_TRIGGER__25$', arg4=3) # 대사
        move_npc(spawnId=1003, patrolName='MS2PatrolData_OrdeOut') # 에레브 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료연출04_20002266()


class 완료연출04_20002266(state.State):
    def on_enter(self):
        set_portal(portalId=500, visible=True, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[601], visible=True)
        destroy_monster(spawnIds=[1003])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료연출05_20002266()


class 완료연출05_20002266(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)


class 용무없는유저는아웃(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[22651], questIds=[20002285], questStates=[3]):
            return 챕터10에필로그연출01()


#  챕터10 에필로그 연출
class 챕터10에필로그연출01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_user(mapId=52000087, portalId=10)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 챕터10에필로그연출02()


class 챕터10에필로그연출02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__26$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출03()


class 챕터10에필로그연출03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__27$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출05()


class 챕터10에필로그연출05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__28$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출05b()


class 챕터10에필로그연출05b(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출06()


class 챕터10에필로그연출06(state.State):
    def on_enter(self):
        set_sound(triggerId=90000, arg2=True) # 마드리아 고조 브금
        set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__29$', arg4=6)
        set_onetime_effect(id=2007, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_01_00002007.xml')
        set_skip(state=챕터10에필로그연출06스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 챕터10에필로그연출06스킵()


class 챕터10에필로그연출06스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출07()


class 챕터10에필로그연출07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__30$', arg4=6)
        set_onetime_effect(id=2008, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_02_00002008.xml')
        set_skip(state=챕터10에필로그연출07스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 챕터10에필로그연출07스킵()


class 챕터10에필로그연출07스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출08()


class 챕터10에필로그연출08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__31$', arg4=9)
        set_onetime_effect(id=2009, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_03_00002009.xml')
        set_skip(state=챕터10에필로그연출08스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 챕터10에필로그연출08스킵()


class 챕터10에필로그연출08스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출09()


class 챕터10에필로그연출09(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__32$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 챕터10에필로그연출10()


class 챕터10에필로그연출10(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__33$', arg4=5)
        set_onetime_effect(id=2010, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_04_00002010.xml')
        set_skip(state=챕터10에필로그연출10스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 챕터10에필로그연출10스킵()


class 챕터10에필로그연출10스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출11()


class 챕터10에필로그연출11(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__34$', arg4=5)
        set_onetime_effect(id=2011, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_05_00002011.xml')
        set_skip(state=챕터10에필로그연출11스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 챕터10에필로그연출11스킵()


class 챕터10에필로그연출11스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출12()


class 챕터10에필로그연출12(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__35$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출13()


class 챕터10에필로그연출13(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__36$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출13_b()


class 챕터10에필로그연출13_b(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__37$', arg4=5)
        set_onetime_effect(id=2012, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_06_00002012.xml')
        set_skip(state=챕터10에필로그연출13b스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 챕터10에필로그연출13b스킵()


class 챕터10에필로그연출13b스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출14()


class 챕터10에필로그연출14(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__38$', arg4=5)
        set_onetime_effect(id=2013, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_07_00002013.xml')
        set_skip(state=챕터10에필로그연출14스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출14스킵()


class 챕터10에필로그연출14스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출15()


class 챕터10에필로그연출15(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__39$', arg4=6)
        set_onetime_effect(id=2014, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_08_00002014.xml')
        set_skip(state=챕터10에필로그연출15스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 챕터10에필로그연출15스킵()


class 챕터10에필로그연출15스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출16()


class 챕터10에필로그연출16(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__40$', arg4=5)
        set_onetime_effect(id=2015, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_09_00002015.xml')
        set_skip(state=챕터10에필로그연출16스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 챕터10에필로그연출16스킵()


class 챕터10에필로그연출16스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출17()


class 챕터10에필로그연출17(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 챕터10에필로그연출18()


class 챕터10에필로그연출18(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__41$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출18b()


class 챕터10에필로그연출18b(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__42$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출19()


class 챕터10에필로그연출19(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__43$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출20()


class 챕터10에필로그연출20(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__44$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출21()


class 챕터10에필로그연출21(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__45$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출22()


class 챕터10에필로그연출22(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=2000025, portalId=2)


