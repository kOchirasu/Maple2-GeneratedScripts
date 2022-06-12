using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000427: Kakomani
/// </summary>
public class _11000427 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001779$
    // - What're you doing here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001781$
                // - Mature $npcName:11000423$s are almost impossible to train. The best time to train them is right after they're born. If only $npcName:23000019[gender:0]$ didn't keep interfering, I could train up a new group of chicks... 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
