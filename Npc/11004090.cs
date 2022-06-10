using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004090: Everfrost Star
/// </summary>
public class _11004090 : NpcScript {
    internal _11004090(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622133907010321$ 
                // - <font color='#909090'>(This giant snowflake reflects the brilliant sun. No matter how brightly it shines, it never seems to melt.)</font>
                return true;
            case 10:
                // $script:0622133907010322$ 
                // - <font color='#909090'>(This giant snowflake reflects the brilliant sun. No matter how brightly it shines, it never seems to melt.)</font>
                // $script:0622133907010323$ 
                // - <font color='#909090'>(Tourists come from all over the world to see the local "Santa" who makes presents for good boys and girls. Taking your picture in front of the snow crystal is a trendy thing to do.)</font>
                // $script:0622133907010324$ 
                // - <font color='#909090'>(They say that the snow crystal is a reflection of the goodness and kindness that lives in the hearts of Santas everywhere.)</font>
                return true;
            default:
                return true;
        }
    }
}
