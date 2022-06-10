using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004136: Eupheria
/// </summary>
public class _11004136 : NpcScript {
    internal _11004136(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0730132107010537$ 
                // - Your aura is one of virtue.
                return true;
            case 10:
                // $script:0730132107010538$ 
                // - All that lifeforce... will you give it to me?
                return true;
            default:
                return true;
        }
    }
}
