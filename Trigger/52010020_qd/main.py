""" trigger/52010020_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=4)
        self.create_monster(spawnIds=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701]):
            return Event_Ready(self.ctx)


class Event_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2001')
        self.set_conversation(type=1, spawnId=102, script='$52010020_QD__MAIN__0$', arg4=5)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2002')
        self.set_conversation(type=1, spawnId=101, script='$52010020_QD__MAIN__1$', arg4=5)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7001], visible=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2004')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2001')
        self.move_user(mapId=52010020, portalId=1, boxId=701)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[103])
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2003')
        self.select_camera_path(pathIds=[8001,8002], returnView=False) # 사이드뷰 카메라
        # self.select_camera(triggerId=8001, enable=True)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001502, script='$52010020_QD__MAIN__2$', arg4=4)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2001')
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_05(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=4)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return end(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(triggerId=701, type='trigger', achieve='luanDialogue')
        self.select_camera(triggerId=8001, enable=False)
        self.move_user(mapId=52010019, portalId=2, boxId=701)


class end(trigger_api.Trigger):
    pass


initial_state = idle
