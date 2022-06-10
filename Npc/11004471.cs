using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004471: Crypto
/// </summary>
public class _11004471 : NpcScript {
    internal _11004471(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012127$ 
                // - That snot-nosed brat went out to play and still hasn't come back.
                return true;
            case 10:
                // $script:1228153007012427$ 
                // - That snot-nosed brat went out to play and still hasn't come back.
                // $script:1227192907012128$ 
                // - This is no time to play. There's a war going on out there! Ugh, what would our parents say?
                return true;
            default:
                return true;
        }
    }
}
