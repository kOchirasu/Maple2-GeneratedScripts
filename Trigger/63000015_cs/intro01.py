""" trigger/63000015_cs/intro01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_widget(type='Guide')
        set_sound(triggerId=10000, arg2=False)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_effect(triggerIds=[5100], visible=False) # 목표지점 바닥
        set_effect(triggerIds=[5101], visible=False) # 목표지점 화살표
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 목료 완료 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5200], visible=False) # 경로 안내
        set_effect(triggerIds=[5201], visible=False) # 경로 안내
        set_effect(triggerIds=[5202], visible=False) # 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 경로 안내
        set_effect(triggerIds=[5204], visible=False) # 경로 안내
        set_effect(triggerIds=[5205], visible=False) # 경로 안내
        set_effect(triggerIds=[5206], visible=False) # 경로 안내
        set_effect(triggerIds=[5207], visible=False) # 경로 안내
        set_effect(triggerIds=[6000], visible=False) # VoiceGangster
        set_effect(triggerIds=[8000], visible=False) # WeiHong 00001390
        set_effect(triggerIds=[8001], visible=False) # WeiHong 00001391
        set_effect(triggerIds=[8002], visible=False) # WeiHong 00001392
        set_effect(triggerIds=[8003], visible=False) # WeiHong 00001393
        set_effect(triggerIds=[8004], visible=False) # WeiHong 00001394
        set_effect(triggerIds=[8005], visible=False) # WeiHong 00000480
        create_monster(spawnIds=[101,201,202,203,204,205,206], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return PlayOpeningMovie01()


#  퀘스트 진행 중 상태, 완료 가능 상태 
class StandAside10(state.State):
    def on_enter(self):
        set_sound(triggerId=10000, arg2=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_mesh(triggerIds=[3001,3002,3003,3004], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return StandAside11()


class StandAside11(state.State):
    def on_enter(self):
        move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        move_npc(spawnId=206, patrolName='MS2PatrolData_206')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return WeiHongQuest03()


#  퀘스트 진행 완료 상태 
class StandAside20(state.State):
    def on_enter(self):
        set_sound(triggerId=10000, arg2=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_mesh(triggerIds=[3001,3002,3003,3004], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return StandAside21()


class StandAside21(state.State):
    def on_enter(self):
        move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        move_npc(spawnId=206, patrolName='MS2PatrolData_206')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return GuideNextMap01()


#  최초 입장 
class PlayOpeningMovie01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9100], questIds=[90000430], questStates=[2]):
            return StandAside10()
        if quest_user_detected(boxIds=[9100], questIds=[90000430], questStates=[3]):
            return StandAside20()
        if wait_tick(waitTick=2000):
            return PlayOpeningMovie02()


class PlayOpeningMovie02(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='common\Common_Opening.usm', movieId=2)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='2'):
            return PlayMovie01()
        if wait_tick(waitTick=190000):
            return PlayMovie01()


class PlayMovie01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PlayMovie02()


class PlayMovie02(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Cut_Blackstar_Crash.swf', movieId=1) # 임시

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return WeiHongTalk01()
        if wait_tick(waitTick=66000):
            return WeiHongTalk01()


class WeiHongTalk01(state.State):
    def on_enter(self):
        set_sound(triggerId=10000, arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)
        set_effect(triggerIds=[6000], visible=True) # VoiceGangster

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return WeiHongTalk02()

    def on_exit(self):
        set_effect(triggerIds=[6000], visible=False) # VoiceGangster


class WeiHongTalk02(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)
        set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__0$', arg4=6) # Voice 00001390
        set_effect(triggerIds=[8000], visible=True) # WeiHong 00001390
        set_skip(state=WeiHongTalk03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return WeiHongTalk03()


class WeiHongTalk03(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[8000], visible=False) # WeiHong 00001390

    def on_tick(self) -> state.State:
        if true():
            return WeiHongTalk04()


class WeiHongTalk04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__1$', arg4=6) # Voice 00001391
        set_effect(triggerIds=[8001], visible=True) # WeiHong 00001391
        set_skip(state=WeiHongTalk05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return WeiHongTalk05()


class WeiHongTalk05(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[8001], visible=False) # WeiHong 00001391

    def on_tick(self) -> state.State:
        if true():
            return WeiHongTalk06()


class WeiHongTalk06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__2$', arg4=5) # Voice 00001392
        set_effect(triggerIds=[8002], visible=True) # WeiHong 00001392
        set_skip(state=WeiHongTalk07)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return WeiHongTalk07()


class WeiHongTalk07(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[8002], visible=False) # WeiHong 00001392
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=False)
        set_mesh(triggerIds=[3001,3002,3003,3004], visible=False, arg3=0, arg4=0, arg5=0) # barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return StandAside01()


class StandAside01(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return StandAside02()


class StandAside02(state.State):
    def on_enter(self):
        move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        move_npc(spawnId=206, patrolName='MS2PatrolData_206')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return StandAside03()


class StandAside03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return KeytypeSelect01()


class KeytypeSelect01(state.State):
    def on_enter(self):
        guide_event(eventId=10020005)

    def on_tick(self) -> state.State:
        if widget_condition(type='Guide', name='IsTriggerEvent', condition='10020009'):
            return MeetWeiHong01()


class MeetWeiHong01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5002], visible=True) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5100], visible=True) # 목표지점 바닥
        set_effect(triggerIds=[5101], visible=True) # 목표지점 화살표
        show_guide_summary(entityId=10020010, textId=10020010) # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return MeetWeiHong02()


class MeetWeiHong02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # 목표지점 바닥
        set_effect(triggerIds=[5101], visible=False) # 목표지점 화살표
        hide_guide_summary(entityId=10020010)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return WeiHongTalk10()


class WeiHongTalk10(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return WeiHongTalk11()


class WeiHongTalk11(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__3$', arg4=5) # Voice 00000480
        set_effect(triggerIds=[8005], visible=True) # WeiHong 00000480
        set_skip(state=WeiHongTalk12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return WeiHongTalk12()


class WeiHongTalk12(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[8005], visible=False) # WeiHong 00000480
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if true():
            return WeiHongTalk13()


class WeiHongTalk13(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__4$', arg4=5) # Voice 00001393
        set_effect(triggerIds=[8003], visible=True) # WeiHong 00001393
        set_skip(state=WeiHongTalk14)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return WeiHongTalk14()


class WeiHongTalk14(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[8003], visible=False) # WeiHong 00001393
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if true():
            return MafiaTalk10()


class MafiaTalk10(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # VoiceGangster
        set_conversation(type=1, spawnId=201, script='$63000015_CS__INTRO01__5$', arg4=3, arg5=0)
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MafiaTalk11()


class MafiaTalk11(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        set_conversation(type=1, spawnId=202, script='$63000015_CS__INTRO01__6$', arg4=3, arg5=0)
        set_npc_emotion_sequence(spawnId=202, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MafiaTalk12()


class MafiaTalk12(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=202, sequenceName='Idle_A')
        set_conversation(type=1, spawnId=206, script='$63000015_CS__INTRO01__7$', arg4=3, arg5=0)
        set_npc_emotion_sequence(spawnId=206, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return WeiHongTalk20()

    def on_exit(self):
        set_effect(triggerIds=[6000], visible=False) # VoiceGangster


class WeiHongTalk20(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=206, sequenceName='Idle_A')
        set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__8$', arg4=6) # Voice 00001394
        set_effect(triggerIds=[8004], visible=True) # WeiHong 00001394
        set_skip(state=WeiHongQuest01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return WeiHongQuest01()


class WeiHongQuest01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[8004], visible=False) # WeiHong 00001394
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=602, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return WeiHongQuest02()


class WeiHongQuest02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10020020, textId=10020020) # 가이드 : 스페이스키로 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9100], questIds=[90000430], questStates=[2]):
            return WeiHongQuest03()


class WeiHongQuest03(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10020020)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10020021, textId=10020021) # 가이드 : 웨이 홍과 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9100], questIds=[90000430], questStates=[3]):
            return GuideNextMap01()


class GuideNextMap01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10020021)
        set_portal(portalId=1, visible=True, enabled=False, minimapVisible=True)
        set_effect(triggerIds=[5200], visible=True) # 경로 안내
        set_effect(triggerIds=[5201], visible=True) # 경로 안내
        set_effect(triggerIds=[5202], visible=True) # 경로 안내
        set_effect(triggerIds=[5203], visible=True) # 경로 안내
        set_effect(triggerIds=[5204], visible=True) # 경로 안내
        set_effect(triggerIds=[5205], visible=True) # 경로 안내
        set_effect(triggerIds=[5206], visible=True) # 경로 안내
        set_effect(triggerIds=[5207], visible=True) # 경로 안내
        show_guide_summary(entityId=10020012, textId=10020012) # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return GuideNextMap02()


class GuideNextMap02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10020012)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        show_guide_summary(entityId=10020011, textId=10020011) # 가이드 : 포털 위치에서 스페이스 키 누르기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9100]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10020011)
        set_effect(triggerIds=[5200], visible=False) # 경로 안내
        set_effect(triggerIds=[5201], visible=False) # 경로 안내
        set_effect(triggerIds=[5202], visible=False) # 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 경로 안내
        set_effect(triggerIds=[5204], visible=False) # 경로 안내
        set_effect(triggerIds=[5205], visible=False) # 경로 안내
        set_effect(triggerIds=[5206], visible=False) # 경로 안내
        set_effect(triggerIds=[5207], visible=False) # 경로 안내


