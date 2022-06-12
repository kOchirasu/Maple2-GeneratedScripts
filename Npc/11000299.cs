using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000299: Jake
/// </summary>
public class _11000299 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001188$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001190$
                // - Things around here have never been THIS bad. Maybe it's time for a change of career.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
