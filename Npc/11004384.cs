using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004384: Boris
/// </summary>
public class _11004384 : NpcScript {
    internal _11004384(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011815$ 
                // - The kids sure do love the holidays...
                return true;
            case 10:
                // $script:1109213607011816$ 
                // - The kids really love the holidays...
                switch (selection) {
                    // $script:1109213607011817$
                    // - Not just kids though. Adults love the holidays, too, don't they?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109213607011818$ 
                // - Ehh, it depends. Easier for adults to lose the spirit of the season, I think.
                switch (selection) {
                    // $script:1109213607011819$
                    // - Well, happy holidays!
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109213607011820$ 
                // - Agreed! Happy holidays! Remind everyone that this is a season for joy!
                return true;
            default:
                return true;
        }
    }
}
