using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004538: Barricade Defender
/// </summary>
public class _11004538 : NpcScript {
    internal _11004538(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0104170807012616$ 
                // - Zzz zzz...
                return true;
            case 10:
                // $script:0104170807012617$ 
                // - Zzz zzz...
                // $script:0104170807012618$ 
                // - Wha? Huh? I'm defendin'... I'm defendin' the base!
                // $script:0104170807012619$ 
                // - Here I figured I'd spend my last years of my service in the capital, then retire and spend the rest of my days on a little farm out by Evansville. But nooo, they had to ship me out to this light-forsaken place... 
                return true;
            default:
                return true;
        }
    }
}
