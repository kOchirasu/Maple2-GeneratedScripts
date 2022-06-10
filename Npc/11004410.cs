using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004410: Schatten
/// </summary>
public class _11004410 : NpcScript {
    internal _11004410(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011837$ 
                // - I am the shadow that evil fears.
                return true;
            case 10:
                // $script:1113161307011838$ 
                // - I get the feeling things are gonna get worse before they get better.
                return true;
            default:
                return true;
        }
    }
}
