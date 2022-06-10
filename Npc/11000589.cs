using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000589: Dioni
/// </summary>
public class _11000589 : NpcScript {
    internal _11000589(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000847$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000848$ 
                // - $map:02000023$-style buildings are really cool on the inside.
                return true;
            default:
                return true;
        }
    }
}
