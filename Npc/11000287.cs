using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000287: Bag
/// </summary>
public class _11000287 : NpcScript {
    internal _11000287(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001127$ 
                // - Check the altar.
                return true;
            case 10:
                // $script:0831180407001128$ 
                // - This altar is covered in layers of dust, the result of ages of neglect.
                return true;
            default:
                return true;
        }
    }
}
