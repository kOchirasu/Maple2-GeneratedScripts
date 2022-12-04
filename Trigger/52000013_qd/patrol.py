""" trigger/52000013_qd/patrol.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_actor(triggerId=6000, visible=False, initialSequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 어린벨라등장(self.ctx)


class 어린벨라등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=1)
        self.create_monster(spawnIds=[5000], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 어린벨라패트롤01(self.ctx)


class 어린벨라패트롤01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=5000, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9001, spawnIds=[5000]):
            return 어린벨라대화01(self.ctx)


class 어린벨라대화01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=3)
        self.set_conversation(type=1, spawnId=5000, script='$52000013_QD__MAIN__1$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 어린벨라패트롤02(self.ctx)


class 어린벨라패트롤02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=5000, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9002, spawnIds=[5000]):
            return 어린벨라대화02(self.ctx)


class 어린벨라대화02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='12', seconds=3)
        self.set_conversation(type=1, spawnId=5000, script='$52000013_QD__MAIN__2$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='12'):
            return 어린벨라패트롤03(self.ctx)


class 어린벨라패트롤03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=5000, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9003, spawnIds=[5000]):
            return 카메라연출01(self.ctx)


class 카메라연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='12', seconds=6)
        self.select_camera_path(pathIds=[901], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9004, spawnIds=[5000]):
            return 카메라연출02(self.ctx)


class 카메라연출02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='13', seconds=12)
        self.set_actor(triggerId=6000, visible=True, initialSequence='Idle_A')
        self.select_camera_path(pathIds=[902,903], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='13'):
            return 화면끄기(self.ctx)


class 화면끄기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='14', seconds=2)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='14'):
            return 어린벨라소멸(self.ctx)


class 어린벨라소멸(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='15', seconds=1)
        self.destroy_monster(spawnIds=[5000])
        self.set_actor(triggerId=6000, visible=False, initialSequence='Idle_A')
        self.create_monster(spawnIds=[6001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='15'):
            return 벨라연출01(self.ctx)


class 벨라연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='16', seconds=8)
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=6001, patrolName='MS2PatrolData_2001')
        self.select_camera_path(pathIds=[904,905], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='16'):
            return 벨라연출종료(self.ctx)


class 벨라연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='17', seconds=8)
        self.select_camera(triggerId=905, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='17'):
            return 이동딜레이(self.ctx)


class 이동딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10000], questIds=[10002611], questStates=[3]):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='19', seconds=10)
        self.move_user(mapId=3009017, portalId=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='19'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=10)
        self.destroy_monster(spawnIds=[6001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='20'):
            return 대기(self.ctx)


initial_state = 대기
