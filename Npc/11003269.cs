using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003269: Ellie
/// </summary>
public class _11003269 : NpcScript {
    internal _11003269(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008220$ 
                // - What's wrong?
                return true;
            case 30:
                // $script:0403155707008221$ 
                // - Platoon leader of the Green Hoods, at your service. $npcName:11000015[gender:1]$ sent me here to watch over $map:02000146$.
                return true;
            default:
                return true;
        }
    }
}
