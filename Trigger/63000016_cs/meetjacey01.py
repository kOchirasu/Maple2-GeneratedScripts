""" trigger/63000016_cs/meetjacey01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_widget(type='Guide')
        set_portal(portalId=2, visible=True, enabled=False, minimapVisible=True)
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0) # MonitorOff
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0) # MonitorOn
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[6000], visible=False) # RadioInterference

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return WalkIn01()


#   이미 퀘스트 수락한 상태 제이시 가까이로 강제 이동
class MoveToJacey01(state.State):
    def on_enter(self):
        move_user(mapId=63000016, portalId=10, boxId=9000)
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return MoveToJacey02()


class MoveToJacey02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JaceyQuest02()


class WalkIn01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[90000431], questStates=[2]):
            return MoveToJacey01()
        if wait_tick(waitTick=2000):
            return WalkIn02()


class WalkIn02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return WalkIn03()


class WalkIn03(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return MeetJacey01()


class MeetJacey01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__0$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return MeetJacey02()


class MeetJacey02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MeetJacey03()


class MeetJacey03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JaceyTalk01()


class JaceyTalk01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__1$', arg4=5)
        set_skip(state=JaceyTalk02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return JaceyTalk02()


class JaceyTalk02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JaceyTalk03()


class JaceyTalk03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1002')
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__2$', arg4=4)
        set_skip(state=JaceyTalk04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return JaceyTalk04()


class JaceyTalk04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JaceyTalk05()


class JaceyTalk05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__3$', arg4=4)
        set_skip(state=JaceyTalk06)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return JaceyTalk06()


class JaceyTalk06(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=602, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MinimapGuide01()


#  트리거 To가이드  가이드에서 이동 불가능하게 막기
class MinimapGuide01(state.State):
    def on_enter(self):
        guide_event(eventId=10021010) # 트리거 To가이드 : 탭키 눌러서 미니맵 크게 보기

    def on_tick(self) -> state.State:
        if widget_condition(type='Guide', name='IsTriggerEvent', condition='10021013'):
            return MinimapGuide02()


class MinimapGuide02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return JaceyTalk10()


class JaceyTalk10(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__4$', arg4=4)
        set_skip(state=JaceyTalk11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return JaceyTalk11()


class JaceyTalk11(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JaceyTalk12()


class JaceyTalk12(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__5$', arg4=4)
        set_skip(state=JaceyTalk13)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return JaceyTalk13()


class JaceyTalk13(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolWithJacey01()


class PatrolWithJacey01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10021020, textId=10021020) # 가이드 : 제이시를 따라 이동하기
        move_npc(spawnId=101, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9100, spawnIds=[101]):
            return PatrolWithJacey02()


class PatrolWithJacey02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$63000016_CS__MEETJACEY01__6$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=101, script='$63000016_CS__MEETJACEY01__7$', arg4=3, arg5=3)
        set_conversation(type=1, spawnId=101, script='$63000016_CS__MEETJACEY01__8$', arg4=3, arg5=6)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9101, spawnIds=[101]):
            return PatrolWithJacey03()


class PatrolWithJacey03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$63000016_CS__MEETJACEY01__9$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=101, script='$63000016_CS__MEETJACEY01__10$', arg4=3, arg5=3)
        set_conversation(type=1, spawnId=101, script='$63000016_CS__MEETJACEY01__11$', arg4=3, arg5=6)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9102, spawnIds=[101]):
            return PatrolWithJacey04()


class PatrolWithJacey04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$63000016_CS__MEETJACEY01__12$', arg4=3)
        hide_guide_summary(entityId=10021020)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CallNextRoom01()


class CallNextRoom01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CallNextRoom02()


class CallNextRoom02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=False, arg3=100, arg4=0, arg5=0) # MonitorOff
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # MonitorOn
        set_effect(triggerIds=[6000], visible=True) # RadioInterference

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CallNextRoom03()


class CallNextRoom03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__13$', arg4=4)
        set_skip(state=CallNextRoom04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CallNextRoom04()


class CallNextRoom04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        select_camera(triggerId=700, enable=False)
        set_effect(triggerIds=[6000], visible=False) # RadioInterference

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JaceyQuest00()


#  90000431 퀘스트 수락한 유저를 감지하면 
class JaceyQuest00(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10021030, textId=10021030) # 가이드 : 제이시와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9002], questIds=[90000431], questStates=[2]):
            return JaceyQuest01()


class JaceyQuest01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10021030)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JaceyQuest02()


class JaceyQuest02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__14$', arg4=4)
        set_skip(state=JaceyQuest03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return JaceyQuest03()


class JaceyQuest03(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JaceyQuest04()


class JaceyQuest04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__15$', arg4=4)
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)
        set_skip(state=JaceyQuest05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return JaceyQuest05()


class JaceyQuest05(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return AboutPotion01()


class AboutPotion01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__16$', arg4=4)
        set_skip(state=AboutPotion02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return AboutPotion02()


class AboutPotion02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return AboutPotion03()


class AboutPotion03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001620, script='$63000016_CS__MEETJACEY01__17$', arg4=4)
        set_skip(state=AboutPotion04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return AboutPotion04()


class AboutPotion04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=103, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JaceyLeve01()

    def on_exit(self):
        guide_event(eventId=10021120) # 트리거 To가이드 : PC 컨트롤 불가


class JaceyLeve01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=103, script='$63000016_CS__MEETJACEY01__18$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return JaceyLeve02()


class JaceyLeve02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        destroy_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SendSignalToGuide01()


#  트리거 To가이드  
class SendSignalToGuide01(state.State):
    def on_enter(self):
        guide_event(eventId=10021050) # 트리거 To가이드 : 약초 퀵슬롯에 장착하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PortalOpen01()


class PortalOpen01(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9002]):
            return Quit()


class Quit(state.State):
    pass


