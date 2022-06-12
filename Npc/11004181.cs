using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004181: Red Cape
/// </summary>
public class _11004181 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010624$
    // - What do <i>you</i> want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010625$
                // - None of this makes any sense.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
