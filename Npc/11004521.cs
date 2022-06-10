using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004521: Mayu
/// </summary>
public class _11004521 : NpcScript {
    internal _11004521(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0102174210002228$ 
                // - If you need a lift back to $map:02000001$, I'm your gal!
                return true;
            case 10:
                // $script:0102174210002229$ 
                // - If you need a lift back to $map:02000001$, I'm your gal!
                // $script:0102174210002230$ 
                // - We're heading out straight away. If you miss this place, you can always use the <i>Lumiwind</i> to come back. Are you ready to return to $map:02000001$?
                switch (selection) {
                    // $script:0102174210002231$
                    // - Take me to $map:02000001$!
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0102174210002232$ functionID=1 
                // - All right. Away we go!
                return true;
            default:
                return true;
        }
    }
}
