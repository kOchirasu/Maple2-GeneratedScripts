""" trigger/02000066_bf/pato.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[1299]):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[103], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=301, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[1601], animationEffect=False)
        self.create_monster(spawnIds=[1602], animationEffect=False)
        self.create_monster(spawnIds=[1603], animationEffect=False)
        self.create_monster(spawnIds=[1604], animationEffect=False)
        self.set_skip(state=연출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 연출진행(self.ctx)


class 연출진행(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__PATO__0$', arg4=2)
        self.set_skip(state=연출종료)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2429):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=103, skillId=70000107)
        self.select_camera(triggerId=301, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 시작
