using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003442: Kaitlyn
/// </summary>
public class _11003442 : NpcScript {
    internal _11003442(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008690$ 
                // - What? 
                return true;
            case 10:
                // $script:0721142007008708$ 
                // - What? 
                return true;
            default:
                return true;
        }
    }
}
