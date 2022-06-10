using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000443: Cathy Mart Employee
/// </summary>
public class _11000443 : NpcScript {
    internal _11000443(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001863$ 
                // - Can I help you? 
                return true;
            case 20:
                // $script:0831180407001865$ 
                // - If we don't get that money back, it's coming out of <i>my</i> paycheck... 
                return true;
            case 30:
                // $script:0831180407001866$ 
                // - I don't know who's worse, the boss or the robbers. 
                return true;
            default:
                return true;
        }
    }
}
