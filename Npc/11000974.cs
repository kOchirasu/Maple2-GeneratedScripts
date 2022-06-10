using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000974: Mani
/// </summary>
public class _11000974 : NpcScript {
    internal _11000974(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003370$ 
                // - Welcome, and thank you for coming all the way here. 
                return true;
            case 20:
                // $script:0831180407003372$ 
                // - It gives me tremendous pleasure to watch people enjoying my food. Ho, ho! 
                return true;
            default:
                return true;
        }
    }
}
