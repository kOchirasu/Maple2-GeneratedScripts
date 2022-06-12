using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004171: Startz
/// </summary>
public class _11004171 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010599$
    // - Order now or get a face full of burning oil. Your choice. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010600$
                // - Don't get the wrong idea. I'm not here selling churros because my restaurant is doing poorly, I'm just here to enjoy myself.
                switch (selection) {
                    // $script:0806025707010601$
                    // - So then why ARE you selling churros?
                    case 0:
                        return 11;
                    // $script:0806025707010602$
                    // - Can I have a churro?
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // $script:0806025707010603$
                // - Huh? Because I like to cook, obviously.
                return 11;
            case (11, 1):
                // $script:0806025707010604$
                // - Well... If I'm being honest, we all trekked all the way here to $map:02000499$ to take a vacation, but we ran out of money to pay for lodging.
                return -1;
            case (12, 0):
                // $script:0806025707010605$
                // - They're not done yet. Come back later.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Close,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
