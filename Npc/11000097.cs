using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000097: Solvay
/// </summary>
public class _11000097 : NpcScript {
    internal _11000097(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000381$ 
                // - What seems to be the problem?
                return true;
            case 20:
                // $script:0831180407000382$ 
                // - The Barrota Trading Company is Maple World's biggest mercantile organization. Its hawkers go everywhere in the world, no matter how steep or dangerous.
                return true;
            default:
                return true;
        }
    }
}
