using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003199: Joddy
/// </summary>
public class _11003199 : NpcScript {
    internal _11003199(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008226$ 
                // - A fight between siblings can be even more fearsome than a duel between sworn enemies. I wouldn't stand a chance if $npcName:11000069[gender:1]$ were my sister.
                return true;
            case 10:
                // $script:0404083307008227$ 
                // - A fight between siblings can be even more fearsome than a duel between sworn enemies. I wouldn't stand a chance if $npcName:11000069[gender:1]$ were my sister.
                return true;
            default:
                return true;
        }
    }
}
