using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001029: Elmin
/// </summary>
public class _11001029 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407003519$
    // - Aaahh... No...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003522$
                // - I was in $map:02000309$ looking for Director $npcName:11000843[gender:0]$, when $npcName:24000615$ captured me and dragged me all the way here. 
                return -1;
            case (40, 0):
                // $script:0831180407003523$
                // - There's no time to chat! We have to shut down the Chronometric Computer before our timeline collapses in a temporal cascade.
                return 40;
            case (40, 1):
                // $script:0831180407003524$
                // - If that happens, there'll be no saving $npcName:11000057[gender:1]$.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
