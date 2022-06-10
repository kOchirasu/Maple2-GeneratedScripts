using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004462: Safehold Guardsman
/// </summary>
public class _11004462 : NpcScript {
    internal _11004462(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012077$ 
                // - All clear!
                return true;
            case 10:
                // $script:1227192907012078$ 
                // - All clear!
                // $script:1227192907012079$ 
                // - We're doing our best to keep $map:02020041$ safe!
                return true;
            default:
                return true;
        }
    }
}
