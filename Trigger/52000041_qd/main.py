""" trigger/52000041_qd/main.xml """
import trigger_api


class 완료조건체크50001392(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_effect(triggerIds=[606], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[199], questIds=[50001392], questStates=[3]):
            return 상태01(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001392], questStates=[3]):
            return 상태02조건(self.ctx)


class 진행조건체크50001402(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50001402], questStates=[1]):
            return 연출시작(self.ctx)
        if not self.quest_user_detected(boxIds=[199], questIds=[50001402], questStates=[1]):
            return 진행조건체크50001400(self.ctx)


class 진행조건체크50001400(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50001400], questStates=[1]):
            return 상태02(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001400], questStates=[2]):
            return 상태02(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001400], questStates=[3]):
            return 상태02(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 상태01(self.ctx)


class 상태02조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[199], questIds=[50001421], questStates=[3]):
            return 진행조건체크50001402(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001421], questStates=[3]):
            return 상태03조건(self.ctx)


class 상태03조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[199], questIds=[50001431], questStates=[3]):
            return 상태03(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001431], questStates=[3]):
            return 상태03_2조건(self.ctx)


class 상태03_2조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[199], questIds=[50001432], questStates=[3]):
            return 상태03(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001432], questStates=[3]):
            return 상태04조건(self.ctx)


class 상태04조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[199], questIds=[50001433], questStates=[3]):
            return 상태04(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001432], questStates=[2]):
            return 상태07(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001433], questStates=[3]):
            return 상태05조건(self.ctx)


class 상태05조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[199], questIds=[50001444], questStates=[3]):
            return 상태05(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001444], questStates=[3]):
            return 상태06조건(self.ctx)


class 상태06조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[199], questIds=[50001450], questStates=[3]):
            return 상태06(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001450], questStates=[3]):
            return 상태06_2조건(self.ctx)
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 상태06_2조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[3]):
            return 상태06(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[3]):
            return 상태07조건(self.ctx)
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 상태07조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[1]):
            return 상태06(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[2]):
            return 상태07(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001453], questStates=[3]):
            return 상태08조건(self.ctx)
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 상태08조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[3]):
            return 상태08(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[3]):
            return 종료(self.ctx)


class 상태01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1001,2001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 상태02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1002,2002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 상태03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 상태04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2004], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 상태05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1005], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 상태06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1006,2006], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 상태07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 상태08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1008], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[1000,2000,3000], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=2000, sequenceName='DownIdle_A', duration=2000)
        self.set_npc_emotion_loop(spawnId=3000, sequenceName='Talk_A', duration=30000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC이동01(self.ctx)


class NPC이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=302, enable=True)
        self.move_npc(spawnId=2000, patrolName='MS2PatrolData_2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return NPC이동02(self.ctx)


class NPC이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1000, patrolName='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC이동(self.ctx)


class PC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_9000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 어흥이대사01(self.ctx)


class 어흥이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=True)
        self.set_conversation(type=2, spawnId=11001729, script='$52000041_QD__MAIN__0$', arg4=3)
        self.set_skip(state=어흥이대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 틴차이대사01(self.ctx)


class 어흥이대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=False)
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 틴차이대사01(self.ctx)


class 틴차이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[602], visible=True)
        self.set_conversation(type=2, spawnId=11001708, script='$52000041_QD__MAIN__1$', arg4=3)
        self.set_skip(state=틴차이대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 준타대사01(self.ctx)


class 틴차이대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[602], visible=False)
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 준타대사01(self.ctx)


class 준타대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[603], visible=True)
        self.set_conversation(type=2, spawnId=11001557, script='$52000041_QD__MAIN__2$', arg4=6)
        self.set_skip(state=준타대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 어흥이대사02(self.ctx)


class 준타대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[603], visible=False)
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 어흥이대사02(self.ctx)


