using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001123: Gerome
/// </summary>
public class _11001123 : NpcScript {
    internal _11001123(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0910171307003837$ 
                // - What seems to be the problem? 
                return true;
            case 30:
                // $script:0915135007003943$ 
                // - The scientists in $map:2000270$ are known for their constant innovation. They're the reason I lug these heavy, expensive components everywhere I go. 
                return true;
            default:
                return true;
        }
    }
}
