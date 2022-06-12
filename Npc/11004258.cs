using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004258: Casto
/// </summary>
public class _11004258 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0829171107010976$
    // - It's soooo hot. And I've made no progress on my research. Ugh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0829171107010977$
                // - It's soooo hot. And I've made no progress on my research. Ugh...
                switch (selection) {
                    // $script:0831140807011028$
                    // - What are you researching?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0831140807011029$
                // - Oh, not much. Just, you know, the dragon that lives here in $map:02000011$.
                switch (selection) {
                    // $script:0831140807011030$
                    // - $npcName:23100011$?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0831140807011031$
                // - Maybe. That's what I'm researching. I personally believe that $npcName:23100011$, the legendary dragon, lives here, but I'm searching for proof. You've heard the legend, right?
                switch (selection) {
                    // $script:0831140807011032$
                    // - Nope! Tell me!
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0831140807011033$
                // - Once upon a time, not too far from here, there was a place called the Forest of Wisdom. One day, the fire dragon turned the place into a sea of flame. It was the greatest loss of life in the history of the world. Supposedly, the dragon slumbers somewhere here in $map:02000011$.
                return 13;
            case (13, 1):
                // $script:0831140807011034$
                // - This area didn't used to be so hot... Not until after the fire dragon went into hiding here.
                return 13;
            case (13, 2):
                // $script:0831140807011035$
                // - That's my theory, at least. Anyway, if you find anything, let me know. I kind of want to go home now.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Next,
            (13, 1) => NpcTalkButton.Next,
            (13, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
