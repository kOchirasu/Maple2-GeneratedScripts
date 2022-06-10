using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003355: Ralph's Lackey
/// </summary>
public class _11003355 : NpcScript {
    internal _11003355(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0517164307008506$ 
                // - It won't be so easy next time.
                return true;
            case 20:
                // $script:0517164307008508$ 
                // - You better get ready. The big guy'll knock your teeth out!
                return true;
            default:
                return true;
        }
    }
}
