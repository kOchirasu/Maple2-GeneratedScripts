using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001611: Ishura
/// </summary>
public class _11001611 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0509213707006098$
    // - <font color="#909090">(He's sound asleep.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0511194807006105$
                // - I miss the master. I still hear his voice in my head...
                return -1;
            case (20, 0):
                // $script:0515180407006106$
                // - $npcName:11001229[gender:0]$... Will he ever wake up?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
