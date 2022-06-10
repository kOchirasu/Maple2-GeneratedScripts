using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004441: 
/// </summary>
public class _11004441 : NpcScript {
    internal _11004441(INpcScriptContext context) : base(context) {
        Id = 90;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1221144207012027$ 
                // - How may I help you?
                return true;
            case 21:
                // $script:1221144207012054$ functionID=1 
                // - Absolutely! Hand it over, and I'll take a look at your $item:30001025$! Since you're paying, you can rest assured that the key will be useful.
                return true;
            case 22:
                // $script:1221144207012055$ functionID=1 
                // - Sure! I provide 10 free analyses per day, out of the goodness of my heart. Even if the key is too old to be useful, you'll still get a little something.
                return true;
            case 60:
                // $script:1221144207012042$ 
                // - I get excited thinking about the story behind all these old objects.
                return true;
            case 90:
                // $script:1221144207012051$ 
                // - How can I help you?
                switch (selection) {
                    // $script:1221144207012052$
                    // - Analyze my $item:30001025$, please.
                    case 0:
                        Id = 21;
                        return false;
                    // $script:1221144207012053$
                    // - There's something I need to tell you.
                    case 1:
                        Id = 0; // TODO: 20,30,40,50,60 | 
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
