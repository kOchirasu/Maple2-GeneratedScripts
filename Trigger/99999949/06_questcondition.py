""" trigger/99999949/06_questcondition.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[11000064], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9051]):
            self.add_effect_nif(spawnId=11000064, nifPath='Map\Royalcity\Indoor\ry_in_cubric_mat_A01.nif', isOutline=True, scale=0.5, rotateZ=45)
            self.face_emotion(emotionName='Ride_Idle_000')
            return Wait2(self.ctx)


class Wait2(common.Trigger):
    def on_enter(self):
        self.debug_string(string='AddEffectNif 테스트')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Guide(self.ctx)

    def on_exit(self):
        self.remove_effect_nif(spawnId=11000064)
        self.face_emotion()


class Guide(common.Trigger):
    def on_enter(self):
        self.debug_string(string='40002673퀘스트 완료가능 or 완료 상태를 만들고 6번 영역안에 들어가보세요.')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9050], questIds=[40002673,40002674,40002675,40002676,40002677,40002678,40002679], questStates=[1]):
            return NpcChange01(self.ctx)


class NpcChange01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[11000064])
        self.create_monster(spawnIds=[11000044], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[11000044])
        self.debug_string(string='5초 후에 트리거가 리셋됩니다. 6번 영역 밖으로 나가세요.')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait(self.ctx)


initial_state = Wait
