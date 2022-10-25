""" trigger/99999911/main.xml """
import common


# 플레이어 감지
class 최초(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=701, boxId=1):
            return 시작조건체크(self.ctx)


class 시작조건체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 어나운스0(self.ctx)
        if self.count_users(boxId=701, boxId=20):
            return 어나운스0(self.ctx)


class 어나운스0(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$99999911__MAIN__0$', arg3='4000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 어나운스1(self.ctx)


class 어나운스1(common.Trigger):
    def on_enter(self):
        self.show_count_ui(text='$61000004_ME__TRIGGER_01__1$', stage=0, count=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5500):
            self.set_mesh(triggerIds=[301,302,303], visible=False, arg3=12, delay=0)
            self.set_achievement(triggerId=101, type='trigger', achieve='dailyquest_start')
            return idle(self.ctx)


class idle(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True, animationDelay=1)
        self.create_monster(spawnIds=[102], animationEffect=True, animationDelay=2)
        self.create_monster(spawnIds=[103], animationEffect=True, animationDelay=3)
        self.create_monster(spawnIds=[104], animationEffect=True, animationDelay=4)
        self.create_monster(spawnIds=[105], animationEffect=True, animationDelay=5)
        self.create_monster(spawnIds=[106], animationEffect=True, animationDelay=6)
        self.create_monster(spawnIds=[107], animationEffect=True, animationDelay=7)
        self.create_monster(spawnIds=[108], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[301], animationEffect=True, animationDelay=1)
        self.create_monster(spawnIds=[302], animationEffect=True, animationDelay=2)
        self.create_monster(spawnIds=[303], animationEffect=True, animationDelay=3)
        self.create_monster(spawnIds=[304], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[305], animationEffect=True, animationDelay=1)
        self.create_monster(spawnIds=[306], animationEffect=True, animationDelay=2)
        self.create_monster(spawnIds=[307], animationEffect=True, animationDelay=3)
        self.create_monster(spawnIds=[308], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[309], animationEffect=True, animationDelay=1)
        self.create_monster(spawnIds=[310], animationEffect=True, animationDelay=2)
        self.create_monster(spawnIds=[311], animationEffect=True, animationDelay=3)
        self.create_monster(spawnIds=[312], animationEffect=True, animationDelay=0)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return Round1_Start(self.ctx)


class Round1_Start(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991104, key='Round_02', value=1)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return None # Missing State: random_start


initial_state = 최초
