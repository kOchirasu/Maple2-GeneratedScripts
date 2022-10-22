""" trigger/99999949/06_questcondition.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[11000064], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9051]):
            add_effect_nif(spawnId=11000064, nifPath='Map\Royalcity\Indoor\ry_in_cubric_mat_A01.nif', isOutline=True, scale=0.5, rotateZ=45)
            face_emotion(emotionName='Ride_Idle_000')
            return Wait2()


class Wait2(state.State):
    def on_enter(self):
        debug_string(string='AddEffectNif 테스트')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Guide()

    def on_exit(self):
        remove_effect_nif(spawnId=11000064)
        face_emotion()


class Guide(state.State):
    def on_enter(self):
        debug_string(string='40002673퀘스트 완료가능 or 완료 상태를 만들고 6번 영역안에 들어가보세요.')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9050], questIds=[40002673,40002674,40002675,40002676,40002677,40002678,40002679], questStates=[1]):
            return NpcChange01()


class NpcChange01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[11000064])
        create_monster(spawnIds=[11000044], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[11000044])
        debug_string(string='5초 후에 트리거가 리셋됩니다. 6번 영역 밖으로 나가세요.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait()


