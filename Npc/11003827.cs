using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003827: Mason
/// </summary>
public class _11003827 : NpcScript {
    internal _11003827(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0115140307009751$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:0115140307009752$ 
                // - There's work to be done.
                return true;
            default:
                return true;
        }
    }
}
