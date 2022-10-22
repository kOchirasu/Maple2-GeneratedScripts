""" trigger/52000015_qd/tutorial03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # 위험 연출 이펙트 01
        set_effect(triggerIds=[5001], visible=False) # 위험 연출 이펙트 02
        set_effect(triggerIds=[5002], visible=False) # 위험 연출 사운드 이펙트
        set_effect(triggerIds=[6000], visible=False) # 이슈라 음성 사운드 이펙트 01
        set_effect(triggerIds=[6001], visible=False) # 이슈라 음성 사운드 이펙트 02
        set_effect(triggerIds=[6100], visible=False) # 변절한 칼리브 8검 음성 사운드 이펙트 01
        set_effect(triggerIds=[6002], visible=False) # 이슈라 음성 사운드 이펙트 03
        set_effect(triggerIds=[6003], visible=False) # 이슈라 음성 사운드 이펙트 04
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[201], arg2=True)
        create_widget(type='Guide')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트진행중()


class 퀘스트진행중(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[90000414], questStates=[2]):
            return 딜레이02()


class 딜레이02(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 딜레이03()


class 딜레이03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip(state=이슈라대화04대기CSkip, arg2='nextState')

    def on_tick(self) -> state.State:
        if true():
            return 순간이동준비()


class 순간이동준비(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[6000], visible=True) # 이슈라 음성 사운드 이펙트 01
        set_conversation(type=2, spawnId=11001244, script='$52000015_QD__TUTORIAL03__0$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 순간이동시작()


class 순간이동시작(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=2)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[201])
        create_monster(spawnIds=[202])
        move_user(mapId=52000015, portalId=50, boxId=9001)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 순간이동진행()


class 순간이동진행(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=1)
        set_effect(triggerIds=[6000], visible=False) # 이슈라 음성 사운드 이펙트 01

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 순간이동완료()


class 순간이동완료(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=3)
        select_camera(triggerId=601, enable=True)
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 적등장01()


class 적등장01(state.State):
    def on_enter(self):
        set_timer(timerId='7', seconds=2)
        create_monster(spawnIds=[901])
        create_monster(spawnIds=[902])
        create_monster(spawnIds=[903])
        create_monster(spawnIds=[904])

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return 이슈라대화01()


class 이슈라대화01(state.State):
    def on_enter(self):
        set_timer(timerId='8', seconds=3)
        set_effect(triggerIds=[6001], visible=True) # 이슈라 음성 사운드 이펙트 02
        set_conversation(type=2, spawnId=11001244, script='$52000015_QD__TUTORIAL03__1$', arg4=3)
        set_skip(state=이슈라대화02대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='8'):
            return 이슈라대화02대기()


class 이슈라대화02대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 이슈라대화02()


class 이슈라대화02(state.State):
    def on_enter(self):
        set_timer(timerId='9', seconds=1)
        move_npc(spawnId=901, patrolName='MS2PatrolData_901')
        move_npc(spawnId=902, patrolName='MS2PatrolData_902')
        move_npc(spawnId=903, patrolName='MS2PatrolData_903')
        move_npc(spawnId=904, patrolName='MS2PatrolData_904')
        move_npc(spawnId=101, patrolName='MS2PatrolData_101') # 레쟌 마중 시작

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return 변절자대화01()

    def on_exit(self):
        set_effect(triggerIds=[6001], visible=False) # 이슈라 음성 사운드 이펙트 02


class 변절자대화01(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=3)
        set_effect(triggerIds=[6100], visible=True) # 변절한 칼리브 8검 음성 사운드 이펙트 01
        set_conversation(type=2, spawnId=11001235, script='$52000015_QD__TUTORIAL03__2$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 이슈라대화03대기()


class 이슈라대화03대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 이슈라대화03()


class 이슈라대화03(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=3)
        set_effect(triggerIds=[6100], visible=False) # 변절한 칼리브 8검 음성 사운드 이펙트 01
        set_effect(triggerIds=[6002], visible=True) # 이슈라 음성 사운드 이펙트 03
        set_conversation(type=2, spawnId=11001244, script='$52000015_QD__TUTORIAL03__3$', arg4=3)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 이슈라대화04대기()


class 이슈라대화04대기CSkip(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202])
        move_user(mapId=52000015, portalId=50, boxId=9001)
        remove_cinematic_talk()
        destroy_monster(spawnIds=[901,902,903,904])

    def on_tick(self) -> state.State:
        if true():
            return 이슈라대화04()


class 이슈라대화04대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 이슈라대화04()


class 이슈라대화04(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return HP가이드01()

    def on_exit(self):
        set_effect(triggerIds=[6002], visible=False) # 이슈라 음성 사운드 이펙트 03


#  HP 가칼이드  
class HP가이드01(state.State):
    def on_enter(self):
        guide_event(eventId=10012060) # 트리거 To가이드 : HP 가이드 시작

    def on_tick(self) -> state.State:
        if widget_condition(type='Guide', name='IsTriggerEvent', condition='10012070'):
            return 전투시작01()


class 전투시작01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[203], arg2=True)
        destroy_monster(spawnIds=[901,902,903,904])
        create_monster(spawnIds=[911,912,913,914], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 전투중01()


class 전투중01(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 위기상황연출준비()


class 위기상황연출준비(state.State):
    def on_enter(self):
        set_timer(timerId='21', seconds=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5002], visible=True) # 위험 연출 사운드 이펙트
        set_effect(triggerIds=[5000], visible=True) # 위험 연출 이펙트 01

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return 위기상황연출시작01()


class 위기상황연출시작01(state.State):
    def on_enter(self):
        set_timer(timerId='22', seconds=1)
        set_effect(triggerIds=[5000], visible=True) # 위험 연출 이펙트 01
        set_effect(triggerIds=[6003], visible=True) # 이슈라 음성 사운드 이펙트 04
        set_conversation(type=2, spawnId=11001244, script='$52000015_QD__TUTORIAL03__4$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='22'):
            return 위기상황연출시작02()


class 위기상황연출시작02(state.State):
    def on_enter(self):
        set_timer(timerId='23', seconds=1)
        set_effect(triggerIds=[5000], visible=True) # 위험 연출 이펙트 01
        set_effect(triggerIds=[5001], visible=True) # 위험 연출 이펙트 02

    def on_tick(self) -> state.State:
        if time_expired(timerId='23'):
            return 위기상황연출완료()


class 위기상황연출완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_effect(triggerIds=[5000], visible=True) # 위험 연출 이펙트 01
        set_effect(triggerIds=[5001], visible=True) # 위험 연출 이펙트 02
        set_timer(timerId='23', seconds=3)
        destroy_monster(spawnIds=[203])
        destroy_monster(spawnIds=[911,912,913,914])
        set_effect(triggerIds=[6003], visible=False) # 이슈라 음성 사운드 이펙트 04

    def on_tick(self) -> state.State:
        if time_expired(timerId='23'):
            return 위기상황종료()


class 위기상황종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # 위험 연출 이펙트 01
        set_effect(triggerIds=[5001], visible=False) # 위험 연출 이펙트 02
        move_user(mapId=63000012, portalId=50, boxId=9002)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_exit(self):
        set_effect(triggerIds=[5002], visible=False) # 위험 연출 사운드 이펙트


