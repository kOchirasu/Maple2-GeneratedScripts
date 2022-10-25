""" trigger/52020001_qd/main_5.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[4]):
            return 기다림(self.ctx)


class 기다림(common.Trigger):
    def on_enter(self):
        self.shadow_expedition(type='OpenBossGauge', maxGaugePoint=300, title='출력 에너지')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 체력조건_1(self.ctx)


class 체력조건_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.shadow_expedition_reach_point(point=150):
            return 알림_1(self.ctx)


class 알림_1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='에너지가 50%충전 되었습니다.', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 체력조건_2(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[6000041], animationEffect=False)
        self.create_monster(spawnIds=[6000042], animationEffect=False)
        self.add_buff(boxIds=[6000041], skillId=49286001, level=1, isPlayer=True)
        self.add_buff(boxIds=[6000042], skillId=49286001, level=1, isPlayer=True)


class 체력조건_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.shadow_expedition_reach_point(point=300):
            return 알림_5(self.ctx)

    def on_exit(self):
        self.set_achievement(type='trigger', achieve='EscapeToKritias')


class 알림_5(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='에너지가 100%충전 되었습니다.', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 알림_6(self.ctx)


class 알림_6(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='곧 최대 출력으로 돌진 합니다.', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마지막_연출(self.ctx)


class 마지막_연출(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(pathIds=[2000009], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 캐릭터숨기기(self.ctx)


class 캐릭터숨기기(common.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=False)
        self.create_monster(spawnIds=[7002], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마지막_연출_2(self.ctx)


class 마지막_연출_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return AI연출(self.ctx)


class AI연출(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.select_camera_path(pathIds=[2000013], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return AI연출_2(self.ctx)


class AI연출_2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=0, script='준비완료! 크리티아스로 돌진!', arg4=3, arg5=0)
        self.set_ai_extra_data(key='wing', value=1, boxId=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 끝(self.ctx)


class 끝(common.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='wing', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 끝_2(self.ctx)


class 끝_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 맵이동(self.ctx)


class 맵이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2020001, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None


initial_state = 시작
