using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004184: Eupheria
/// </summary>
public class _11004184 : NpcScript {
    internal _11004184(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010630$ 
                // - Do you need something?
                return true;
            case 10:
                // $script:0806025707010631$ 
                // - It's certainly reassuring to have these two at my side, but we have a lot of work ahead of us if we intend to come out on top.
                return true;
            default:
                return true;
        }
    }
}
