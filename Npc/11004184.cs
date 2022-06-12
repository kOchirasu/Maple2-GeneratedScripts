using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004184: Eupheria
/// </summary>
public class _11004184 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010630$
    // - Do you need something?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010631$
                // - It's certainly reassuring to have these two at my side, but we have a lot of work ahead of us if we intend to come out on top.
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
