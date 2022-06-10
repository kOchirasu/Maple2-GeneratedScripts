using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001029: Elmin
/// </summary>
public class _11001029 : NpcScript {
    internal _11001029(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003519$ 
                // - Aaahh... No...
                return true;
            case 30:
                // $script:0831180407003522$ 
                // - I was in $map:02000309$ looking for Director $npcName:11000843[gender:0]$, when $npcName:24000615$ captured me and dragged me all the way here. 
                return true;
            case 40:
                // $script:0831180407003523$ 
                // - There's no time to chat! We have to shut down the Chronometric Computer before our timeline collapses in a temporal cascade.
                // $script:0831180407003524$ 
                // - If that happens, there'll be no saving $npcName:11000057[gender:1]$.
                return true;
            default:
                return true;
        }
    }
}
