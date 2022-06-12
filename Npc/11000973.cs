using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000973: Hamantha
/// </summary>
public class _11000973 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003367$
    // - Oh, no. You aren't getting my digits. Now shoo!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003369$
                // - Sniff... Name's $npcName:11000973[gender:1]$, and I'm the prettiest little thing you're going to find in $map:02000186$.
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
