using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001710: Tinchai
/// </summary>
public class _11001710 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006962$
    // - Mm?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0728024507006992$
                // - Were your contacts any good this time?
                switch (selection) {
                    // $script:0805021607007084$
                    // - Your informants are little cuties.
                    case 0:
                        return 31;
                    // $script:0805021607007085$
                    // - Is their information reliable?
                    case 1:
                        return 40;
                }
                return -1;
            case (31, 0):
                // $script:0805021607007086$
                // - I suppose they are! Don't judge them by their looks, though. They've got a knack for gathering information.
                switch (selection) {
                    // $script:0805021607007087$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (40, 0):
                // $script:0805021607007088$
                // - I can't think of any reason it wouldn't be. If you're worried, I'll vouch for them personally. They've never failed me in the past.
                switch (selection) {
                    // $script:0805021607007089$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}
