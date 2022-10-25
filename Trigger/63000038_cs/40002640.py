""" trigger/63000038_cs/40002640.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_off')
        self.set_actor(triggerId=202, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_off')
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3400], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3401], visible=True, arg3=0, delay=0, scale=0)
        self.set_sound(triggerId=13500, enable=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199], jobCode=100):
            return 퀘스트분기_스트라이커(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=110):
            return 퀘스트분기_소울바인더(self.ctx)


class 퀘스트분기_스트라이커(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[101], questIds=[40002640], questStates=[1]):
            return 차연출시작1(self.ctx)
        if self.quest_user_detected(boxIds=[101], questIds=[40002640], questStates=[2]):
            self.move_user(mapId=63000038, portalId=2)
            return 수락대기40002641(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[40002640], questStates=[3]):
            self.move_user(mapId=63000038, portalId=2)
            return 수락대기40002641(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[40002641], questStates=[1]):
            self.move_user(mapId=63000038, portalId=2)
            return 포털생성(self.ctx)


class 퀘스트분기_소울바인더(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[101], questIds=[40002650], questStates=[1]):
            return 차연출시작1(self.ctx)
        if self.quest_user_detected(boxIds=[101], questIds=[40002650], questStates=[2]):
            return 차연출시작1(self.ctx)
        if self.quest_user_detected(boxIds=[101], questIds=[40002650], questStates=[3]):
            return 차연출시작1(self.ctx)
        if self.quest_user_detected(boxIds=[101], questIds=[40002651], questStates=[1]):
            return 차연출시작1(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[40002651], questStates=[2]):
            self.move_user(mapId=63000038, portalId=2)
            return 완료가능40002651(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[40002651], questStates=[3]):
            self.move_user(mapId=63000038, portalId=2)
            return 완료가능40002651(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[40002652], questStates=[1]):
            self.move_user(mapId=63000040, portalId=1)
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[40002652], questStates=[2]):
            self.move_user(mapId=63000040, portalId=1)
            return 종료(self.ctx)


class 차연출시작1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=2001, sequenceName='Attack_Idle_A', duration=1E+10)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199], jobCode=100):
            self.create_monster(spawnIds=[1001], animationEffect=False)
            self.set_npc_emotion_loop(spawnId=1001, sequenceName='Attack_Idle_A', duration=1E+10)
            return 차연출딜레이1(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=110):
            self.create_monster(spawnIds=[11001], animationEffect=False)
            self.set_npc_emotion_loop(spawnId=11001, sequenceName='Attack_Idle_A', duration=1E+10)
            return 차연출딜레이1(self.ctx)


class 차연출딜레이1(common.Trigger):
    def on_enter(self):
        self.set_skip(state=차연출종료1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차연출종료1(self.ctx)


class 차연출종료1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)
        self.create_monster(spawnIds=[2101,2102], animationEffect=False)
        self.set_user_value(triggerId=99999002, key='Setlever', value=1)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2101]):
            return 계단생성(self.ctx)
        if self.monster_dead(boxIds=[2102]):
            return 계단생성(self.ctx)


class 계단생성(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2001])
        self.create_monster(spawnIds=[2002], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=2002, sequenceName='Attack_Idle_A', duration=1E+10)
        self.destroy_monster(spawnIds=[2101,2102])
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            return 차전투대기2(self.ctx)


class 차전투대기2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199], jobCode=100):
            self.destroy_monster(spawnIds=[1001])
            self.create_monster(spawnIds=[1002], animationEffect=False)
            self.set_npc_emotion_loop(spawnId=1002, sequenceName='Attack_Idle_A', duration=1E+10)
            return 차전투2(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=110):
            self.destroy_monster(spawnIds=[11001])
            self.create_monster(spawnIds=[11002], animationEffect=False)
            self.set_npc_emotion_loop(spawnId=11002, sequenceName='Attack_Idle_A', duration=1E+10)
            return 차전투2(self.ctx)


class 차전투2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2103], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2103]):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3400], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_on')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103], jobCode=100):
            return 차연출시작2(self.ctx)
        if self.user_detected(boxIds=[103], jobCode=110):
            return 차연출시작_소울바인더2(self.ctx)


class 차연출시작2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 칸두라대사01(self.ctx)


class 칸두라대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__0$', arg4=3)
        self.set_skip(state=칸두라대사01스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 칸두라대사02(self.ctx)


class 칸두라대사01스킵(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칸두라대사02(self.ctx)


class 칸두라대사02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__1$', arg4=5)
        self.set_skip(state=칸두라대사02스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 칸두라공격(self.ctx)


class 칸두라대사02스킵(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칸두라공격(self.ctx)


class 칸두라공격(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)
        self.set_npc_emotion_sequence(spawnId=2002, sequenceName='Attack_01_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return 칸두라공격이펙트(self.ctx)


class 칸두라공격이펙트(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return 가로막기(self.ctx)


class 가로막기(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=303, enable=True)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 처맞기(self.ctx)


class 처맞기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.select_camera(triggerId=304, enable=True)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002B')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 처맞기후딜레이(self.ctx)


class 처맞기후딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_npc_emotion_loop(spawnId=1002, sequenceName='Down_Idle_A', duration=1E+10)
            return NPC대사01(self.ctx)


class NPC대사01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=307, enable=True)
        self.set_conversation(type=2, spawnId=11001782, script='$63000038_CS__40002640__2$', arg4=3)
        self.set_skip(state=NPC대사01스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC대사02(self.ctx)


class NPC대사01스킵(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NPC대사02(self.ctx)


class NPC대사02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001782, script='$63000038_CS__40002640__3$', arg4=4)
        self.set_skip(state=NPC대사02스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 칸두라대사03(self.ctx)


class NPC대사02스킵(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칸두라대사03(self.ctx)


class 칸두라대사03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__4$', arg4=5)
        self.set_skip(state=칸두라대사03스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 칸투라이동(self.ctx)


class 칸두라대사03스킵(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칸투라이동(self.ctx)


class 차연출시작_소울바인더2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 칸두라대사01_소울바인더(self.ctx)


class 칸두라대사01_소울바인더(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__5$', arg4=4)
        self.set_skip(state=칸두라대사01스킵_소울바인더)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 칸두라대사02_소울바인더(self.ctx)


class 칸두라대사01스킵_소울바인더(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칸두라대사02_소울바인더(self.ctx)


class 칸두라대사02_소울바인더(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__6$', arg4=4)
        self.set_skip(state=칸두라대사02스킵_소울바인더)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 칸두라공격_소울바인더(self.ctx)


class 칸두라대사02스킵_소울바인더(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칸두라공격_소울바인더(self.ctx)


class 칸두라공격_소울바인더(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)
        self.set_npc_emotion_sequence(spawnId=2002, sequenceName='Attack_01_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return 칸두라공격이펙트_소울바인더(self.ctx)


class 칸두라공격이펙트_소울바인더(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return 가로막기_소울바인더(self.ctx)


class 가로막기_소울바인더(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=303, enable=True)
        self.move_npc(spawnId=11002, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 처맞기_소울바인더(self.ctx)


class 처맞기_소울바인더(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.select_camera(triggerId=304, enable=True)
        self.move_npc(spawnId=11002, patrolName='MS2PatrolData_1002B')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 처맞기후딜레이_소울바인더(self.ctx)


class 처맞기후딜레이_소울바인더(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_npc_emotion_loop(spawnId=11002, sequenceName='Down_Idle_A', duration=1E+10)
            return 칸두라대사03_소울바인더(self.ctx)


class 칸두라대사03_소울바인더(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__7$', arg4=3)
        self.set_skip(state=칸두라대사03스킵_소울바인더)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 칸두라대사04_소울바인더(self.ctx)


class 칸두라대사03스킵_소울바인더(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칸두라대사04_소울바인더(self.ctx)


class 칸두라대사04_소울바인더(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__8$', arg4=6)
        # Missing State: 칸두라대사04스킵_소울바인더
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 칸투라이동(self.ctx)


class 칸두라대사04스킵_소울바인더_소울바인더(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칸투라이동(self.ctx)


class 칸투라이동(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2104,2105], animationEffect=False)
        # action name="NPC를이동시킨다" arg1="2002" arg2="MS2PatrolData_2002"/

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 차연출종료2(self.ctx)


class 차연출종료2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=305, enable=False)
        self.destroy_monster(spawnIds=[2002])
        self.create_monster(spawnIds=[2001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='FirstPhaseEnd', value=1):
            self.set_mesh(triggerIds=[3401], visible=False, arg3=0, delay=0, scale=0)
            self.set_actor(triggerId=202, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_on')
            return 차연출시작3(self.ctx)


class 차연출시작3(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[2104,2105])
        self.select_camera(triggerId=306, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return 차연출분기3(self.ctx)


class 차연출분기3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199], jobCode=100):
            return 차연출종료3(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=110):
            return NPC교체_소울바인더(self.ctx)


class NPC교체_소울바인더(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='KillallShadow')
        self.destroy_monster(spawnIds=[11002])
        self.create_monster(spawnIds=[11003], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 차연출종료3(self.ctx)


class 차연출종료3(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99999004, key='BossGuide', value=1)
        self.select_camera(triggerId=307, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ChangeBGM', value=1):
            return HP50퍼센트대기(self.ctx)


class HP50퍼센트대기(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=13500, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CallFriendlyNPC', value=1):
            return 차소환분기4(self.ctx)


class 차소환분기4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199], jobCode=100):
            self.destroy_monster(spawnIds=[1002])
            self.create_monster(spawnIds=[1003], animationEffect=True)
            return NPC소환(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[40002651], questStates=[1]):
            self.destroy_monster(spawnIds=[11003])
            self.create_monster(spawnIds=[11004], animationEffect=True)
            return NPC소환(self.ctx)


class NPC소환(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleEnd', value=1):
            return NPC원위치딜레이(self.ctx)


class NPC원위치딜레이(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=13500, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 차원위치분기5(self.ctx)


class 차원위치분기5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199], jobCode=100):
            return NPC원위치(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=110):
            return NPC원위치_소울바인더(self.ctx)


class NPC원위치(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=104, spawnIds=[1003]):
            return 수락대기40002641(self.ctx)


class 수락대기40002641(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1003])
        self.create_monster(spawnIds=[1004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[40002641], questStates=[1]):
            return 포털생성(self.ctx)


class NPC원위치_소울바인더(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=11004, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=104, spawnIds=[11004]):
            return 소울바인더연출시작(self.ctx)


class 소울바인더연출시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=63000038, portalId=3)
        self.destroy_monster(spawnIds=[11004])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 준타틴차이등장(self.ctx)


class 준타틴차이등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[13001,13002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 준타대사01(self.ctx)


class 준타대사01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=308, enable=True)
        self.set_conversation(type=2, spawnId=11001557, script='$63000038_CS__40002640__9$', arg4=5)
        self.set_skip(state=준타대사01스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 칸두라대사05(self.ctx)


class 준타대사01스킵(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칸두라대사05(self.ctx)


class 칸두라대사05(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=311, enable=True)
        self.create_monster(spawnIds=[2004], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=2004, sequenceName='Attack_Idle_A', duration=1E+10)
        self.set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__10$', arg4=5)
        self.set_skip(state=칸두라대사05스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 칸두라대사06(self.ctx)


class 칸두라대사05스킵(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 칸두라대사06(self.ctx)


class 칸두라대사06(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__11$', arg4=3)
        self.set_skip(state=칸두라대사06스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 비전등장(self.ctx)


class 칸두라대사06스킵(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 비전등장(self.ctx)


class 비전등장(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=309, enable=True)
        self.create_monster(spawnIds=[14001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 칸두라공격02(self.ctx)


class 칸두라공격02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=True)
        self.set_npc_emotion_sequence(spawnId=2004, sequenceName='Attack_01_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return 비전대신맞기(self.ctx)


class 비전대신맞기(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=310, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 비전대신맞기이펙트(self.ctx)


class 비전대신맞기이펙트(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 동영상시작(self.ctx)


class 동영상시작(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Cut_Farewell_Vision.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 완료가능40002651(self.ctx)

    def on_exit(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='DisappearKandura')


class 완료가능40002651(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=310, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[13001,13002,14001,2004])
        self.create_monster(spawnIds=[13003,13004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[40002652], questStates=[1]):
            self.move_user(mapId=63000040, portalId=1)
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[40002652], questStates=[2]):
            self.move_user(mapId=63000040, portalId=1)
            return 종료(self.ctx)


class 포털생성(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26300381, textId=26300381, duration=3000)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
