using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000566: Ron
/// </summary>
public class _11000566 : NpcScript {
    internal _11000566(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002342$ 
                // - Go ahead. I'm listening. 
                return true;
            case 20:
                // $script:0831180407002344$ 
                // - Stay out of trouble. You don't want to end up like Dark Wind. 
                return true;
            default:
                return true;
        }
    }
}
