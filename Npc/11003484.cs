using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003484: Kaitlyn
/// </summary>
public class _11003484 : NpcScript {
    internal _11003484(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008697$ 
                // - ... 
                return true;
            case 10:
                // $script:0721142007008715$ 
                // - ... 
                return true;
            default:
                return true;
        }
    }
}
