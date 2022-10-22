""" trigger/63000024_cs/wakeup01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_widget(type='Guide')
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # 목표 바닥 지점01 NPC
        set_effect(triggerIds=[5102], visible=False) # 목표 바닥 지점03 포탈
        set_effect(triggerIds=[5200], visible=False) # 화살표01 NPC
        set_effect(triggerIds=[5300], visible=False) # 경로 안내
        set_effect(triggerIds=[5301], visible=False) # 경로 안내
        set_effect(triggerIds=[5302], visible=False) # 경로 안내
        set_effect(triggerIds=[5303], visible=False) # 경로 안내
        set_effect(triggerIds=[5304], visible=False) # 경로 안내
        set_effect(triggerIds=[5500], visible=False) # 경로 안내
        set_effect(triggerIds=[5501], visible=False) # 경로 안내
        set_effect(triggerIds=[5502], visible=False) # 경로 안내
        set_effect(triggerIds=[5503], visible=False) # 경로 안내
        set_effect(triggerIds=[5504], visible=False) # 경로 안내
        set_effect(triggerIds=[5505], visible=False) # 경로 안내
        set_effect(triggerIds=[5506], visible=False) # 경로 안내
        set_effect(triggerIds=[6000], visible=False) # Voice_Tinchai_00001674
        set_effect(triggerIds=[6001], visible=False) # Voice_Tinchai_00001714
        set_effect(triggerIds=[6002], visible=False) # Voice_Tinchai_00001675
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return PlayMovie01()


class PlayMovie01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000444], questStates=[1]):
            return QuestOnGoing04()
        if quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[3]):
            return QuestOnGoing03()
        if quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[2]):
            return QuestOnGoing02()
        if quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[1]):
            return QuestOnGoing01()
        if wait_tick(waitTick=2000):
            return LodingDelay01()


#  첫 번째 퀘스트 수락한 상태 
class QuestOnGoing01(state.State):
    def on_enter(self):
        move_user(mapId=63000024, portalId=10, boxId=9900)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: MoveToGetWeapon01


#  첫 번째 퀘스트 완료 가능 상태 
class QuestOnGoing02(state.State):
    def on_enter(self):
        move_user(mapId=63000024, portalId=10, boxId=9900)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestStart02()


#  첫 번째 퀘스트 완료 상태 
class QuestOnGoing03(state.State):
    def on_enter(self):
        move_user(mapId=63000024, portalId=10, boxId=9900)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestStart03()


#  두 번째 퀘스트 수락한 상태
class QuestOnGoing04(state.State):
    def on_enter(self):
        move_user(mapId=63000024, portalId=10, boxId=9900)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[103], arg2=False)
        set_portal(portalId=1, visible=True, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TimeToLeave01()


#  최초 입장 
class LodingDelay01(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=True)
        set_scene_skip(state=TinChaiTalk04_CSkip, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCDownIdle01()


class PCDownIdle01(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Down_Idle_D', duration=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCDownIdle02()


class PCDownIdle02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LookAround01()


class LookAround01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[501,502], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return LookAround02()


class LookAround02(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=18000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LookAround03()


class LookAround03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LookAround04()


class LookAround04(state.State):
    def on_enter(self):
        select_camera(triggerId=510, enable=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_105')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LookAround05()


class LookAround05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LookAround06()


class LookAround06(state.State):
    def on_enter(self):
        select_camera(triggerId=511, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LookAround07()


class LookAround07(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TinChaiTalk01()


class TinChaiTalk01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # Voice_Tinchai_00001674
        set_conversation(type=2, spawnId=11001708, script='$63000024_CS__WAKEUP01__0$', arg4=7) # Voice 00001674
        set_skip(state=TinChaiTalk02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return TinChaiTalk02()


class TinChaiTalk02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return TinChaiTalk03()


class TinChaiTalk03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001714
        set_conversation(type=2, spawnId=11001708, script='$63000024_CS__WAKEUP01__1$', arg4=5) # Voice 00001714
        set_skip(state=TinChaiTalk04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TinChaiTalk04()


class TinChaiTalk04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        move_user(mapId=63000024, portalId=10, boxId=9900)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=600, enable=False)

    def on_tick(self) -> state.State:
        if true():
            return 키타입설정안내01()


class TinChaiTalk04_CSkip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        move_user(mapId=63000024, portalId=10, boxId=9900)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=600, enable=False)

    def on_tick(self) -> state.State:
        if true():
            return 키타입설정안내01()


class 키타입설정안내01(state.State):
    def on_enter(self):
        guide_event(eventId=10030005) # 트리거 To가이드 : 키타입설정

    def on_tick(self) -> state.State:
        if widget_condition(type='Guide', name='IsTriggerEvent', condition='10030009'):
            return MeetTinChai01()


class MeetTinChai01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5100], visible=True) # 목표 바닥 지점01 NPC
        set_effect(triggerIds=[5200], visible=True) # 화살표01 NPC
        set_effect(triggerIds=[5300], visible=True) # 경로 안내
        set_effect(triggerIds=[5301], visible=True) # 경로 안내
        set_effect(triggerIds=[5302], visible=True) # 경로 안내
        set_effect(triggerIds=[5303], visible=True) # 경로 안내
        set_effect(triggerIds=[5304], visible=True) # 경로 안내
        show_guide_summary(entityId=10030010, textId=10030010) # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return MeetTinChai02()


class MeetTinChai02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # 목표 바닥 지점01 NPC
        set_effect(triggerIds=[5200], visible=False) # 화살표01 NPC
        set_effect(triggerIds=[5300], visible=False) # 경로 안내
        set_effect(triggerIds=[5301], visible=False) # 경로 안내
        set_effect(triggerIds=[5302], visible=False) # 경로 안내
        set_effect(triggerIds=[5303], visible=False) # 경로 안내
        set_effect(triggerIds=[5304], visible=False) # 경로 안내
        hide_guide_summary(entityId=10030010)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TinChaiTalk10()


class TinChaiTalk10(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TinChaiTalk11()


class TinChaiTalk11(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=True) # Voice_Tinchai_00001675
        set_conversation(type=2, spawnId=11001708, script='$63000024_CS__WAKEUP01__2$', arg4=6) # Voice 00001675
        set_skip(state=TinChaiTalk14)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return TinChaiTalk12()


class TinChaiTalk12(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return TinChaiTalk13()


class TinChaiTalk13(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$63000024_CS__WAKEUP01__3$', arg4=5)
        set_skip(state=TinChaiTalk14)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TinChaiTalk14()


class TinChaiTalk14(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10030020, textId=10030020) # 가이드 : 틴차이에게 다가가 스페이스키로 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[1]):
            return QuestStart01()

    def on_exit(self):
        hide_guide_summary(entityId=10030020)


#  오브젝트 반응, 아이템 줍기, 무기 장착, 일반 공격 가이드  
class QuestStart01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[2]):
            return QuestStart02()


class QuestStart02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[3]):
            return QuestStart03()


#  약초 장착 가이드  
class QuestStart03(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000444], questStates=[1]):
            return QuestStart04()


class QuestStart04(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=False, minimapVisible=False)
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TimeToLeave01()


class TimeToLeave01(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_103')
        set_conversation(type=1, spawnId=103, script='$63000024_CS__WAKEUP01__4$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return GuideNextMap01()


class GuideNextMap01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10030010, textId=10030010) # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5102], visible=True) # 목표 바닥 지점03 포탈
        set_effect(triggerIds=[5500], visible=True) # 경로 안내
        set_effect(triggerIds=[5501], visible=True) # 경로 안내
        set_effect(triggerIds=[5502], visible=True) # 경로 안내
        set_effect(triggerIds=[5503], visible=True) # 경로 안내
        set_effect(triggerIds=[5504], visible=True) # 경로 안내
        set_effect(triggerIds=[5505], visible=True) # 경로 안내
        set_effect(triggerIds=[5506], visible=True) # 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            return GuideNextMap02()


class GuideNextMap02(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_104')
        hide_guide_summary(entityId=10030010)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=1060, textId=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GuideNextMap03()


class GuideNextMap03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=1060)


