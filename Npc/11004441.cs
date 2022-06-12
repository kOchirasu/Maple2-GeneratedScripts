using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004441: 
/// </summary>
public class _11004441 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (90, NpcTalkButton.SelectableDistractor);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:1221144207012027$ 
                // - How may I help you?
                return default;
            case 21:
                // $script:1221144207012054$ functionID=1 
                // - Absolutely! Hand it over, and I'll take a look at your $item:30001025$! Since you're paying, you can rest assured that the key will be useful.
                return default;
            case 22:
                // $script:1221144207012055$ functionID=1 
                // - Sure! I provide 10 free analyses per day, out of the goodness of my heart. Even if the key is too old to be useful, you'll still get a little something.
                return default;
            case 60:
                // $script:1221144207012042$ 
                // - I get excited thinking about the story behind all these old objects.
                return default;
            case 90:
                // $script:1221144207012051$ 
                // - How can I help you?
                switch (selection) {
                    // $script:1221144207012052$
                    // - Analyze my $item:30001025$, please.
                    case 0:
                        return (21, NpcTalkButton.Close);
                    // $script:1221144207012053$
                    // - There's something I need to tell you.
                    case 1:
                        // TODO: goto 20,30,40,50,60
                        // (Id, Button) = (20, NpcTalkButton.None);
                        // (Id, Button) = (30, NpcTalkButton.None);
                        // (Id, Button) = (40, NpcTalkButton.None);
                        // (Id, Button) = (50, NpcTalkButton.None);
                        // (Id, Button) = (60, NpcTalkButton.Close);
                        // TODO: gotoFail 
                        return (0, NpcTalkButton.None);
                }
                return default;
        }
        
        return default;
    }
}
