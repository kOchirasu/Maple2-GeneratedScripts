using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004282: Loose Tile
/// </summary>
public class _11004282 : NpcScript {
    internal _11004282(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011296$ 
                // - <font color="#909090">(A distant roar echoes through the air.)</font>
                return true;
            case 10:
                // $script:0911203207011297$ 
                // - <font color="#909090">(A distant roar echoes through the air.)</font>
                // $script:0911203207011298$ 
                // - <font color="#909090">(The tile is loose, but the roar reverberates through your body. Your every instinct tells you to run.)</font>
                // $script:0913151207011309$ 
                // - <font color="#909090">(For a brief moment, you swear you see something moving through the crack in the floor. Surely you imagined it...)</font>
                return true;
            default:
                return true;
        }
    }
}
