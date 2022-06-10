using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004382: Lydia
/// </summary>
public class _11004382 : NpcScript {
    internal _11004382(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011803$ 
                // - I will find love this winter!
                return true;
            case 10:
                // $script:1109213607011804$ 
                // - I confessed my love to someone during the holidays last year...
                switch (selection) {
                    // $script:1109213607011805$
                    // - What happened?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109213607011806$ 
                // - The very next day, he gave it away. This year, I'll give it to someone special...
                switch (selection) {
                    // $script:1109213607011807$
                    // - Well, happy holidays!
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109213607011808$ 
                // - You listen to me, find your true love before the year ends!
                return true;
            default:
                return true;
        }
    }
}
