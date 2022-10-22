""" trigger/52010056_qd/eventsection_d.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Ready()


class Ready(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=2005, spawnIds=[999]):
            return 연출준비()


class 연출준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera_path(pathIds=[4006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 경비병_외침()


class 경비병_외침(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=999, sequenceName='Attack_01_B')
        add_cinematic_talk(npcId=11003816, msg='$52010056_QD__EventSection_D__0$', duration=3727)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3727):
            return 크림슨스피어_출동()

    def on_exit(self):
        create_monster(spawnIds=[901], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[902], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[903], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[904], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[905], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[906], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[907], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[908], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[909], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[910], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[911], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[912], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[913], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[914], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[915], arg2=True) # 크림슨 스피어: 29000386
        change_monster(removeSpawnId=999, addSpawnId=901)


class 크림슨스피어_출동(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        remove_buff(boxId=2001, skillId=70000107)


