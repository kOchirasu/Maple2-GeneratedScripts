""" trigger/52020001_qd/main_2.xml """
import trigger_api


class 차감지2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2]):
            return 잠시기다림_1(self.ctx)


class 잠시기다림_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 타이머시작(self.ctx)

    def on_exit(self) -> None:
        self.set_event_ui(type=1, arg2='폭격이 더욱 거세집니다. 서둘러 이동하세요!', arg3='4000')


class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='101', seconds=180, startDelay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 몬스터출현_3(self.ctx)


class 몬스터출현_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[6100002], animationEffect=False)
        self.create_monster(spawnIds=[6000011], animationEffect=False)
        self.create_monster(spawnIds=[6000012], animationEffect=False)
        self.create_monster(spawnIds=[6000013], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터사망_3(self.ctx)
        if self.time_expired(timerId='101'):
            return 실패(self.ctx)


class 몬스터사망_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[6000011]) and self.monster_dead(boxIds=[6000012]) and self.monster_dead(boxIds=[6000013]):
            return 몬스터출현_4(self.ctx)
        if self.time_expired(timerId='101'):
            return 실패(self.ctx)


class 몬스터출현_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[6000014], animationEffect=False)
        self.create_monster(spawnIds=[6000015], animationEffect=False)
        self.create_monster(spawnIds=[6000016], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터사망_4(self.ctx)
        if self.time_expired(timerId='101'):
            return 실패(self.ctx)


class 몬스터사망_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[6000014]) and self.monster_dead(boxIds=[6000015]) and self.monster_dead(boxIds=[6000016]):
            return 생성_2(self.ctx)
        if self.time_expired(timerId='101'):
            return 실패(self.ctx)


class 생성_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timerId='101')
        self.set_interact_object(triggerIds=[10002002], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 작동_2(self.ctx)


class 작동_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002002], stateValue=0):
            return 연출시작_2(self.ctx)


class 연출시작_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[6100002])
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.visible_my_pc(isVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[2000005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 폭발_2(self.ctx)


class 폭발_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 맵폭발연출_1(self.ctx)


class 맵폭발연출_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10031], visible=True)
        self.set_skill(triggerIds=[6004], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return 카메라연출(self.ctx)


class 카메라연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[2000006], returnView=False)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return pc소환_2(self.ctx)


class pc소환_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=True)
        self.move_user(mapId=52020001, portalId=12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return 카메라리셋(self.ctx)


class 카메라리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=16, visible=True, enable=True, minimapVisible=False)
        self.reset_camera(interpolationTime=0.8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            pass


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10090], visible=True)
        self.set_effect(triggerIds=[10091], visible=True)
        self.set_effect(triggerIds=[10092], visible=True)
        self.set_mesh(triggerIds=[80000], visible=True, arg3=0, delay=0, scale=0)
        self.destroy_monster(spawnIds=[-1])
        self.set_event_ui(type=1, arg2='미션에 실패하였습니다. 다시 재도전 해보세요.', arg3='4000')
        self.move_user(mapId=52020001, portalId=99)
        self.set_portal(portalId=14, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            pass


initial_state = 차감지2
