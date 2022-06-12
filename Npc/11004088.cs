using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004088: Rainsong Fairy
/// </summary>
public class _11004088 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0622133907010301$
    // - A cold and rainy day, like when we met.
    //   His eyes, his love, I never will forget...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0622133907010302$
                // - A cold and rainy day, like when we met.
                //   His eyes, his love, I never will forget...
                return 10;
            case (10, 1):
                // $script:0622133907010303$
                // - I see a wand'rer, hail! Be welcome here.
                //   This is Ellosylva, the Fairy's Tear.
                switch (selection) {
                    // $script:0622133907010304$
                    // - That's a sad name.
                    case 0:
                        return 31;
                }
                return 10;
            case (10, 2):
                // $script:0625134307010363$
                // - Once a fairy falls in love, she never forgets her lover, even after they've gone to the place where we cannot follow...
                return 10;
            case (10, 3):
                // $script:0625134307010364$
                // - I broke the rules and fell in love. I first met him here in $map:02000042$. It still smells like him...
                return 10;
            case (10, 4):
                // $script:0625134307010365$
                // - We were happy together, but it couldn't last. And now, I can never see him again...
                return 10;
            case (10, 5):
                // $script:0622133907010309$
                // - He told me that my song made him think of the rain. That is why I sing here—to remember him. But, no matter how cheerfully I try to sing, it always comes out sad...
                switch (selection) {
                    // $script:0625134307010366$
                    // - It's a beautiful song.
                    case 0:
                        return 37;
                }
                return -1;
            case (31, 0):
                // $script:0622133907010305$
                // - We fairies oft wear smiles bright and hale,
                //   but in this rain, I share my pain, my tale.
                switch (selection) {
                    // $script:0622133907010306$
                    // - What's your story?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0622133907010308$
                // - A human's heart I held in hand, and mine
                //   in his. But human lives are short and I
                //   was left behind when it came to be his time.
                return -1;
            case (37, 0):
                // $script:0625134307010367$
                // - Thank you, traveler. I like to think that he's out there, somewhere, still listening to me. Come see me again whenever you want to hear me sing.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Next,
            (10, 4) => NpcTalkButton.Next,
            (10, 5) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            (37, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
