using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004214: Frontier Foundation Quartermaster
/// </summary>
public class _11004214 : NpcScript {
    internal _11004214(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806130507010732$ 
                // - Great work out there today! 
                return true;
            case 10:
                // $script:0806130507010733$ 
                // - I've got just what you need to continue the search. 
                return true;
            default:
                return true;
        }
    }
}
