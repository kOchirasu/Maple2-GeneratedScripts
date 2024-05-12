""" trigger/64000001_gd/enter.xml """
import trigger_api


class PvP(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이펙트 ID 하드코딩임으로 바꾸지 말것
        self.set_effect(triggerIds=[701], visible=False)
        self.set_effect(triggerIds=[702], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            # arg6="A길드트리거박스, B길드트리거박스, A길드선수선발박스, B길드선수선발박스, A길드이동포털, B길드이동포털, 경기장포털, 필요승수"
            # arg5가 4일 때 arg2는 (시작대기시간)으로 Timeout이 걸려있다. 변경하려면 프로그래머에게 문의
            self.set_pvp_zone(boxId=101, arg2=30, duration=120, additionalEffectId=90001002, arg5=4, boxIds=[102,103,112,113,10,11,1,3])
            return PvP종료(self.ctx)


class PvP종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.pvp_zone_ended(boxId=101):
            return 게임종료(self.ctx)


class 게임종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='999', seconds=4, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='999'):
            # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
            # self.set_achievement(triggerId=102, type='pvp_win', achieve='61000009')
            return 완료(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='999')


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=60)
        # self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.move_user(mapId=0, portalId=0)


initial_state = PvP
