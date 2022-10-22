""" trigger/52000021_qd/main01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=False) # 보호막 이펙트
        set_effect(triggerIds=[6100], visible=False) # 전투영역 배리어 룬 쉴드 이펙트
        set_effect(triggerIds=[6200], visible=False) # 홀슈타트 아이스 쉴드 이펙트
        set_effect(triggerIds=[6201], visible=False) # 홀슈타트 아이스 드라이브 이펙트
        set_effect(triggerIds=[6202], visible=False) # 홀슈타트 아이스 임팩트 이펙트
        set_effect(triggerIds=[6300], visible=False) # 이슈라 플레임 쉴드 이펙트
        set_effect(triggerIds=[6301], visible=False) # 이슈라 플레임 드라이브 이펙트
        set_effect(triggerIds=[6400], visible=False) # 보호막 불안정 연출 이펙트 Keep
        set_effect(triggerIds=[6401], visible=False) # 보호막 불안정 연출 이펙트 Invoke
        set_effect(triggerIds=[6500], visible=False) # 얼음 속성 공격 폭발 - 홀슈타트
        set_effect(triggerIds=[6600], visible=False) # 얼음 속성 공격 그라운드 - 홀슈타트
        set_effect(triggerIds=[6700], visible=False) # 얼음 속성 공격 인피니티 - 홀슈타트
        set_mesh(triggerIds=[5000,5001,5002], visible=False, arg3=0, arg4=0, arg5=0) # 이슈라 영역 진입 제한
        set_mesh(triggerIds=[4000,4001,4002,4003], visible=False, arg3=0, arg4=0, arg5=0) # 보호막 영역 탈출 제한
        set_interact_object(triggerIds=[10000831], state=0) # 보호 룬 주문석 : Shield ON
        set_interact_object(triggerIds=[10000832], state=2) # 보호 룬 주문석 : Shield OFF
        create_monster(spawnIds=[111], arg2=True) # 퀘스트용 유페리아
        create_monster(spawnIds=[311], arg2=True) # 퀘스트용 이슈라
        move_npc(spawnId=311, patrolName='MS2PatrolData_311') # 이슈라 Walking

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[60001030], questStates=[1]):
            return 연출준비()


#  대치 상황 : 이슈라와 홀슈타트 Attack Idle 모션 
class 연출준비(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111]) # 퀘스트용 유페리아
        destroy_monster(spawnIds=[311]) # 퀘스트용 이슈라
        set_timer(timerId='1', seconds=2)
        set_mesh(triggerIds=[5000,5001,5002], visible=True, arg3=0, arg4=0, arg5=0) # 이슈라 영역 진입 제한
        set_effect(triggerIds=[6100], visible=True) # 전투영역 배리어 룬 쉴드 이펙트
        select_camera(triggerId=600, enable=True)
        create_monster(spawnIds=[101], arg2=True) # 연출용 유페리아
        create_monster(spawnIds=[201], arg2=True) # 연출용 홀슈타트
        create_monster(spawnIds=[301], arg2=True) # 연출용 이슈라
        set_effect(triggerIds=[6200], visible=True) # 홀슈타트 아이스 쉴드 이펙트
        set_effect(triggerIds=[6300], visible=True) # 이슈라 플레임 쉴드 이펙트
        set_effect(triggerIds=[6201], visible=True) # 홀슈타트 아이스 드라이브 이펙트
        set_effect(triggerIds=[6301], visible=True) # 이슈라 플레임 드라이브 이펙트
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 딜레이()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 카메라연출시작()


class 카메라연출시작(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=6)
        select_camera_path(pathIds=[600,601,602], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 이슈라대화01()


class 이슈라대화01(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=5)
        set_conversation(type=2, spawnId=11001244, script='$52000021_QD__MAIN01__0$', arg4=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 이슈라대화02()


class 이슈라대화02(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=2, spawnId=11001244, script='$52000021_QD__MAIN01__1$', arg4=5)
        set_interact_object(triggerIds=[10000831], state=1) # 보호 룬 주문석 : Shield ON

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 주문석반응대기()


class 주문석반응대기(state.State):
    def on_enter(self):
        select_camera(triggerId=602, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000831], arg2=0):
            return 보호막설정01()

    def on_exit(self):
        set_interact_object(triggerIds=[10000831], state=2) # 보호 룬 주문석 : Shield ON
        set_interact_object(triggerIds=[10000832], state=0) # 보호 룬 주문석 : Shield OFF
        set_effect(triggerIds=[6000], visible=True) # 보호막 이펙트
        set_mesh(triggerIds=[4000,4001,4002,4003], visible=True, arg3=0, arg4=0, arg5=0) # 보호막 영역 탈출 제한


# 유저가 영역 안에 들어온 상태
class 보호막설정01(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=603, enable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 목표전달01()


class 목표전달01(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=4)
        set_conversation(type=2, spawnId=11001244, script='$52000021_QD__MAIN01__2$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 목표전달02()


class 목표전달02(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=603, enable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 유저감지01()


class 유저감지01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 탈출경고01()


class 탈출경고01(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=4)
        set_conversation(type=1, spawnId=101, script='$52000021_QD__MAIN01__3$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=301, script='$52000021_QD__MAIN01__4$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 탈출경고02()


class 탈출경고02(state.State):
    def on_enter(self):
        set_timer(timerId='21', seconds=4)
        set_effect(triggerIds=[6400], visible=True) # 보호막 불안정 연출 이펙트 Keep
        set_conversation(type=1, spawnId=301, script='$52000021_QD__MAIN01__5$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return 탈출경고03()


class 탈출경고03(state.State):
    def on_enter(self):
        set_timer(timerId='22', seconds=4)
        set_conversation(type=1, spawnId=301, script='$52000021_QD__MAIN01__6$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='22'):
            return 탈출경고04()


class 탈출경고04(state.State):
    def on_enter(self):
        set_timer(timerId='25', seconds=3)
        set_effect(triggerIds=[6401], visible=True) # 보호막 불안정 연출 이펙트 Invoke
        set_conversation(type=1, spawnId=101, script='$52000021_QD__MAIN01__7$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='25'):
            return 탈출경고05()


class 탈출경고05(state.State):
    def on_enter(self):
        set_timer(timerId='26', seconds=3)
        set_effect(triggerIds=[6401], visible=True) # 보호막 불안정 연출 이펙트 Invoke
        set_conversation(type=1, spawnId=101, script='$52000021_QD__MAIN01__8$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='26'):
            return 탈출경고06()


class 탈출경고06(state.State):
    def on_enter(self):
        set_timer(timerId='26', seconds=3)
        set_conversation(type=1, spawnId=101, script='$52000021_QD__MAIN01__9$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='26'):
            return 탈출가능01()


class 탈출가능01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000832], state=1) # 보호 룬 주문석 : Shield OFF

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000832], arg2=0):
            return 보호막해제01()

    def on_exit(self):
        set_interact_object(triggerIds=[10000832], state=2) # 보호 룬 주문석 : Shield OFF


#  유저가 영역을 벗어남
class 보호막해제01(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=1)
        set_effect(triggerIds=[6000], visible=False) # 보호막 이펙트
        set_effect(triggerIds=[6400], visible=False) # 보호막 불안정 연출 이펙트 Keep
        set_effect(triggerIds=[6401], visible=False) # 보호막 불안정 연출 이펙트 Invoke
        set_effect(triggerIds=[6202], visible=True) # 홀슈타트 아이스 임팩트 이펙트
        set_mesh(triggerIds=[4000,4001,4002,4003], visible=False, arg3=0, arg4=0, arg5=0) # 보호막 영역 탈출 제한
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=610, enable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 홀슈타트연출01()

    def on_exit(self):
        set_effect(triggerIds=[6200], visible=False) # 홀슈타트 아이스 쉴드 이펙트
        set_effect(triggerIds=[6201], visible=False) # 홀슈타트 아이스 드라이브 이펙트
        set_effect(triggerIds=[6300], visible=False) # 이슈라 플레임 쉴드 이펙트
        set_effect(triggerIds=[6301], visible=False) # 이슈라 플레임 드라이브 이펙트
        set_effect(triggerIds=[6100], visible=False) # 전투영역 배리어 룬 쉴드 이펙트


class 홀슈타트연출01(state.State):
    def on_enter(self):
        set_timer(timerId='31', seconds=2)
        set_effect(triggerIds=[6202], visible=True) # 홀슈타트 아이스 임팩트 이펙트
        set_conversation(type=2, spawnId=11001244, script='$52000021_QD__MAIN01__10$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='31'):
            return 홀슈타트연출02()


class 홀슈타트연출02(state.State):
    def on_enter(self):
        set_timer(timerId='32', seconds=3)
        select_camera(triggerId=611, enable=True)
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9010, spawnIds=[201]):
            return 홀슈타트연출03()


class 홀슈타트연출03(state.State):
    def on_enter(self):
        set_timer(timerId='33', seconds=1)
        set_effect(triggerIds=[6700], visible=True) # 얼음 속성 공격 인피니티 - 홀슈타트
        set_effect(triggerIds=[6600], visible=True) # 얼음 속성 공격 그라운드 - 홀슈타트
        set_effect(triggerIds=[6500], visible=True) # 얼음 속성 공격 폭발 - 홀슈타트
        set_conversation(type=2, spawnId=11001244, script='$52000021_QD__MAIN01__11$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='33'):
            return 홀슈타트연출04()


class 홀슈타트연출04(state.State):
    def on_enter(self):
        set_timer(timerId='35', seconds=1)
        move_npc(spawnId=201, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if time_expired(timerId='35'):
            return 연출종료준비()


#  퀘스트용 NPC로 교체
class 연출종료준비(state.State):
    def on_enter(self):
        set_timer(timerId='34', seconds=2)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[201]) # 연출용 홀슈타트
        destroy_monster(spawnIds=[101]) # 연출용 유페리아
        destroy_monster(spawnIds=[301]) # 연출용 이슈라
        create_monster(spawnIds=[111], arg2=True) # 퀘스트용 유페리아
        create_monster(spawnIds=[311], arg2=True) # 퀘스트용 이슈라
        move_npc(spawnId=311, patrolName='MS2PatrolData_311') # 이슈라 Walking

    def on_tick(self) -> state.State:
        if time_expired(timerId='34'):
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=4)


class 종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=611, enable=False)
        set_achievement(triggerId=9900, type='trigger', achieve='EscapeHallstatt')
        set_mesh(triggerIds=[5000,5001,5002], visible=False, arg3=0, arg4=0, arg5=0) # 이슈라 영역 진입 제한


