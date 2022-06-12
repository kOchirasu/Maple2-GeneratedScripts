using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000843: Mett
/// </summary>
public class _11000843 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407003084$
    // - Oh, no... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003087$
                // - This is beyond bad! $npcName:22400062$ is trying to manipulate the timeline to his own ends! If he succeeds, the resulting temporal cascade will wipe away all of history as we know it!
                return -1;
            case (40, 0):
                // $script:0831180407003088$
                // - This place exists upon the central axis of time for our universe. It is a road to all things. Here all possible timelines coexist simultaneously. $npcName:22400062$ plans to collapse them all into a single eventuality, one where he reigns supreme!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