class 어흥이대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001729, script='$52000041_QD__MAIN__3$', arg4=4)
        self.set_skip(state=어흥이대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 준타대사02(self.ctx)


class 어흥이대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 준타대사02(self.ctx)


class 준타대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001557, script='$52000041_QD__MAIN__4$', arg4=5)
        self.set_skip(state=준타대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 준타대사02_2(self.ctx)


class 준타대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 준타대사02_2(self.ctx)


class 준타대사02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001557, script='$52000041_QD__MAIN__5$', arg4=3)
        self.set_skip(state=준타대사02_2스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 어흥이대사03(self.ctx)


class 준타대사02_2스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 어흥이대사03(self.ctx)


class 어흥이대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[604], visible=True)
        self.set_conversation(type=2, spawnId=11001729, script='$52000041_QD__MAIN__6$', arg4=3)
        self.set_skip(state=어흥이대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC이동03(self.ctx)


class 어흥이대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[604], visible=False)
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NPC이동03(self.ctx)


class NPC이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=303, enable=True)
        self.move_npc(spawnId=1000, patrolName='MS2PatrolData_1000B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 틴차이대사02(self.ctx)


class 틴차이대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001708, script='$52000041_QD__MAIN__7$', arg4=3)
        self.set_skip(state=틴차이대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 틴차이대사03(self.ctx)


class 틴차이대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 틴차이대사03(self.ctx)


class 틴차이대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001708, script='$52000041_QD__MAIN__8$', arg4=3)
        self.set_skip(state=틴차이대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 틴차이대사04(self.ctx)


class 틴차이대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 틴차이대사04(self.ctx)


class 틴차이대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001708, script='$52000041_QD__MAIN__9$', arg4=3)
        self.set_skip(state=틴차이대사04스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 말풍선대사01(self.ctx)


class 틴차이대사04스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 말풍선대사01(self.ctx)


class 말풍선대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=1000, script='$52000041_QD__MAIN__10$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=3000, script='$52000041_QD__MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 말풍선대사02(self.ctx)


class 말풍선대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=2000, script='$52000041_QD__MAIN__15$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 말풍선대사03(self.ctx)


class 말풍선대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=3000, script='$52000041_QD__MAIN__16$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 말풍선대사04(self.ctx)


class 말풍선대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=1000, script='$52000041_QD__MAIN__17$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 말풍선대사05(self.ctx)


class 말풍선대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$52000041_QD__MAIN__18$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 준타대사03(self.ctx)


class 준타대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[605], visible=True)
        self.set_conversation(type=2, spawnId=11001557, script='$52000041_QD__MAIN__12$', arg4=5)
        self.set_skip(state=준타대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 어흥이대사05(self.ctx)


class 준타대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[605], visible=False)
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 어흥이대사05(self.ctx)


class 어흥이대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[606], visible=True)
        self.set_conversation(type=2, spawnId=11001729, script='$52000041_QD__MAIN__13$', arg4=4)
        self.set_skip(state=어흥이대사05스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 어흥이대사06(self.ctx)


class 어흥이대사05스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[606], visible=False)
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 어흥이대사06(self.ctx)


class 어흥이대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001729, script='$52000041_QD__MAIN__14$', arg4=1)
        self.set_skip(state=어흥이대사06스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return NPC이동04(self.ctx)


class 어흥이대사06스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NPC이동04(self.ctx)


class NPC이동04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=302, enable=True)
        self.move_npc(spawnId=3000, patrolName='MS2PatrolData_3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=101, spawnIds=[3000]):
            self.destroy_monster(spawnIds=[3000])
            return NPC이동05(self.ctx)


class NPC이동05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=302, enable=False)
        self.move_npc(spawnId=1000, patrolName='MS2PatrolData_1000C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.destroy_monster(spawnIds=[1000,2000])
            self.create_monster(spawnIds=[1010,2010], animationEffect=False)
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=199, type='trigger', achieve='gdreunion')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 완료조건체크50001392
