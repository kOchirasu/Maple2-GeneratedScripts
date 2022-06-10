using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000293: Ellbo
/// </summary>
public class _11000293 : NpcScript {
    internal _11000293(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001167$ 
                // - What brings you to me?
                return true;
            case 30:
                // $script:0831180407001170$ 
                // - Want to know how I keep my fur so shiny?
                return true;
            default:
                return true;
        }
    }
}
