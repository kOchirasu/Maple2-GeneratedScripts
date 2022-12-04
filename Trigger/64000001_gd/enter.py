""" trigger/64000001_gd/enter.xml """
import trigger_api


class PvP(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[701], visible=False)
        self.set_effect(triggerIds=[702], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.set_pvp_zone(boxId=101, arg2=30, duration=120, additionalEffectId=90001002, arg5=4, boxIds=[102,103,112,113,10,11,1,3])
            return PvP종료(self.ctx)


class PvP종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.pvp_zone_ended(boxId=101):
            return 게임종료(self.ctx)


class 게임종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='999', seconds=4, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='999'):
            return 완료(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='999')


class 완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=60)
        # action name="포탈을설정한다" arg1="1" arg2="1" arg3="1" arg4="1"/

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.move_user(mapId=0, portalId=0)
            return None


initial_state = PvP
