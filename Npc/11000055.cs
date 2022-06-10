using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000055: Joseph
/// </summary>
public class _11000055 : NpcScript {
    internal _11000055(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000237$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407000240$ 
                // - $MyPCName$, if you're hungry you should come inside. This is my house right here, and my mom is baking cookies.
                return true;
            default:
                return true;
        }
    }
}
