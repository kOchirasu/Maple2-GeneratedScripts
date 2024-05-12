""" trigger/52010019_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102,103])


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='3', seconds=3)
        self.set_conversation(type=2, spawnId=11001292, script='$52010014_QD__MAIN__0$', arg4=3)
        self.set_skip(state=Event_02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001285, script='$52010014_QD__MAIN__1$', arg4=3)
        self.set_skip(state=Event_03)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001285, script='$52010014_QD__MAIN__2$', arg4=3)
        self.set_skip(state=Event_04)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_04(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001292, script='$52010014_QD__MAIN__3$', arg4=3)
        self.set_timer(timerId='3', seconds=3)
        self.set_skip(state=Event_05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_05(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8001, enable=False)


initial_state = idle
