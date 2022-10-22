""" trigger/52100002_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 퀘스트체크()


class 퀘스트체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50100060], questStates=[1]):
            return 룸체크()
        if quest_user_detected(boxIds=[199], questIds=[50100060], questStates=[2]):
            return 퀘스트완료가능이거나완료1()
        if quest_user_detected(boxIds=[199], questIds=[50100060], questStates=[3]):
            return 퀘스트완료가능이거나완료1()


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 던전시작()
        if not is_dungeon_room():
            return 퀘스트던전시작()


class 던전시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002,2001], arg2=False)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2001]):
            set_effect(triggerIds=[601], visible=True)
            return 사망체크()
        if monster_dead(boxIds=[2001,2002]):
            return 사망딜레이()


class 사망체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001,2002]):
            return 사망딜레이()


class 사망딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 종료체크()


class 종료체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001,2002]):
            return 암전대기()


class 퀘스트던전시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002,2101], arg2=False)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2101]):
            set_effect(triggerIds=[601], visible=True)
            return 퀘스트사망체크()
        if monster_dead(boxIds=[2101,2102]):
            return 퀘스트사망딜레이()


class 퀘스트사망체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2101,2102]):
            return 퀘스트사망딜레이()


class 퀘스트사망딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 퀘스트종료체크()


class 퀘스트종료체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2101,2102]):
            return 암전대기()


class 암전대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 종료연출대기()


class 종료연출대기(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        move_user(mapId=52100002, portalId=2)
        destroy_monster(spawnIds=[1001,1002,2001,2002,2101,2102])
        create_monster(spawnIds=[1098,1099], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_loop(spawnId=1098, sequenceName='Dead_B', duration=3000000)
        set_npc_emotion_loop(spawnId=1099, sequenceName='Dead_B', duration=3000000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료연출()


class 종료연출(state.State):
    def on_enter(self):
        set_skip(state=연출종료)
        add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$02000392_BF__MAIN__0$', align='left', duration=4000)
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__1$', align='right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return PC대사()


class PC대사(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$02000392_BF__MAIN__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC대사2()


class PC대사2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$02000392_BF__MAIN__10$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 자매교체()


class 자매교체(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1098,1099])
        create_monster(spawnIds=[1096,1097], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 자매대화()


class 자매대화(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 자매대화01()


class 자매대화01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$02000392_BF__MAIN__3$', align='left', duration=4000)
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__4$', align='right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 자매대화02()


class 자매대화02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$02000392_BF__MAIN__5$', align='left', duration=5000)
        set_conversation(type=1, spawnId=1097, script='$02000392_BF__MAIN__6$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 자매대화03()


class 자매대화03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__11$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC대사3()


class PC대사3(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$02000392_BF__MAIN__12$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 자매대화04()


class 자매대화04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__7$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 자매대화05()


class 자매대화05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__8$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 자매대화06()


class 자매대화06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__9$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_skip()
        destroy_monster(spawnIds=[1098,1099])
        destroy_monster(spawnIds=[1096,1097])
        create_monster(spawnIds=[1096,1097], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2) # action name="카메라를선택한다" arg1="302" arg2="0"/
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 룸체크2()


class 퀘스트완료가능이거나완료1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1096,1097], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 룸체크2()


class 룸체크2(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 던전완료()
        if not is_dungeon_room():
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            return 종료()


class 던전완료(state.State):
    def on_enter(self):
        dungeon_clear()
        set_achievement(triggerId=199, type='trigger', achieve='ClearSirenSisters')
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


