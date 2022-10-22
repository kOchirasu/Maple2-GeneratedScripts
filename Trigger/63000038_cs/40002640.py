""" trigger/63000038_cs/40002640.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_off')
        set_actor(triggerId=202, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_off')
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3400], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3401], visible=True, arg3=0, arg4=0, arg5=0)
        set_sound(triggerId=13500, arg2=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199], jobCode=100):
            return 퀘스트분기_스트라이커()
        if user_detected(boxIds=[199], jobCode=110):
            return 퀘스트분기_소울바인더()


class 퀘스트분기_스트라이커(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[40002640], questStates=[1]):
            return 차연출시작1()
        if quest_user_detected(boxIds=[101], questIds=[40002640], questStates=[2]):
            move_user(mapId=63000038, portalId=2)
            return 수락대기40002641()
        if quest_user_detected(boxIds=[199], questIds=[40002640], questStates=[3]):
            move_user(mapId=63000038, portalId=2)
            return 수락대기40002641()
        if quest_user_detected(boxIds=[199], questIds=[40002641], questStates=[1]):
            move_user(mapId=63000038, portalId=2)
            return 포털생성()


class 퀘스트분기_소울바인더(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[40002650], questStates=[1]):
            return 차연출시작1()
        if quest_user_detected(boxIds=[101], questIds=[40002650], questStates=[2]):
            return 차연출시작1()
        if quest_user_detected(boxIds=[101], questIds=[40002650], questStates=[3]):
            return 차연출시작1()
        if quest_user_detected(boxIds=[101], questIds=[40002651], questStates=[1]):
            return 차연출시작1()
        if quest_user_detected(boxIds=[199], questIds=[40002651], questStates=[2]):
            move_user(mapId=63000038, portalId=2)
            return 완료가능40002651()
        if quest_user_detected(boxIds=[199], questIds=[40002651], questStates=[3]):
            move_user(mapId=63000038, portalId=2)
            return 완료가능40002651()
        if quest_user_detected(boxIds=[199], questIds=[40002652], questStates=[1]):
            move_user(mapId=63000040, portalId=1)
            return 종료()
        if quest_user_detected(boxIds=[199], questIds=[40002652], questStates=[2]):
            move_user(mapId=63000040, portalId=1)
            return 종료()


class 차연출시작1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[2001], arg2=False)
        set_npc_emotion_loop(spawnId=2001, sequenceName='Attack_Idle_A', duration=1E+10)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199], jobCode=100):
            create_monster(spawnIds=[1001], arg2=False)
            set_npc_emotion_loop(spawnId=1001, sequenceName='Attack_Idle_A', duration=1E+10)
            return 차연출딜레이1()
        if user_detected(boxIds=[199], jobCode=110):
            create_monster(spawnIds=[11001], arg2=False)
            set_npc_emotion_loop(spawnId=11001, sequenceName='Attack_Idle_A', duration=1E+10)
            return 차연출딜레이1()


class 차연출딜레이1(state.State):
    def on_enter(self):
        set_skip(state=차연출종료1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차연출종료1()


class 차연출종료1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)
        create_monster(spawnIds=[2101,2102], arg2=False)
        set_user_value(triggerId=99999002, key='Setlever', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2101]):
            return 계단생성()
        if monster_dead(boxIds=[2102]):
            return 계단생성()


class 계단생성(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2001])
        create_monster(spawnIds=[2002], arg2=False)
        set_npc_emotion_loop(spawnId=2002, sequenceName='Attack_Idle_A', duration=1E+10)
        destroy_monster(spawnIds=[2101,2102])
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 차전투대기2()


class 차전투대기2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199], jobCode=100):
            destroy_monster(spawnIds=[1001])
            create_monster(spawnIds=[1002], arg2=False)
            set_npc_emotion_loop(spawnId=1002, sequenceName='Attack_Idle_A', duration=1E+10)
            return 차전투2()
        if user_detected(boxIds=[199], jobCode=110):
            destroy_monster(spawnIds=[11001])
            create_monster(spawnIds=[11002], arg2=False)
            set_npc_emotion_loop(spawnId=11002, sequenceName='Attack_Idle_A', duration=1E+10)
            return 차전투2()


class 차전투2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2103], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2103]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3400], visible=False, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_on')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103], jobCode=100):
            return 차연출시작2()
        if user_detected(boxIds=[103], jobCode=110):
            return 차연출시작_소울바인더2()


class 차연출시작2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 칸두라대사01()


class 칸두라대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__0$', arg4=3)
        set_skip(state=칸두라대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 칸두라대사02()


class 칸두라대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칸두라대사02()


class 칸두라대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__1$', arg4=5)
        set_skip(state=칸두라대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 칸두라공격()


class 칸두라대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칸두라공격()


class 칸두라공격(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        set_npc_emotion_sequence(spawnId=2002, sequenceName='Attack_01_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 칸두라공격이펙트()


class 칸두라공격이펙트(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 가로막기()


class 가로막기(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 처맞기()


class 처맞기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        select_camera(triggerId=304, enable=True)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 처맞기후딜레이()


class 처맞기후딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_npc_emotion_loop(spawnId=1002, sequenceName='Down_Idle_A', duration=1E+10)
            return NPC대사01()


class NPC대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=307, enable=True)
        set_conversation(type=2, spawnId=11001782, script='$63000038_CS__40002640__2$', arg4=3)
        set_skip(state=NPC대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC대사02()


class NPC대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return NPC대사02()


class NPC대사02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001782, script='$63000038_CS__40002640__3$', arg4=4)
        set_skip(state=NPC대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 칸두라대사03()


class NPC대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칸두라대사03()


class 칸두라대사03(state.State):
    def on_enter(self):
        select_camera(triggerId=305, enable=True)
        set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__4$', arg4=5)
        set_skip(state=칸두라대사03스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 칸투라이동()


class 칸두라대사03스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칸투라이동()


class 차연출시작_소울바인더2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 칸두라대사01_소울바인더()


class 칸두라대사01_소울바인더(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__5$', arg4=4)
        set_skip(state=칸두라대사01스킵_소울바인더)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 칸두라대사02_소울바인더()


class 칸두라대사01스킵_소울바인더(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칸두라대사02_소울바인더()


class 칸두라대사02_소울바인더(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__6$', arg4=4)
        set_skip(state=칸두라대사02스킵_소울바인더)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 칸두라공격_소울바인더()


class 칸두라대사02스킵_소울바인더(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칸두라공격_소울바인더()


class 칸두라공격_소울바인더(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        set_npc_emotion_sequence(spawnId=2002, sequenceName='Attack_01_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 칸두라공격이펙트_소울바인더()


class 칸두라공격이펙트_소울바인더(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 가로막기_소울바인더()


class 가로막기_소울바인더(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)
        move_npc(spawnId=11002, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 처맞기_소울바인더()


class 처맞기_소울바인더(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        select_camera(triggerId=304, enable=True)
        move_npc(spawnId=11002, patrolName='MS2PatrolData_1002B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 처맞기후딜레이_소울바인더()


class 처맞기후딜레이_소울바인더(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_npc_emotion_loop(spawnId=11002, sequenceName='Down_Idle_A', duration=1E+10)
            return 칸두라대사03_소울바인더()


class 칸두라대사03_소울바인더(state.State):
    def on_enter(self):
        select_camera(triggerId=305, enable=True)
        set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__7$', arg4=3)
        set_skip(state=칸두라대사03스킵_소울바인더)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 칸두라대사04_소울바인더()


class 칸두라대사03스킵_소울바인더(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칸두라대사04_소울바인더()


class 칸두라대사04_소울바인더(state.State):
    def on_enter(self):
        select_camera(triggerId=305, enable=True)
        set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__8$', arg4=6)
        # Missing State: 칸두라대사04스킵_소울바인더
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 칸투라이동()


class 칸두라대사04스킵_소울바인더_소울바인더(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칸투라이동()


class 칸투라이동(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2104,2105], arg2=False) # action name="NPC를이동시킨다" arg1="2002" arg2="MS2PatrolData_2002"/

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차연출종료2()


class 차연출종료2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=305, enable=False)
        destroy_monster(spawnIds=[2002])
        create_monster(spawnIds=[2001], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='FirstPhaseEnd', value=1):
            set_mesh(triggerIds=[3401], visible=False, arg3=0, arg4=0, arg5=0)
            set_actor(triggerId=202, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_on')
            return 차연출시작3()


class 차연출시작3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[2104,2105])
        select_camera(triggerId=306, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 차연출분기3()


class 차연출분기3(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199], jobCode=100):
            return 차연출종료3()
        if user_detected(boxIds=[199], jobCode=110):
            return NPC교체_소울바인더()


class NPC교체_소울바인더(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='KillallShadow')
        destroy_monster(spawnIds=[11002])
        create_monster(spawnIds=[11003], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 차연출종료3()


class 차연출종료3(state.State):
    def on_enter(self):
        set_user_value(triggerId=99999004, key='BossGuide', value=1)
        select_camera(triggerId=307, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_value(key='ChangeBGM', value=1):
            return HP50퍼센트대기()


class HP50퍼센트대기(state.State):
    def on_enter(self):
        set_sound(triggerId=13500, arg2=True)

    def on_tick(self) -> state.State:
        if user_value(key='CallFriendlyNPC', value=1):
            return 차소환분기4()


class 차소환분기4(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199], jobCode=100):
            destroy_monster(spawnIds=[1002])
            create_monster(spawnIds=[1003], arg2=True)
            return NPC소환()
        if quest_user_detected(boxIds=[199], questIds=[40002651], questStates=[1]):
            destroy_monster(spawnIds=[11003])
            create_monster(spawnIds=[11004], arg2=True)
            return NPC소환()


class NPC소환(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BattleEnd', value=1):
            return NPC원위치딜레이()


class NPC원위치딜레이(state.State):
    def on_enter(self):
        set_sound(triggerId=13500, arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 차원위치분기5()


class 차원위치분기5(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199], jobCode=100):
            return NPC원위치()
        if user_detected(boxIds=[199], jobCode=110):
            return NPC원위치_소울바인더()


class NPC원위치(state.State):
    def on_enter(self):
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=104, spawnIds=[1003]):
            return 수락대기40002641()


class 수락대기40002641(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1003])
        create_monster(spawnIds=[1004], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[40002641], questStates=[1]):
            return 포털생성()


class NPC원위치_소울바인더(state.State):
    def on_enter(self):
        move_npc(spawnId=11004, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=104, spawnIds=[11004]):
            return 소울바인더연출시작()


class 소울바인더연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=63000038, portalId=3)
        destroy_monster(spawnIds=[11004])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 준타틴차이등장()


class 준타틴차이등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[13001,13002], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 준타대사01()


class 준타대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=308, enable=True)
        set_conversation(type=2, spawnId=11001557, script='$63000038_CS__40002640__9$', arg4=5)
        set_skip(state=준타대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 칸두라대사05()


class 준타대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칸두라대사05()


class 칸두라대사05(state.State):
    def on_enter(self):
        select_camera(triggerId=311, enable=True)
        create_monster(spawnIds=[2004], arg2=False)
        set_npc_emotion_loop(spawnId=2004, sequenceName='Attack_Idle_A', duration=1E+10)
        set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__10$', arg4=5)
        set_skip(state=칸두라대사05스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 칸두라대사06()


class 칸두라대사05스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칸두라대사06()


class 칸두라대사06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001559, script='$63000038_CS__40002640__11$', arg4=3)
        set_skip(state=칸두라대사06스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 비전등장()


class 칸두라대사06스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 비전등장()


class 비전등장(state.State):
    def on_enter(self):
        select_camera(triggerId=309, enable=True)
        create_monster(spawnIds=[14001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 칸두라공격02()


class 칸두라공격02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        set_npc_emotion_sequence(spawnId=2004, sequenceName='Attack_01_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 비전대신맞기()


class 비전대신맞기(state.State):
    def on_enter(self):
        select_camera(triggerId=310, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 비전대신맞기이펙트()


class 비전대신맞기이펙트(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 동영상시작()


class 동영상시작(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Cut_Farewell_Vision.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 완료가능40002651()

    def on_exit(self):
        set_achievement(triggerId=199, type='trigger', achieve='DisappearKandura')


class 완료가능40002651(state.State):
    def on_enter(self):
        select_camera(triggerId=310, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[13001,13002,14001,2004])
        create_monster(spawnIds=[13003,13004], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[40002652], questStates=[1]):
            move_user(mapId=63000040, portalId=1)
            return 종료()
        if quest_user_detected(boxIds=[199], questIds=[40002652], questStates=[2]):
            move_user(mapId=63000040, portalId=1)
            return 종료()


class 포털생성(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26300381, textId=26300381, duration=3000)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


