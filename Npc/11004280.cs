using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004280: Pillar of Light
/// </summary>
public class _11004280 : NpcScript {
    internal _11004280(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011291$ 
                // - <font color="#909090">(A bright light shines through a crack in the wall.)</font>
                return true;
            case 10:
                // $script:0911203207011292$ 
                // - <font color="#909090">(A bright light shines through a crack in the wall.)</font>
                // $script:0911203207011293$ 
                // - <font color="#909090">(This passageway was blocked off long ago, but something on the other side still shines brilliantly.)</font>
                // $script:0913151207011306$ 
                // - <font color="#909090">(You can sense a different sort of power beyond the crack in the wall.)</font>
                return true;
            default:
                return true;
        }
    }
}
