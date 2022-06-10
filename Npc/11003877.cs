using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003877: Loana
/// </summary>
public class _11003877 : NpcScript {
    internal _11003877(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009870$ 
                // - The waves are calm today! It's a nice day to go sailing.
                return true;
            case 10:
                // $script:0417135107009871$ 
                // - The waves are calm today! It's a nice day to go sailing.
                return true;
            default:
                return true;
        }
    }
}
