using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003537: Mason
/// </summary>
public class _11003537 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1126150707011943$
    // - It is time my order stood with the rest of the empire.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1126150707011944$
                // - I'm listening.
                switch (selection) {
                    // $script:1126150707011945$
                    // - What are the Lumiknights, exactly?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1126150707011946$
                // - The existence of the Lumiknights may no longer be a secret, but that doesn't mean I may speak freely of what we do. In accordance to the Pact of Dantalion, my tongue is bound.
                switch (selection) {
                    // $script:1126150707011947$
                    // - Your what is huh?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1126150707011948$
                // - Of course, if you apply the Third Law of the Equinox, I suppose it wouldn't hurt to let slip a word or two. So long as you remember your Rites of Obfuscation, of course.
                switch (selection) {
                    // $script:1126150707011949$
                    // - Of... of course...
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:1126150707011950$
                // - You can't take these things too lightly. I once spoke the Three Devastating Truths to an insuitably prepared koborc, and it inverted into a quasi-nonsubstantiated autoform. Ha-ha!
                switch (selection) {
                    // $script:1126150707011951$
                    // - Is that... funny...?
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:1126150707011952$
                // - You don't think so? I suppose my sense of humor is more sophisticated than most.
                switch (selection) {
                    // $script:1126150707011953$
                    // - Anyway, about the Lumiknights?
                    case 0:
                        return 35;
                }
                return -1;
            case (35, 0):
                // $script:1126150707011954$
                // - Before you can even begin to comprehend the Lumiknights, you must open your mind to the myriad possibilities of the universe. It can take years of study. Shall we begin with a light reading of the Tome of Bombastic Insensations?
                switch (selection) {
                    // $script:1126150707011955$
                    // - You know what? Never mind.
                    case 0:
                        return 36;
                }
                return -1;
            case (36, 0):
                // $script:1126150707011956$
                // - How unfortunate. Well, if you change your mind, you know where to find me.
                return -1;
            case (40, 0):
                // $script:1126150707011957$
                // - You are not prepared.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.SelectableDistractor,
            (36, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
