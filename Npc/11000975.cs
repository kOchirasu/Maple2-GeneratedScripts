using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000975: Palmer
/// </summary>
public class _11000975 : NpcScript {
    internal _11000975(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003373$ 
                // - Unngh... Unngh... Unngh...  
                return true;
            case 20:
                // $script:0831180407003375$ 
                // - I believe if I work hard now, I'll be able to retire and spend time with my daughter someday. 
                return true;
            default:
                return true;
        }
    }
}
