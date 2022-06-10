using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003440: Einos
/// </summary>
public class _11003440 : NpcScript {
    internal _11003440(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008688$ 
                // - ...
                return true;
            case 10:
                // $script:0721142007008706$ 
                // - ...
                return true;
            default:
                return true;
        }
    }
}
