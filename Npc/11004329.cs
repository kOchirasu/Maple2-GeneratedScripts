using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004329: Jorge
/// </summary>
public class _11004329 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    protected override int Select() {
        // Select 0:
        // $script:1102172107011629$
        // - I see... What a novel approach.
        // Select 20:
        // $script:1010140307011535$
        // - I see... What a novel approach.
        // TODO: 0,20
        return 0;
    }

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1102172107011630$
                // - I see... What a novel approach.
                return -1;
            case (30, 0):
                // $script:1010140307011536$
                // - I see... What a novel approach.
                switch (selection) {
                    // $script:1010140307011537$
                    // - What are you working on there?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:1010140307011538$
                // - Hm? Oh, I'm doing research on the magic of this continent!
                return 40;
            case (40, 1):
                // $script:1010140307011539$
                // - The rumors have already spread as far as $map:02000023$ that the people of this continent practice a form of magic we've never seen.
                return 40;
            case (40, 2):
                // $script:1010140307011540$
                // - There's no way that I would miss such a tantalizing opportunity for self-edification.
                return 40;
            case (40, 3):
                // $script:1010140307011541$
                // - Just you wait! I'm on the verge of a groundbreaking discovery, one for the history books!
                switch (selection) {
                    // $script:0111232407012695$
                    // - I look forward to hearing all about it.
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:0111232407012696$
                // - Indeed!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Next,
            (40, 3) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
