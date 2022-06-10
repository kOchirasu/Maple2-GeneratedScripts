using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000821: Mina
/// </summary>
public class _11000821 : NpcScript {
    internal _11000821(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003017$ 
                // - Sigh... 
                return true;
            case 20:
                // $script:0831180407003019$ 
                // - My skin is still crawling... Can I ever go back home? 
                return true;
            default:
                return true;
        }
    }
}
