using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004186: Darphony
/// </summary>
public class _11004186 : NpcScript {
    internal _11004186(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010634$ 
                // - Ah... N-nice to meet you... 
                return true;
            case 10:
                // $script:0806025707010635$ 
                // - I came here to get t-t-tougher, so I can chase off the w-wolves plaguing our farm.
                return true;
            default:
                return true;
        }
    }
}
