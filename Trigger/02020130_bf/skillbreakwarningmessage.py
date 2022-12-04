""" trigger/02020130_bf/skillbreakwarningmessage.xml """
import trigger_api


# 이슈라 렌듀비앙 유페리아가 죽었을 때 메시지 알림 기능도 있음
class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=601, boxId=1):
            return 신호받기대기중(self.ctx)


class 신호받기대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='WarningMessage', value=0) # 다음 사용을 위해 꼭 WarningMessage 변수 0으로 초기화 하기, 이 변수는 여기서 초기화 해야지 그렇지 않으면 3번 보내는 신호를 다 받아서 메지시 여러번 뜨게 됨

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WarningMessage', value=1):
            return 스킬브레이크메시지출력(self.ctx)
        if self.user_value(key='DeathIshuraRbladerDark', value=1):
            return 이슈라죽음알림(self.ctx)
        if self.user_value(key='DeathRenduebianRbladerDark', value=1):
            return 렌듀비앙죽음알림(self.ctx)
        if self.user_value(key='DeathYuperiaRbladerDark', value=1):
            return 유페리아죽음알림(self.ctx)


class 스킬브레이크메시지출력(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20051001, textId=20051001) # 스킬브레이크 작동되었음을 이 UI 메시지로 알려주기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 천천히다시처음으로돌아가기직전(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20051001)


class 이슈라죽음알림(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20051002, textId=20051002) # 이슈라의 죽음을 이 UI 메시지로 알려주기
        self.set_user_value(key='DeathIshuraRbladerDark', value=0) # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3200): # 아슈라 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
            return 신호받기대기중(self.ctx)
        if self.user_value(key='DeathRenduebianRbladerDark', value=1):
            return 렌듀비앙죽음알림(self.ctx)
        if self.user_value(key='DeathYuperiaRbladerDark', value=1):
            return 유페리아죽음알림(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20051002)


class 렌듀비앙죽음알림(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20051003, textId=20051003) # 렌듀비앙의 죽음을 이 UI 메시지로 알려주기
        self.set_user_value(key='DeathRenduebianRbladerDark', value=0) # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3200): # 렌듀비앙 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
            return 신호받기대기중(self.ctx)
        if self.user_value(key='DeathIshuraRbladerDark', value=1):
            return 이슈라죽음알림(self.ctx)
        if self.user_value(key='DeathYuperiaRbladerDark', value=1):
            return 유페리아죽음알림(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20051003)


class 유페리아죽음알림(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20051004, textId=20051004) # 유페리아의 죽음을 이 UI 메시지로 알려주기
        self.set_user_value(key='DeathYuperiaRbladerDark', value=0) # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3200): # 유페리아 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
            return 신호받기대기중(self.ctx)
        if self.user_value(key='DeathIshuraRbladerDark', value=1):
            return 이슈라죽음알림(self.ctx)
        if self.user_value(key='DeathRenduebianRbladerDark', value=1):
            return 렌듀비앙죽음알림(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20051004)


class 천천히다시처음으로돌아가기직전(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 신호받기대기중(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
