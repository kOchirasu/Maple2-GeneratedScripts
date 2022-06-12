using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000012: Bogie
/// </summary>
public class _11000012 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407000062$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000066$
                // - If I keep working like this, exhaustion's going to get me. And what's worse is that $npcName:11000252[gender:0]$ still won't appreciate all my hard work! You know, it's so hard to take care of $map:02000001$ by myself.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
