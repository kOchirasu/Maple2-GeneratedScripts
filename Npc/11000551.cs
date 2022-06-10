using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000551: Delta
/// </summary>
public class _11000551 : NpcScript {
    internal _11000551(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002333$ 
                // - Ugh... Is anyone there? 
                return true;
            case 30:
                // $script:0831180407002336$ 
                // - My fellow scouts have been scattered... we're on the brink... 
                return true;
            default:
                return true;
        }
    }
}
