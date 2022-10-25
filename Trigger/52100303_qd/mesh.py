""" trigger/52100303_qd/mesh.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return 첫번째길막(self.ctx)


class 첫번째길막(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Mesh', value=2):
            self.set_mesh(triggerIds=[4002], visible=True)
            return 이페이즈(self.ctx)


class 이페이즈(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Mesh', value=3):
            self.set_ai_extra_data(key='Thunder', value=2)
            self.set_mesh(triggerIds=[4003], visible=True)
            return 삼페이즈(self.ctx)


class 삼페이즈(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Mesh', value=4):
            self.set_mesh(triggerIds=[4004], visible=True)
            self.destroy_monster(spawnIds=[111])
            return 진짜마지막(self.ctx)


class 진짜마지막(common.Trigger):
    pass


initial_state = 대기
