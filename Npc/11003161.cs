using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003161: Troy
/// </summary>
public class _11003161 : NpcScript {
    internal _11003161(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0306155707008067$ 
                // - Can I help you?
                return true;
            case 20:
                // $script:0306155707008069$ 
                // - If you love flowers so much, then go pick them yourself. These aren't for you.
                return true;
            default:
                return true;
        }
    }
}
