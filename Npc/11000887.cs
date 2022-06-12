using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000887: Grinika
/// </summary>
public class _11000887 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003250$
    // - What do I do?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003253$
                // - Did you know Ten was a Kaka? So am I. Heh heh.
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
