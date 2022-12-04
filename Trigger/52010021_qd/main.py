""" trigger/52010021_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=False)
        self.create_monster(spawnIds=[101,102,103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002540], questStates=[3]):
            return Event_01_Idle(self.ctx)


class Event_01_Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52010021, portalId=3, boxId=701)
        self.set_timer(timerId='2', seconds=2)
        self.set_effect(triggerIds=[7001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[104])
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2002')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2004')
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2003')
        self.select_camera(triggerId=8001, enable=True)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_05(self.ctx)

    def on_exit(self):
        self.select_camera(triggerId=8001, enable=True)


class Event_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010021_QD__MAIN__0$', arg4=4)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Ending(self.ctx)


class Ending(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001,8002], returnView=False) # 사이드뷰 카메라
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2012')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2014')
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2013')
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return out(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=4)


class out(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return end(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=9, script='$52010021_QD__MAIN__1$', arg3=True)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return real_end2(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=9, script='$52010021_QD__MAIN__2$', arg3=True)
        self.play_system_sound_in_box(sound='System_Laugh_01')


class real_end2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return real_end3(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=9, script='$52010021_QD__MAIN__3$', arg3=True)


class real_end3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return real_end4(self.ctx)

    def on_exit(self):
        self.play_system_sound_in_box(sound='System_Burp_01')


class real_end4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return real_end(self.ctx)


class real_end(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='mikaEpilogueEnd')
        self.move_user(mapId=2010002, portalId=1, boxId=701)


initial_state = idle
