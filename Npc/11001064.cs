using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001064: Ruben
/// </summary>
public class _11001064 : NpcScript {
    internal _11001064(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003625$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:0831180407003628$ 
                // - I'd better find a clue as soon as possible...  
                return true;
            default:
                return true;
        }
    }
}
