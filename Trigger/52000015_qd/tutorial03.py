""" trigger/52000015_qd/tutorial03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # 위험 연출 이펙트 01
        self.set_effect(triggerIds=[5001], visible=False) # 위험 연출 이펙트 02
        self.set_effect(triggerIds=[5002], visible=False) # 위험 연출 사운드 이펙트
        self.set_effect(triggerIds=[6000], visible=False) # 이슈라 음성 사운드 이펙트 01
        self.set_effect(triggerIds=[6001], visible=False) # 이슈라 음성 사운드 이펙트 02
        self.set_effect(triggerIds=[6100], visible=False) # 변절한 칼리브 8검 음성 사운드 이펙트 01
        self.set_effect(triggerIds=[6002], visible=False) # 이슈라 음성 사운드 이펙트 03
        self.set_effect(triggerIds=[6003], visible=False) # 이슈라 음성 사운드 이펙트 04
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.create_widget(type='Guide')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트진행중(self.ctx)


class 퀘스트진행중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[90000414], questStates=[2]):
            return 딜레이02(self.ctx)


class 딜레이02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 딜레이03(self.ctx)


class 딜레이03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=이슈라대화04대기CSkip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 순간이동준비(self.ctx)


class 순간이동준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[6000], visible=True) # 이슈라 음성 사운드 이펙트 01
        self.set_conversation(type=2, spawnId=11001244, script='$52000015_QD__TUTORIAL03__0$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 순간이동시작(self.ctx)


class 순간이동시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=2)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202])
        self.move_user(mapId=52000015, portalId=50, boxId=9001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 순간이동진행(self.ctx)


class 순간이동진행(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=1)
        self.set_effect(triggerIds=[6000], visible=False) # 이슈라 음성 사운드 이펙트 01

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 순간이동완료(self.ctx)


class 순간이동완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=3)
        self.select_camera(triggerId=601, enable=True)
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 적등장01(self.ctx)


class 적등장01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='7', seconds=2)
        self.create_monster(spawnIds=[901])
        self.create_monster(spawnIds=[902])
        self.create_monster(spawnIds=[903])
        self.create_monster(spawnIds=[904])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return 이슈라대화01(self.ctx)


class 이슈라대화01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='8', seconds=3)
        self.set_effect(triggerIds=[6001], visible=True) # 이슈라 음성 사운드 이펙트 02
        self.set_conversation(type=2, spawnId=11001244, script='$52000015_QD__TUTORIAL03__1$', arg4=3)
        self.set_skip(state=이슈라대화02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='8'):
            return 이슈라대화02대기(self.ctx)


class 이슈라대화02대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 이슈라대화02(self.ctx)


class 이슈라대화02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='9', seconds=1)
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_901')
        self.move_npc(spawnId=902, patrolName='MS2PatrolData_902')
        self.move_npc(spawnId=903, patrolName='MS2PatrolData_903')
        self.move_npc(spawnId=904, patrolName='MS2PatrolData_904')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101') # 레쟌 마중 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return 변절자대화01(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[6001], visible=False) # 이슈라 음성 사운드 이펙트 02


class 변절자대화01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=3)
        self.set_effect(triggerIds=[6100], visible=True) # 변절한 칼리브 8검 음성 사운드 이펙트 01
        self.set_conversation(type=2, spawnId=11001235, script='$52000015_QD__TUTORIAL03__2$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 이슈라대화03대기(self.ctx)


class 이슈라대화03대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 이슈라대화03(self.ctx)


class 이슈라대화03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=3)
        self.set_effect(triggerIds=[6100], visible=False) # 변절한 칼리브 8검 음성 사운드 이펙트 01
        self.set_effect(triggerIds=[6002], visible=True) # 이슈라 음성 사운드 이펙트 03
        self.set_conversation(type=2, spawnId=11001244, script='$52000015_QD__TUTORIAL03__3$', arg4=3)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 이슈라대화04대기(self.ctx)


class 이슈라대화04대기CSkip(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202])
        self.move_user(mapId=52000015, portalId=50, boxId=9001)
        self.remove_cinematic_talk()
        self.destroy_monster(spawnIds=[901,902,903,904])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 이슈라대화04(self.ctx)


class 이슈라대화04대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 이슈라대화04(self.ctx)


class 이슈라대화04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return HP가이드01(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[6002], visible=False) # 이슈라 음성 사운드 이펙트 03


# HP 가칼이드
class HP가이드01(trigger_api.Trigger):
    def on_enter(self):
        self.guide_event(eventId=10012060) # 트리거 To가이드 : HP 가이드 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='Guide', name='IsTriggerEvent', condition='10012070'):
            return 전투시작01(self.ctx)


class 전투시작01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[203], animationEffect=True)
        self.destroy_monster(spawnIds=[901,902,903,904])
        self.create_monster(spawnIds=[911,912,913,914], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 전투중01(self.ctx)


class 전투중01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='20'):
            return 위기상황연출준비(self.ctx)


class 위기상황연출준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='21', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[5002], visible=True) # 위험 연출 사운드 이펙트
        self.set_effect(triggerIds=[5000], visible=True) # 위험 연출 이펙트 01

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='21'):
            return 위기상황연출시작01(self.ctx)


class 위기상황연출시작01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='22', seconds=1)
        self.set_effect(triggerIds=[5000], visible=True) # 위험 연출 이펙트 01
        self.set_effect(triggerIds=[6003], visible=True) # 이슈라 음성 사운드 이펙트 04
        self.set_conversation(type=2, spawnId=11001244, script='$52000015_QD__TUTORIAL03__4$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='22'):
            return 위기상황연출시작02(self.ctx)


class 위기상황연출시작02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='23', seconds=1)
        self.set_effect(triggerIds=[5000], visible=True) # 위험 연출 이펙트 01
        self.set_effect(triggerIds=[5001], visible=True) # 위험 연출 이펙트 02

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='23'):
            return 위기상황연출완료(self.ctx)


class 위기상황연출완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_effect(triggerIds=[5000], visible=True) # 위험 연출 이펙트 01
        self.set_effect(triggerIds=[5001], visible=True) # 위험 연출 이펙트 02
        self.set_timer(timerId='23', seconds=3)
        self.destroy_monster(spawnIds=[203])
        self.destroy_monster(spawnIds=[911,912,913,914])
        self.set_effect(triggerIds=[6003], visible=False) # 이슈라 음성 사운드 이펙트 04

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='23'):
            return 위기상황종료(self.ctx)


class 위기상황종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # 위험 연출 이펙트 01
        self.set_effect(triggerIds=[5001], visible=False) # 위험 연출 이펙트 02
        self.move_user(mapId=63000012, portalId=50, boxId=9002)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_exit(self):
        self.set_effect(triggerIds=[5002], visible=False) # 위험 연출 사운드 이펙트


initial_state = 대기
