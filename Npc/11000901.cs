using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000901: Bunny Gal
/// </summary>
public class _11000901 : NpcScript {
    internal _11000901(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003700$ 
                // - Welcome, $MyPCName$!
                return true;
            case 50:
                // $script:0908154107003705$ 
                // - You're amazing!
                return true;
            case 60:
                // $script:0908154107003706$ 
                // - You did it! Good job!
                return true;
            default:
                return true;
        }
    }
}
