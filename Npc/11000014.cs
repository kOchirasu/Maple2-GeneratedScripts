using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000014: Kalanko
/// </summary>
public class _11000014 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000067$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000069$
                // - W-who are you? You better not be here to steal anything. This is my spot!
                switch (selection) {
                    // $script:0831180407000070$
                    // - That's right.
                    case 0:
                        return 21;
                    // $script:0831180407000071$
                    // - No.
                    case 1:
                        return 22;
                }
                return -1;
            case (21, 0):
                // $script:0831180407000072$
                // - Hey, no! Get out! If we take too much stuff, they'll notice for sure!
                return -1;
            case (22, 0):
                // $script:0831180407000073$
                // - Oh, okay. Good. You'd better get out of here then, before someone sees you. And don't tell anyone you saw me in here!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
