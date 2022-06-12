using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000873: Bostie
/// </summary>
public class _11000873 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003155$
    // - Sigh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003158$
                // - I've got this awful, creeping feeling that something bad is coming. I really hope I'm wrong.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
