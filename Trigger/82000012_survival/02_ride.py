""" trigger/82000012_survival/02_ride.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7100,7200,7300,7400,7500,7600,7700,7800], visible=False) # MushBalloon Regen Sound
        set_effect(triggerIds=[5100,5200,5300,5400,5500,5600,5700,5800], visible=False) # MushBalloon Rise Sound
        set_effect(triggerIds=[6100,6200,6300,6400,6500,6600,6700,6800], visible=False) # MushBalloon Disappear Sound
        set_user_value(key='SetRide', value=0)
        set_user_value(key='StartPatrol', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='SetRide', value=1):
            return Ride01_Ready()
        if user_value(key='SetRide', value=2):
            return Ride02_Ready()
        if user_value(key='SetRide', value=3):
            return Ride03_Ready()
        if user_value(key='SetRide', value=4):
            return Ride04_Ready()
        if user_value(key='SetRide', value=5):
            return Ride05_Ready()
        if user_value(key='SetRide', value=6):
            return Ride06_Ready()
        if user_value(key='SetRide', value=7):
            return Ride07_Ready()
        if user_value(key='SetRide', value=8):
            return Ride08_Ready()


#  North_To_South 
class Ride01_Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7100], visible=True) # MushBalloon Regen Sound
        create_monster(spawnIds=[110], arg2=False) # North_To_South
        write_log(logName='Survival', arg3='bus_01') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride01_StartPatrolDelay()


class Ride01_StartPatrolDelay(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5100], visible=True) # MushBalloon Rise Sound
        move_npc(spawnId=110, patrolName='MS2PatrolData_111')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Ride01_StartPatrol()


class Ride01_StartPatrol(state.State):
    def on_enter(self):
        add_buff(boxIds=[110], skillId=70001081, level=1, arg4=True, arg5=False) # MushBalloon Flying Loop Sound
        move_npc(spawnId=110, patrolName='MS2PatrolData_110') # North_To_South

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=32000):
            return Quit()

    def on_exit(self):
        destroy_monster(spawnIds=[110])
        set_effect(triggerIds=[6100], visible=True) # MushBalloon Disappear Sound


#  South_To_North 
class Ride02_Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7200], visible=True) # MushBalloon Regen Sound
        create_monster(spawnIds=[120], arg2=False) # South_To_North
        write_log(logName='Survival', arg3='bus_02') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride02_StartPatrolDelay()


class Ride02_StartPatrolDelay(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5200], visible=True) # MushBalloon Rise Sound
        move_npc(spawnId=120, patrolName='MS2PatrolData_121')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Ride02_StartPatrol()


class Ride02_StartPatrol(state.State):
    def on_enter(self):
        add_buff(boxIds=[120], skillId=70001081, level=1, arg4=True, arg5=False) # MushBalloon Flying Loop Sound
        move_npc(spawnId=120, patrolName='MS2PatrolData_120') # South_To_North

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=32000):
            return Quit()

    def on_exit(self):
        destroy_monster(spawnIds=[120])
        set_effect(triggerIds=[6200], visible=True) # MushBalloon Disappear Sound


#  East_To_West 
class Ride03_Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7300], visible=True) # MushBalloon Regen Sound
        create_monster(spawnIds=[130], arg2=False) # East_To_West
        write_log(logName='Survival', arg3='bus_03') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride03_StartPatrolDelay()


class Ride03_StartPatrolDelay(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5300], visible=True) # MushBalloon Rise Sound
        move_npc(spawnId=130, patrolName='MS2PatrolData_131')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Ride03_StartPatrol()


class Ride03_StartPatrol(state.State):
    def on_enter(self):
        add_buff(boxIds=[130], skillId=70001081, level=1, arg4=True, arg5=False) # MushBalloon Flying Loop Sound
        move_npc(spawnId=130, patrolName='MS2PatrolData_130') # East_To_West

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=32000):
            return Quit()

    def on_exit(self):
        destroy_monster(spawnIds=[130])
        set_effect(triggerIds=[6300], visible=True) # MushBalloon Disappear Sound


#  West_To_East 
class Ride04_Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7400], visible=True) # MushBalloon Regen Sound
        create_monster(spawnIds=[140], arg2=False) # West_To_East
        write_log(logName='Survival', arg3='bus_04') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride04_StartPatrolDelay()


class Ride04_StartPatrolDelay(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5400], visible=True) # MushBalloon Rise Sound
        move_npc(spawnId=140, patrolName='MS2PatrolData_141')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Ride04_StartPatrol()


class Ride04_StartPatrol(state.State):
    def on_enter(self):
        add_buff(boxIds=[140], skillId=70001081, level=1, arg4=True, arg5=False) # MushBalloon Flying Loop Sound
        move_npc(spawnId=140, patrolName='MS2PatrolData_140') # North_To_South

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=32000):
            return Quit()

    def on_exit(self):
        destroy_monster(spawnIds=[140])
        set_effect(triggerIds=[6400], visible=True) # MushBalloon Disappear Sound


#  West_To_East 
class Ride05_Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7500], visible=True) # MushBalloon Regen Sound
        create_monster(spawnIds=[150], arg2=False) # NorthWest_To_SouthEast
        write_log(logName='Survival', arg3='bus_05') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride05_StartPatrolDelay()


class Ride05_StartPatrolDelay(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5500], visible=True) # MushBalloon Rise Sound
        move_npc(spawnId=150, patrolName='MS2PatrolData_151')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Ride05_StartPatrol()


class Ride05_StartPatrol(state.State):
    def on_enter(self):
        add_buff(boxIds=[150], skillId=70001081, level=1, arg4=True, arg5=False) # MushBalloon Flying Loop Sound
        move_npc(spawnId=150, patrolName='MS2PatrolData_150') # NorthWest_To_SouthEast

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=32000):
            return Quit()

    def on_exit(self):
        destroy_monster(spawnIds=[150])
        set_effect(triggerIds=[6500], visible=True) # MushBalloon Disappear Sound


#  NorthEast_To_SouthWest 
class Ride06_Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7600], visible=True) # MushBalloon Regen Sound
        create_monster(spawnIds=[160], arg2=False) # NorthEast_To_SouthWest
        write_log(logName='Survival', arg3='bus_06') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride06_StartPatrolDelay()


class Ride06_StartPatrolDelay(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5600], visible=True) # MushBalloon Rise Sound
        move_npc(spawnId=160, patrolName='MS2PatrolData_161')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Ride06_StartPatrol()


class Ride06_StartPatrol(state.State):
    def on_enter(self):
        add_buff(boxIds=[160], skillId=70001081, level=1, arg4=True, arg5=False) # MushBalloon Flying Loop Sound
        move_npc(spawnId=160, patrolName='MS2PatrolData_160') # NorthEast_To_SouthWest

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=32000):
            return Quit()

    def on_exit(self):
        destroy_monster(spawnIds=[160])
        set_effect(triggerIds=[6600], visible=True) # MushBalloon Disappear Sound


#  SouthWest_To_NorthEast 
class Ride07_Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7700], visible=True) # MushBalloon Regen Sound
        create_monster(spawnIds=[170], arg2=False) # SouthWest_To_NorthEast
        write_log(logName='Survival', arg3='bus_07') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride07_StartPatrolDelay()


class Ride07_StartPatrolDelay(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5700], visible=True) # MushBalloon Rise Sound
        move_npc(spawnId=170, patrolName='MS2PatrolData_171')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Ride07_StartPatrol()


class Ride07_StartPatrol(state.State):
    def on_enter(self):
        add_buff(boxIds=[170], skillId=70001081, level=1, arg4=True, arg5=False) # MushBalloon Flying Loop Sound
        move_npc(spawnId=170, patrolName='MS2PatrolData_170') # SouthWest_To_NorthEast

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=32000):
            return Quit()

    def on_exit(self):
        destroy_monster(spawnIds=[170])
        set_effect(triggerIds=[6700], visible=True) # MushBalloon Disappear Sound


#  SouthEast_To_NorthWest 
class Ride08_Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7800], visible=True) # MushBalloon Regen Sound
        create_monster(spawnIds=[180], arg2=False) # SouthEast_To_NorthWest
        write_log(logName='Survival', arg3='bus_08') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride08_StartPatrolDelay()


class Ride08_StartPatrolDelay(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5800], visible=True) # MushBalloon Rise Sound
        move_npc(spawnId=180, patrolName='MS2PatrolData_181')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Ride08_StartPatrol()


class Ride08_StartPatrol(state.State):
    def on_enter(self):
        add_buff(boxIds=[180], skillId=70001081, level=1, arg4=True, arg5=False) # MushBalloon Flying Loop Sound
        move_npc(spawnId=180, patrolName='MS2PatrolData_180') # SouthEast_To_NorthWest

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=32000):
            return Quit()

    def on_exit(self):
        destroy_monster(spawnIds=[180])
        set_effect(triggerIds=[6800], visible=True) # MushBalloon Disappear Sound


class Quit(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='bus_end') # 서바이벌 버스 로그


