using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004551: Office Guard
/// </summary>
public class _11004551 : NpcScript {
    internal _11004551(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0109163907012668$ 
                // - You! Outlander! You better not be here to bother $npcName:11004401[gender:1]$.
                return true;
            case 10:
                // $script:0109163907012669$ 
                // - You! Outlander! You better not be here to bother $npcName:11004401[gender:1]$.
                return true;
            default:
                return true;
        }
    }
}
