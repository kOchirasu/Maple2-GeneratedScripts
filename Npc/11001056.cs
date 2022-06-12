using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001056: Intertimer
/// </summary>
public class _11001056 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180610001152$
    // - This teleportation device is on a test run.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610001153$
                // - Do you want to use this experimental teleportation device?
                //   Destination: $map:02000259$
                //   Cost: 5,000 mesos
                return -1;
            case (10, 0):
                // $script:0831180610001154$
                // - The testing period of this teleportation device has ended.
                return -1;
            case (20, 0):
                // $script:0831180610001155$
                // - You do not have enough money to use this experimental teleportation device. It costs 5,000 mesos to use.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            (1, 0) => NpcTalkButton.TakeBoat,
            _ => NpcTalkButton.None,
        };
    }
}
