""" trigger/02000490_bf/bossspawn.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1,2,3,4,5], visible=True, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[999], animationEffect=False) # 이벤트
        self.create_monster(spawnIds=[99], animationEffect=False) # 핑크빈
        self.create_monster(spawnIds=[90], animationEffect=False)
        self.create_monster(spawnIds=[91], animationEffect=False)
        self.create_monster(spawnIds=[92], animationEffect=False)
        self.create_monster(spawnIds=[93], animationEffect=False)
        self.create_monster(spawnIds=[94], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 종료딜레이(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 종료딜레이(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=9999998, key='BattleEnd', value=1)
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.dungeon_clear()
            return 종료(self.ctx)


class 던전실패(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_user_value(triggerId=9999998, key='BattleEnd', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.dungeon_enable_give_up(isEnable='0')


initial_state = 시작대기중
