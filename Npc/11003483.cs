using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003483: Humblis Agent
/// </summary>
public class _11003483 : NpcScript {
    internal _11003483(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008696$ 
                // - What's wrong?
                return true;
            case 10:
                // $script:0721142007008714$ 
                // - What's wrong?
                return true;
            default:
                return true;
        }
    }
}
