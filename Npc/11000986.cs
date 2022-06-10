using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000986: Shapian
/// </summary>
public class _11000986 : NpcScript {
    internal _11000986(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003398$ 
                // - That was the only way to show my gratitude... Sniff... 
                return true;
            case 20:
                // $script:0831180407003400$ 
                // - There are many stones yet unknown to the world. The ones that shine aren't the only beautiful ones. 
                return true;
            default:
                return true;
        }
    }
}
