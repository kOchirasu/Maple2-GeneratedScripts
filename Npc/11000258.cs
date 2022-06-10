using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000258: Hoon
/// </summary>
public class _11000258 : NpcScript {
    internal _11000258(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001067$ 
                // - What seems to be the problem?
                return true;
            case 10:
                // $script:0831180407001068$ 
                // - Please keep your voice down. I'm not supposed to be talking with anyone right now.
                return true;
            default:
                return true;
        }
    }
}
