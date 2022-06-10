using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001059: Danak
/// </summary>
public class _11001059 : NpcScript {
    internal _11001059(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003617$ 
                // - Gasp! Did my wife send you?
                return true;
            case 30:
                // $script:0831180407003620$ 
                // - No one understands the burning passion of this lonely man... Sigh... 
                return true;
            default:
                return true;
        }
    }
}
