using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004568: Mika
/// </summary>
public class _11004568 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0220211107014560$
    // - Aaaah.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220211107014561$
                // - Hmm hm hummm!
                return 10;
            case (10, 1):
                // $script:0220211107014562$
                // - Huh? Did you say something?
                switch (selection) {
                    // $script:0220211107014563$
                    // - Take off your headphones!
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0220211107014564$
                // - Good idea! There we go. You're here for the Queen Bean Rumble?
                return 20;
            case (20, 1):
                // $script:0220211107014565$
                // - Me too! I bet you didn't know I could fight.
                switch (selection) {
                    // $script:0220211107014566$
                    // - I haven't thought about it.
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0220211107014567$
                // - Well, I can, and I'm really good at it, too.
                return 30;
            case (30, 1):
                // $script:0220211107014568$
                // - In fact, I'm the very first fighter the Pink Beans invited. It wasn't easy for them, either. Karkar isn't exactly in their backyard.
                return 30;
            case (30, 2):
                // $script:0220211107014569$
                // - Anyway, I'll see you in the fight!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
