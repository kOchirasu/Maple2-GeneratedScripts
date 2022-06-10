using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001959: Fallen Guard
/// </summary>
public class _11001959 : NpcScript {
    internal _11001959(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1201224107007508$ 
                // - Ugh...   
                return true;
            case 20:
                // $script:1201224107007510$ 
                // - They took $npcName:11000526[gender:0]$... 
                return true;
            default:
                return true;
        }
    }
}
