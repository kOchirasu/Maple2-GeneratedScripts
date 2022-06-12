using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000235: Tracy
/// </summary>
public class _11000235 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407001000$
    // - Sigh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001004$
                // - Mm? You're not the person I saw.
                switch (selection) {
                    // $script:0831180407001005$
                    // - What are you doing?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407001006$
                // - I don't know. I don't know why I'm doing this, so please stop talking to me.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
