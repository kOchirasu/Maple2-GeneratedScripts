using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000366: Janine
/// </summary>
public class _11000366 : NpcScript {
    internal _11000366(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001511$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407001513$ 
                // - Do you know what makes cats so appealing? It's how independent they are! Though... it's possible for them to be too independent. Like $npcName:11000367$, for example.
                return true;
            default:
                return true;
        }
    }
}
