""" trigger/99999999_bf/main.xml """
from common import *
import state


#  심연의 성채 
#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5000], visible=True)
        set_mesh(triggerIds=[8900], visible=True)
        set_mesh(triggerIds=[8901], visible=True)
        set_mesh(triggerIds=[8902], visible=True)
        set_mesh(triggerIds=[8903], visible=True)
        set_mesh(triggerIds=[8904], visible=True)
        set_mesh(triggerIds=[8905], visible=True)
        set_effect(triggerIds=[8000], visible=False)
        set_effect(triggerIds=[8001], visible=False)
        set_skill(triggerIds=[9000], isEnable=False)
        enable_spawn_point_pc(spawnId=0, isEnable=True)
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=False)
        enable_spawn_point_pc(spawnId=3, isEnable=False)
        enable_spawn_point_pc(spawnId=4, isEnable=False)
        enable_spawn_point_pc(spawnId=5, isEnable=False)
        enable_spawn_point_pc(spawnId=6, isEnable=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 카메라경로()


class 카메라경로(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False)
        select_camera_path(pathIds=[7000,7001], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라리셋()


class 카메라리셋(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701], jobCode=0):
            return ready()


#  첫번째 발판
class ready(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        set_event_ui(type=1, arg2='까마득한 성채를 따라 내려가야 합니다.\n몰려오는 어둠을 조심하세요.', arg3='3000')
        create_monster(spawnIds=[101,1011,1012,1013,1014,1017,1018,1019], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,1011,1012,1013,1014,1017,1018,1019]):
            return 도마뱀스폰1()


class 도마뱀스폰1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8900], visible=False)
        create_monster(spawnIds=[1015,1016], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702], jobCode=0):
            return 시작702()


class 시작702(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=1, isEnable=True)
        create_monster(spawnIds=[102,1022,1023,1024,1025], arg2=True)
        side_npc_talk(npcId=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='인간? 이게 얼마 만에 맡아보는 인간 냄새인지... 아주 향긋하군. 천천히 어둠 속으로 내려오라고.')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102,1022,1023,1024,1025]):
            return 마무리1_702()


class 마무리1_702(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8901], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마무리2_702()


class 마무리2_702(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='불쌍한 인간... 샘은 이미 너를 주시하고 있어. 어둠이 너를 쫓을거야.')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[703], jobCode=0):
            return 시작703()


class 시작703(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1026])
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 진행703()


class 진행703(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='어둠의 샘이 당신의 존재를 눈치챘습니다.\n생명을 탐하는 검은 화살이 당신을 뒤쫓습니다.', arg3='3000')
        create_monster(spawnIds=[109], arg2=True)
        create_monster(spawnIds=[103,1031,1032,1033,1034], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103,1031,1032,1033,1034]):
            return 마무리1_703()


class 마무리1_703(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8902], visible=False)
        create_monster(spawnIds=[1035], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마무리2_703()


class 마무리2_703(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='수백년간 잠들어 있던 샘이 깨어났어. 샘은 영혼을 원해. 가까이 다가가지 않는게 좋아.')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[704], jobCode=0):
            return 시작704()


class 시작704(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=2, isEnable=False)
        enable_spawn_point_pc(spawnId=3, isEnable=True)
        create_monster(spawnIds=[104,1041,1042,1043,1044], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 진행704()


class 진행704(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='거미... 난 거미가 싫어... 거미는 영혼을 옭아매는 자...')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[104,1041,1042,1043,1044]):
            return 마무리704()


class 마무리704(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8903], visible=False)
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='샘은 거미의 눈을 빌려 모든걸 감시하고 있어. 조심하는게 좋아.')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[705], jobCode=0):
            return 시작705()


class 시작705(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=3, isEnable=False)
        enable_spawn_point_pc(spawnId=4, isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 진행705()


class 진행705(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105,1051,1052,1053,1054], arg2=True)
        side_npc_talk(npcId=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='얼마 안남았어. 조금 더... 조금 더 내려와봐.')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105,1051,1052,1053,1054]):
            return 마무리705()


class 마무리705(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8904], visible=False)
        create_monster(spawnIds=[1036], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[708], jobCode=0):
            return 버프걸어주기()


class 버프걸어주기(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='여기 들어온 순간...')
        set_skill(triggerIds=[9000], isEnable=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[706], jobCode=0):
            return 시작706()


class 시작706(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='어둠을 만나게 되면... 다신 올라올 수 없어.')
        enable_spawn_point_pc(spawnId=4, isEnable=False)
        enable_spawn_point_pc(spawnId=5, isEnable=True)
        create_monster(spawnIds=[106,1061,1063,1064,1065], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106,1061,1063,1064,1065]):
            return 마무리706()


class 마무리706(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8905], visible=False)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='그래 마치 우리처럼...')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[707], jobCode=0):
            return 시작707()


class 시작707(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=5, isEnable=False)
        enable_spawn_point_pc(spawnId=6, isEnable=True)
        create_monster(spawnIds=[108], arg2=True)
        side_npc_talk(npcId=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='캬하하! 여기까지 오다니, 재미있겠는걸. 네 영혼도 여기에 묶어주마.')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[108]):
            return 포털생성전()


class 포털생성전(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[109])
        create_monster(spawnIds=[1091], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 포털생성전2()


class 포털생성전2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[109])
        create_monster(spawnIds=[1091], arg2=True)
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='잠깐, 더 내려 갈거야? 여기서 어디로 갈지 우린 알 수 없어. 여긴 뒤틀린 미지의 공간. 모든 것은 샘의 뜻대로...')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 포털생성()


class 포털생성(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


