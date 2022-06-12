using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003637: Esther
/// </summary>
public class _11003637 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009072$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009073$
                // - ...
                switch (selection) {
                    // $script:1109121007009074$
                    // - That agent's got to be around here somewhere...
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009075$
                // - Hmph. Where does the she get off, sending me a novice like you?
                switch (selection) {
                    // $script:1109121007009076$
                    // - Guh-whaaaah?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009077$
                // - If you can't recognize one of your fellow agents in disguise, then you really are hopeless.
                switch (selection) {
                    // $script:1109121007009078$
                    // - But... you're a chess piece...
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009079$
                // - I have nothing more to say to you, dullard. Go back to $npcName:11003535[gender:1]$ and tell her that you've failed.
                switch (selection) {
                    // $script:1109121007009080$
                    // - I can't go back empty-handed!
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009081$
                // - No need to shout! I'll give you one more chance—let's call it a test. If you're really a bonafide agent, then you surely know where $map:02000153$ is.
                switch (selection) {
                    // $script:1109121007009082$
                    // - It's in $map:02000001$, the heart of the empire!
                    case 0:
                        return 15;
                    // $script:1109121007009083$
                    // - $map:02000100$, of course.
                    case 1:
                        return 16;
                    // $script:1109121007009084$
                    // - Dark Wind isn't a place. It's a feeling you carry in your heart.
                    case 2:
                        return 17;
                }
                return -1;
            case (15, 0):
                // $script:1109121007009085$
                // - Wrong. Begone, dullard.
                switch (selection) {
                    // $script:1109121007009086$
                    // - Give me another chance!
                    case 0:
                        return 18;
                }
                return -1;
            case (16, 0):
                // $script:1109121007009087$
                // - I suppose you aren't a <i>complete</i> fool. Very well. The message is "Apple, snake, dinosaur."
                switch (selection) {
                    // $script:1109121007009088$
                    // - Is that it?
                    case 0:
                        return 19;
                }
                return -1;
            case (17, 0):
                // $script:1109121007009089$
                // - What nonsense!
                switch (selection) {
                    // $script:1109121007009090$
                    // - Give me another chance!
                    case 0:
                        return 18;
                }
                return -1;
            case (18, 0):
                // $script:1109121007009091$
                // - Where is $map:02000153$?
                switch (selection) {
                    // $script:1109121007009092$
                    // - It's in $map:02000001$, the heart of the empire!
                    case 0:
                        return 15;
                    // $script:1109121007009093$
                    // - $map:02000100$, of course.
                    case 1:
                        return 16;
                    // $script:1127144607009321$
                    // - Dark Wind isn't a place. It's a feeling you carry in your heart.
                    case 2:
                        return 17;
                }
                return -1;
            case (19, 0):
                // $script:1109121007009094$
                // - ...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.SelectableDistractor,
            (15, 0) => NpcTalkButton.SelectableDistractor,
            (16, 0) => NpcTalkButton.SelectableDistractor,
            (17, 0) => NpcTalkButton.SelectableDistractor,
            (18, 0) => NpcTalkButton.SelectableDistractor,
            (19, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
