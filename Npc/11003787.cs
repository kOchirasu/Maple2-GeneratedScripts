using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003787: Schatten
/// </summary>
public class _11003787 : NpcScript {
    internal _11003787(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213192607009644$ 
                // - I am the shadow that evil fears. 
                return true;
            case 10:
                // $script:1213192607009645$ 
                // - What can <i>I</i> do for <i>you</i>? 
                return true;
            default:
                return true;
        }
    }
}
