using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003437: Anne
/// </summary>
public class _11003437 : NpcScript {
    internal _11003437(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008685$ 
                // - My mind is somewhere else today.
                return true;
            case 10:
                // $script:0721142007008703$ 
                // - The work never ends.
                return true;
            default:
                return true;
        }
    }
}
