""" trigger/52020001_qd/main_4.xml """
import common


class 차감지2(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002010], state=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[4]):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 카메리이동(self.ctx)


class 카메리이동(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000010], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 탈것등장(self.ctx)


class 탈것등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[7001], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 폭발_1(self.ctx)


class 폭발_1(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[10052], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 폭발_2(self.ctx)


class 폭발_2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[10053], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 폭발_3(self.ctx)


class 폭발_3(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[10054], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 맵폭발연출(self.ctx)


class 맵폭발연출(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[10051], visible=True)
        self.set_skill(triggerIds=[6007], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4400):
            return 연출끝(self.ctx)


class 연출끝(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000010], returnView=True)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 오브젝트반응(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[6100004], animationEffect=False)


class 오브젝트반응(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='좋아! 이 녀석을 타고 돌격해야겠어!!', arg4=3, arg5=0)
        self.set_interact_object(triggerIds=[10002010], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 오브젝트반응_2(self.ctx)


class 오브젝트반응_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002010], stateValue=0):
            return 오브젝트반응_3(self.ctx)


class 오브젝트반응_3(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002010], state=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 카메라연출(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[7001], arg2=False)


class 카메라연출(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 알림(self.ctx)


class 알림(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='출력이 부족해 크리티아스로 진입할 수 없습니다.', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 알림_2(self.ctx)


class 알림_2(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='적들을 처치하면 에너지를 충전할 수 있습니다.\n제한시간 내에 100%충전해, 크리티아스로 진입하세요!', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 타이머시작(self.ctx)


class 타이머시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='110', seconds=360, startDelay=1, interval=1, vOffset=80)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 몬스터생성(self.ctx)


class 몬스터생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[6000030], animationEffect=False)
        self.create_monster(spawnIds=[6000031], animationEffect=False)
        self.create_monster(spawnIds=[6000032], animationEffect=False)
        self.create_monster(spawnIds=[6000033], animationEffect=False)
        self.create_monster(spawnIds=[6000034], animationEffect=False)
        self.set_user_value(triggerId=909, key='respawn', value=1)
        self.set_user_value(triggerId=910, key='respawn', value=1)
        self.set_user_value(triggerId=911, key='respawn', value=1)
        self.set_user_value(triggerId=912, key='respawn', value=1)
        self.set_user_value(triggerId=913, key='respawn', value=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='110'):
            return 실패(self.ctx)


class 실패(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000009], returnView=True)
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


initial_state = 차감지2
