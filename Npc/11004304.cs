using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004304: Ghost
/// </summary>
public class _11004304 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1002141907011434$
    // - Can you see me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1002141907011437$
                // - I guess living people really can see ghosts on Halloween.
                return 30;
            case (30, 1):
                // $script:1002141907011438$
                // - Please don't ask me if I saw anything...
                switch (selection) {
                    // $script:1002141907011439$
                    // - Did you see anything?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1002141907011440$
                // - N-no! I don't want <i>that woman</i> coming after me, so the answer is no!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
