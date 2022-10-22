""" trigger/52000041_qd/main.xml """
from common import *
import state


class 완료조건체크50001392(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[606], visible=False)

    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[199], questIds=[50001392], questStates=[3]):
            return 상태01()
        if quest_user_detected(boxIds=[199], questIds=[50001392], questStates=[3]):
            return 상태02조건()


class 진행조건체크50001402(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50001402], questStates=[1]):
            return 연출시작()
        if not quest_user_detected(boxIds=[199], questIds=[50001402], questStates=[1]):
            return 진행조건체크50001400()


class 진행조건체크50001400(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50001400], questStates=[1]):
            return 상태02()
        if quest_user_detected(boxIds=[199], questIds=[50001400], questStates=[2]):
            return 상태02()
        if quest_user_detected(boxIds=[199], questIds=[50001400], questStates=[3]):
            return 상태02()
        if wait_tick(waitTick=1000):
            return 상태01()


class 상태02조건(state.State):
    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[199], questIds=[50001421], questStates=[3]):
            return 진행조건체크50001402()
        if quest_user_detected(boxIds=[199], questIds=[50001421], questStates=[3]):
            return 상태03조건()


class 상태03조건(state.State):
    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[199], questIds=[50001431], questStates=[3]):
            return 상태03()
        if quest_user_detected(boxIds=[199], questIds=[50001431], questStates=[3]):
            return 상태03_2조건()


class 상태03_2조건(state.State):
    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[199], questIds=[50001432], questStates=[3]):
            return 상태03()
        if quest_user_detected(boxIds=[199], questIds=[50001432], questStates=[3]):
            return 상태04조건()


class 상태04조건(state.State):
    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[199], questIds=[50001433], questStates=[3]):
            return 상태04()
        if quest_user_detected(boxIds=[199], questIds=[50001432], questStates=[2]):
            return 상태07()
        if quest_user_detected(boxIds=[199], questIds=[50001433], questStates=[3]):
            return 상태05조건()


class 상태05조건(state.State):
    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[199], questIds=[50001444], questStates=[3]):
            return 상태05()
        if quest_user_detected(boxIds=[199], questIds=[50001444], questStates=[3]):
            return 상태06조건()


class 상태06조건(state.State):
    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[199], questIds=[50001450], questStates=[3]):
            return 상태06()
        if quest_user_detected(boxIds=[199], questIds=[50001450], questStates=[3]):
            return 상태06_2조건()
        if wait_tick(waitTick=100):
            return 종료()


class 상태06_2조건(state.State):
    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[3]):
            return 상태06()
        if quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[3]):
            return 상태07조건()
        if wait_tick(waitTick=100):
            return 종료()


class 상태07조건(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[1]):
            return 상태06()
        if quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[2]):
            return 상태07()
        if quest_user_detected(boxIds=[199], questIds=[50001453], questStates=[3]):
            return 상태08조건()
        if wait_tick(waitTick=100):
            return 종료()


class 상태08조건(state.State):
    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[3]):
            return 상태08()
        if quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[3]):
            return 종료()


class 상태01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,2001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 상태02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002,2002], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 상태03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 상태04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2004], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 상태05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1005], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 상태06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1006,2006], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 상태07(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 상태08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1000,2000,3000], arg2=False)
        set_npc_emotion_loop(spawnId=2000, sequenceName='DownIdle_A', duration=2000)
        set_npc_emotion_loop(spawnId=3000, sequenceName='Talk_A', duration=30000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC이동01()


class NPC이동01(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        move_npc(spawnId=2000, patrolName='MS2PatrolData_2000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return NPC이동02()


class NPC이동02(state.State):
    def on_enter(self):
        move_npc(spawnId=1000, patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC이동()


class PC이동(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_9000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 어흥이대사01()


class 어흥이대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_conversation(type=2, spawnId=11001729, script='$52000041_QD__MAIN__0$', arg4=3)
        set_skip(state=어흥이대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 틴차이대사01()


class 어흥이대사01스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사01()


class 틴차이대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        set_conversation(type=2, spawnId=11001708, script='$52000041_QD__MAIN__1$', arg4=3)
        set_skip(state=틴차이대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 준타대사01()


class 틴차이대사01스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사01()


class 준타대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)
        set_conversation(type=2, spawnId=11001557, script='$52000041_QD__MAIN__2$', arg4=6)
        set_skip(state=준타대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 어흥이대사02()


class 준타대사01스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 어흥이대사02()


class 어흥이대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001729, script='$52000041_QD__MAIN__3$', arg4=4)
        set_skip(state=어흥이대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 준타대사02()


class 어흥이대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사02()


class 준타대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000041_QD__MAIN__4$', arg4=5)
        set_skip(state=준타대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 준타대사02_2()


class 준타대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사02_2()


class 준타대사02_2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000041_QD__MAIN__5$', arg4=3)
        set_skip(state=준타대사02_2스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 어흥이대사03()


class 준타대사02_2스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 어흥이대사03()


class 어흥이대사03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        set_conversation(type=2, spawnId=11001729, script='$52000041_QD__MAIN__6$', arg4=3)
        set_skip(state=어흥이대사03스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC이동03()


class 어흥이대사03스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return NPC이동03()


class NPC이동03(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)
        move_npc(spawnId=1000, patrolName='MS2PatrolData_1000B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 틴차이대사02()


class 틴차이대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000041_QD__MAIN__7$', arg4=3)
        set_skip(state=틴차이대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 틴차이대사03()


class 틴차이대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사03()


class 틴차이대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000041_QD__MAIN__8$', arg4=3)
        set_skip(state=틴차이대사03스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 틴차이대사04()


class 틴차이대사03스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사04()


class 틴차이대사04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000041_QD__MAIN__9$', arg4=3)
        set_skip(state=틴차이대사04스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 말풍선대사01()


class 틴차이대사04스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 말풍선대사01()


class 말풍선대사01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1000, script='$52000041_QD__MAIN__10$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=3000, script='$52000041_QD__MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 말풍선대사02()


class 말풍선대사02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2000, script='$52000041_QD__MAIN__15$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 말풍선대사03()


class 말풍선대사03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=3000, script='$52000041_QD__MAIN__16$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 말풍선대사04()


class 말풍선대사04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1000, script='$52000041_QD__MAIN__17$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 말풍선대사05()


class 말풍선대사05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000041_QD__MAIN__18$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 준타대사03()


class 준타대사03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[605], visible=True)
        set_conversation(type=2, spawnId=11001557, script='$52000041_QD__MAIN__12$', arg4=5)
        set_skip(state=준타대사03스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 어흥이대사05()


class 준타대사03스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[605], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 어흥이대사05()


class 어흥이대사05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[606], visible=True)
        set_conversation(type=2, spawnId=11001729, script='$52000041_QD__MAIN__13$', arg4=4)
        set_skip(state=어흥이대사05스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 어흥이대사06()


class 어흥이대사05스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[606], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 어흥이대사06()


class 어흥이대사06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001729, script='$52000041_QD__MAIN__14$', arg4=1)
        set_skip(state=어흥이대사06스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return NPC이동04()


class 어흥이대사06스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return NPC이동04()


class NPC이동04(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        move_npc(spawnId=3000, patrolName='MS2PatrolData_3000')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=101, spawnIds=[3000]):
            destroy_monster(spawnIds=[3000])
            return NPC이동05()


class NPC이동05(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=False)
        move_npc(spawnId=1000, patrolName='MS2PatrolData_1000C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            destroy_monster(spawnIds=[1000,2000])
            create_monster(spawnIds=[1010,2010], arg2=False)
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='gdreunion')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


