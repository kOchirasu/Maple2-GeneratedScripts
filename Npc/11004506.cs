using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004506: Mannstad Sentry
/// </summary>
public class _11004506 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012436$
    // - I know your face. Road in on that primitive flying boat, didn't you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012437$
                // - I know your face. Road in on that primitive flying boat, didn't you?
                switch (selection) {
                    // $script:1228182607012438$
                    // - That's right.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1228182607012439$
                // - Hmph. You did good work in Richmonde, I'll give you that.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
