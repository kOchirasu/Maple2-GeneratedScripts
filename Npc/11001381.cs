using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001381: Modir
/// </summary>
public class _11001381 : NpcScript {
    internal _11001381(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217192807005381$ 
                // - Hm? What brings you here?
                return true;
            case 30:
                // $script:1228164407005724$ 
                // - I'm thinking up ways to bring prosperity to $map:02010036$. If you want to chat, talk to someone else.
                return true;
            default:
                return true;
        }
    }
}
