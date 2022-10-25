""" trigger/52020001_qd/main_3.xml """
import common


class 차감지2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[3]):
            return 잠시기다림_1(self.ctx)


class 잠시기다림_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 타이머시작(self.ctx)


class 타이머시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='102', seconds=180, startDelay=1, interval=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 몬스터출현_5(self.ctx)


class 몬스터출현_5(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[6100003], animationEffect=False)
        self.create_monster(spawnIds=[6000018], animationEffect=False)
        self.create_monster(spawnIds=[6000019], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터체력50(self.ctx)
        if self.time_expired(timerId='102'):
            return 실패(self.ctx)


class 몬스터체력50(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.any_one():
            return 생성_2(self.ctx)
        if self.time_expired(timerId='102'):
            return 실패(self.ctx)


class 생성_2(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[6000018], skillId=49286001, level=1, isPlayer=True)
        self.add_buff(boxIds=[6000019], skillId=49286001, level=1, isPlayer=True)
        self.reset_timer(timerId='102')
        self.set_interact_object(triggerIds=[10002003], state=1)
        self.set_event_ui(type=1, arg2='아크레온이 거대해지며 모든공격을 튕겨내기 시작했습니다.', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 작동_2(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=921, key='respawn', value=1)


class 작동_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002003], stateValue=0):
            return 연출시작_2(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=921, key='respawn_end', value=2)


class 연출시작_2(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[6100003])
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.visible_my_pc(isVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000007], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 폭발_2(self.ctx)


class 폭발_2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[10002], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=900):
            return 맵폭발연출_1(self.ctx)


class 맵폭발연출_1(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[10041], visible=True)
        self.set_skill(triggerIds=[6005], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=400):
            return 카메라연출(self.ctx)


class 카메라연출(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000008], returnView=False)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.destroy_monster(spawnIds=[6000018])
        self.destroy_monster(spawnIds=[6000019])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return pc소환_2(self.ctx)


class pc소환_2(common.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=True)
        self.move_user(mapId=52020001, portalId=13)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return 맵폭발연출_2(self.ctx)


class 맵폭발연출_2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[10042], visible=True)
        self.set_skill(triggerIds=[6006], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=400):
            return 카메라리셋(self.ctx)


class 카메라리셋(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=17, visible=True, enable=True, minimapVisible=False)
        self.reset_camera(interpolationTime=0.8)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None


class 실패(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[10090], visible=True)
        self.set_effect(triggerIds=[10091], visible=True)
        self.set_effect(triggerIds=[10092], visible=True)
        self.set_mesh(triggerIds=[80000], visible=True, arg3=0, delay=0, scale=0)
        self.destroy_monster(spawnIds=[-1])
        self.set_event_ui(type=1, arg2='미션에 실패하였습니다. 다시 재도전 해보세요.', arg3='4000')
        self.move_user(mapId=52020001, portalId=99)
        self.set_portal(portalId=14, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return None


class 끝(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return None


initial_state = 차감지2
