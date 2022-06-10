using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000489: Hani
/// </summary>
public class _11000489 : NpcScript {
    internal _11000489(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002142$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:0831180407002145$ 
                // - He's so hot, and his voice is amaaazing. When I hear him sing, I can hardly control myself! 
                return true;
            default:
                return true;
        }
    }
}
