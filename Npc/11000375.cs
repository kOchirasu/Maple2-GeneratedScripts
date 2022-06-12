using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000375: Luvar
/// </summary>
public class _11000375 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001541$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001543$
                // - Enoki mushrooms grow here. They require clean, undisturbed areas to flourish. I suppose no one ever comes to this valley, then.
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
