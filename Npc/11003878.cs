using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003878: Mani
/// </summary>
public class _11003878 : NpcScript {
    internal _11003878(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009872$ 
                // - Welcome to $map:02000425$, the beautiful island of alchemy.
                return true;
            case 10:
                // $script:0417135107009873$ 
                // - Welcome to $map:02000425$, the beautiful island of alchemy.
                return true;
            case 20:
                // $script:0419172107009857$ 
                // - Welcome to $map:02000425$, the beautiful island of alchemy.
                return true;
            default:
                return true;
        }
    }
}
