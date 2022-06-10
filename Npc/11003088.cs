using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003088: Orde
/// </summary>
public class _11003088 : NpcScript {
    internal _11003088(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0207122607007930$ 
                // - Who would have thought places like this would still exist in Maple World?
                return true;
            case 10:
                // $script:0207122607007931$ 
                // - I'd love to jump into that hot spring... just not when you're watching me, $MyPCName$.
                return true;
            default:
                return true;
        }
    }
}
