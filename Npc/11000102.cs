using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000102: Bunny Gal
/// </summary>
public class _11000102 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407000399$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407000400$
                // - Oh, hello! How do you like $map:02000064$ so far?
                switch (selection) {
                    // $script:0831180407000401$
                    // - What are you doing?
                    case 0:
                        return 51;
                    // $script:0831180407000402$
                    // - What events does the palace sponsor?
                    case 1:
                        return 52;
                    // $script:0831180407000403$
                    // - How can I participate in mini-games?
                    case 2:
                        return 53;
                    // $script:0831180407000404$
                    // - What do I get for winning mini-games?
                    case 3:
                        return 54;
                }
                return -1;
            case (51, 0):
                // $script:0831180407000405$
                // - What am I doing?  Can't you see? I'm dancing for everyone who came to $map:02000064$. Some folks have said I should stop because of the earthquake, but I don't get it.
                return 51;
            case (51, 1):
                // $script:0831180407000406$
                // - Come on, don't be so serious. Don't wallow in disappointment. We should cheer up and stay optimistic. Even $npcName:11000075[gender:1]$ said so!
                return 51;
            case (51, 2):
                // $script:0831180407000407$
                // - And don't push yourself too hard. Sometimes you need to take a break and collect yourself. Maple World has all kinds of fun and exciting events to keep you busy. You can meet new people and win fabulous prizes, too!
                return -1;
            case (52, 0):
                // $script:0831180407000408$
                // - Oh man, I thought everybody knew about those! The palace advertises them everywhere. Okay, well, I can still tell you about it.
                return 52;
            case (52, 1):
                // $script:0831180407000409$
                // - The palace sponsors many events all across Maple World. A decade ago, when Maple World faced one of the greatest challenges in its history, $npcName:11000075[gender:1]$ decided to do something to help distract the people from their worries.
                return 52;
            case (52, 2):
                // $script:0831180407000410$
                // - She said that Maple World needs something to bring people together. Since then, we've held all sorts of games on a regular basis for the benefit of the people.
                return 52;
            case (52, 3):
                // $script:0831180407000411$
                // - Of course, Maple World is still not completely safe. The recent earthquake, for instance... Oops, I shouldn't have mentioned that. A-anyway, these events are important just in how much they help the morale of the populace. 
                return -1;
            case (53, 0):
                // $script:0831180407000412$
                // - Participating in mini-games is easy! $npcName:11001899$ will make an announcement anytime a game goes live. All you have to do is play!
                return 53;
            case (53, 1):
                // $script:0831180407000413$
                // - And even if you're feeling lazy and not up for traveling, there's no need to worry! You can teleport to mini-games from anywhere in the universe! When the Event Notification window appears, just press Enter next to the event you want to join!
                return 53;
            case (53, 2):
                // $script:0831180407000414$
                // - Well, what are you standing around here for? Go play some mini-games!
                return -1;
            case (54, 0):
                // $script:0831180407000415$
                // - Win palace-sponsored events to receive the blessing of $npcName:11000075[gender:1]$. It's a great honor, you know!
                return 54;
            case (54, 1):
                // $script:0831180407000416$
                // - And that's not all! You'll earn mesos, nice skins, and useful potions, too. A lot of people come to this place, dreaming of wealth and fame.
                return 54;
            case (54, 2):
                // $script:0831180407000417$
                // - Oh, right. When you join $map:61000001$ or $map:61000002$ games, keep an eye out for the merchants who sell interesting items! That should make your time in $map:02000064$ even more worthwhile!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Next,
            (51, 1) => NpcTalkButton.Next,
            (51, 2) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.Next,
            (52, 1) => NpcTalkButton.Next,
            (52, 2) => NpcTalkButton.Next,
            (52, 3) => NpcTalkButton.Close,
            (53, 0) => NpcTalkButton.Next,
            (53, 1) => NpcTalkButton.Next,
            (53, 2) => NpcTalkButton.Close,
            (54, 0) => NpcTalkButton.Next,
            (54, 1) => NpcTalkButton.Next,
            (54, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
