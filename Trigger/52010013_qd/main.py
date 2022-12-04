""" trigger/52010013_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102,103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10002797], questStates=[1]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[104])
        self.set_timer(timerId='3', seconds=3)
        self.set_conversation(type=2, spawnId=11001217, script='$52010013_QD__MAIN__0$', arg4=3)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_02_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_02_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8002, enable=True)
        self.set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__1$', arg4=5)
        self.set_skip(state=Event_03_IDLE)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Event_03_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_03_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010013_QD__MAIN__2$', arg4=4)
        self.set_skip(state=Event_04_IDLE)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_04_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_04_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__3$', arg4=4)
        self.set_timer(timerId='4', seconds=4)
        self.set_skip(state=Event_05_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_05_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_05_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__4$', arg4=4)
        self.set_timer(timerId='4', seconds=4)
        self.set_skip(state=Event_06_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_06_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_06_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_06(self.ctx)


class Event_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010013_QD__MAIN__5$', arg4=5)
        self.set_timer(timerId='5', seconds=5)
        self.set_skip(state=Event_07_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Event_07_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_07_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_07(self.ctx)


class Event_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__6$', arg4=4)
        self.set_timer(timerId='3', seconds=3)
        self.set_skip(state=Event_08_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_08_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_08_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_08(self.ctx)


class Event_08(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010013_QD__MAIN__7$', arg4=4)
        self.set_timer(timerId='4', seconds=4)
        self.set_skip(state=Event_09_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_09_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_09_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_09(self.ctx)


class Event_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__8$', arg4=3)
        self.set_timer(timerId='3', seconds=3)
        self.set_skip(state=Event_10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_10(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__9$', arg4=4)
        self.set_timer(timerId='4', seconds=4)
        self.set_skip(state=End)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return End(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.select_camera(triggerId=8001, enable=False)
        self.select_camera(triggerId=8002, enable=False)


class End(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='DragonMika')
        self.move_user(mapId=2010002, portalId=13, boxId=701)


initial_state = idle
