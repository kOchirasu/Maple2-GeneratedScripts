using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004315: Nairin
/// </summary>
public class _11004315 : NpcScript {
    internal _11004315(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0928133807011356$ 
                // - Would you like to take on a mission for Green Hoods?
                return true;
            case 10:
                // $script:0928133807011357$ 
                // - Our survey teams encountered some mechanical trees during their exploration of Kritias. Just hearing about it gives me the creeps. Who would build such a thing?
                return true;
            case 20:
                // $script:0116153807012735$ 
                // - Sorry, but I don't have any missions just yet.
                return true;
            default:
                return true;
        }
    }
}
