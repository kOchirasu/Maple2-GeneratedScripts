using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001181: Godar
/// </summary>
public class _11001181 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:1014150507004129$
    // - Ah, I should update my travel journal!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1014150507004132$
                // - Ah, a local! <font color="#ffd200">Yalario!</font> It always been my dream to explore strange new worlds, and seek out new life and new civilizations! Traveling this land has been an awesome experience.
                return 30;
            case (30, 1):
                // $script:1014150507004133$
                // - ...Ah, but I'm sure these sights seem so plain to you. Well, I hope I'll get to keep visiting new places and writing about them in my travel journal.
                switch (selection) {
                    // $script:1014150507004134$
                    // - Yala-what-io?
                    case 0:
                        return 31;
                    // $script:1014150507004135$
                    // - I take it you like to travel?
                    case 1:
                        return 32;
                    // $script:1014150507004136$
                    // - Where exactly are you from?
                    case 2:
                        return 33;
                }
                return -1;
            case (31, 0):
                // $script:1014150507004137$
                // - New friend! This is how we greet strangers who we want to be our friends. $npcName:11001179[gender:0]$ shouted it out when we first arrived in $map:02000064$, so I guess it can also be used for villages. Well, at least it can be by our captain.
                return -1;
            case (32, 0):
                // $script:1014150507004138$
                // - Of course! Setting foot in a new land, leaving proof of your journey... There's nothing more exciting! I bet everyone in the <b>Allicari Merchant Society</b> would agree.
                return -1;
            case (33, 0):
                // $script:1014150507004139$
                // - I'm from a place far, far away! On the other side of the sea. To get there from here you have to go north... no wait, south... Err, east? We sort of stumbled upon this land by accident. My homeland is beautiful, although it's much different than here.
                return -1;
            case (40, 0):
                // $script:1026143107004294$
                // - Ah, yalario! What can I do for you?
                switch (selection) {
                    // $script:1026143107004295$
                    // - I'm looking for some $item:30000421$.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1026143107004296$
                // - Ah, those. The smuggler called $npcName:11001212[gender:0]$ sells them, but I wouldn't do business with him if I were you.
                switch (selection) {
                    // $script:1026143107004297$
                    // - Why do you say that?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1026143107004298$
                // - He snuck onto our vessel because he did not want to pay a simple fare. No one who does such a thing could be considered trustworthy.
                switch (selection) {
                    // $script:1026143107004299$
                    // - Where can I find $npcName:11001212[gender:0]$ now?
                    case 0:
                        return 43;
                }
                return -1;
            case (43, 0):
                // $script:1026143107004300$
                // - Captain $npcName:11001179[gender:0]$ kicked him off the ship. Last I saw, he was running off toward $map:03000014$.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
