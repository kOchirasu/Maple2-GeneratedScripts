using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001021: Porte
/// </summary>
public class _11001021 : NpcScript {
    internal _11001021(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003468$ 
                // - Did the boss send you?
                return true;
            case 30:
                // $script:0831180407003471$ 
                // - I don't have time for chitchat. I'm on a very important mission right now.
                return true;
            default:
                return true;
        }
    }
}
