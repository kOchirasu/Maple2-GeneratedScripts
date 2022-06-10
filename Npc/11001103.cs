using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001103: Rute
/// </summary>
public class _11001103 : NpcScript {
    internal _11001103(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180306000404$ 
                // - You must be here to see me.
                return true;
            case 40:
                // $script:0809123006000906$ 
                // - The stuff's not ready yet. Come back later.
                return true;
            default:
                return true;
        }
    }
}
