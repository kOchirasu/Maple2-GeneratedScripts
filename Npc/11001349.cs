using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001349: Zobek
/// </summary>
public class _11001349 : NpcScript {
    internal _11001349(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005309$ 
                // - What can I do for you?
                return true;
            case 30:
                // $script:1217012607005312$ 
                // - Why would Mademoiselle Rue want to go into business with Cathy Catalina? They're polar opposites of each other. There's no way this partnership will last!
                return true;
            default:
                return true;
        }
    }
}
