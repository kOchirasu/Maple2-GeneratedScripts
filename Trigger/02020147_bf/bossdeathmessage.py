""" trigger/02020147_bf/bossdeathmessage.xml """
import common


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=601, boxId=1):
            return 변수초기화(self.ctx)


class 변수초기화(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='DeathIshuraRbladerDark', value=0)
        self.set_user_value(key='DeathRenduebianRbladerDark', value=0)
        self.set_user_value(key='DeathYuperiaRbladerDark', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 신호받기대기중(self.ctx)


class 신호받기대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='DeathIshuraRbladerDark', value=1):
            return 이슈라죽음알림(self.ctx)
        if self.user_value(key='DeathRenduebianRbladerDark', value=1):
            return 렌듀비앙죽음알림(self.ctx)
        if self.user_value(key='DeathYuperiaRbladerDark', value=1):
            return 유페리아죽음알림(self.ctx)


class 이슈라죽음알림(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20051002, textId=20051002) # 이슈라의 죽음을 이 UI 메시지로 알려주기
        self.set_user_value(key='DeathIshuraRbladerDark', value=0) # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3200): # 이슈라 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
            return 신호받기대기중(self.ctx)
        if self.user_value(key='DeathRenduebianRbladerDark', value=1):
            return 렌듀비앙죽음알림(self.ctx)
        if self.user_value(key='DeathYuperiaRbladerDark', value=1):
            return 유페리아죽음알림(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20051002)


class 렌듀비앙죽음알림(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20051003, textId=20051003) # 렌듀비앙의 죽음을 이 UI 메시지로 알려주기
        self.set_user_value(key='DeathRenduebianRbladerDark', value=0) # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3200): # 렌듀비앙 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
            return 신호받기대기중(self.ctx)
        if self.user_value(key='DeathIshuraRbladerDark', value=1):
            return 이슈라죽음알림(self.ctx)
        if self.user_value(key='DeathYuperiaRbladerDark', value=1):
            return 유페리아죽음알림(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20051003)


class 유페리아죽음알림(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20051004, textId=20051004) # 유페리아의 죽음을 이 UI 메시지로 알려주기
        self.set_user_value(key='DeathYuperiaRbladerDark', value=0) # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3200): # 유페리아 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
            return 신호받기대기중(self.ctx)
        if self.user_value(key='DeathIshuraRbladerDark', value=1):
            return 이슈라죽음알림(self.ctx)
        if self.user_value(key='DeathRenduebianRbladerDark', value=1):
            return 렌듀비앙죽음알림(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20051004)


initial_state = Ready
